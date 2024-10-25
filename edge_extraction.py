import numpy
import numpy as np
import torch
import h5py
import cv2

def interpolate_to_image(pxs, pys, dxs, dys, weights, img):
    """
    Accumulate x and y coords to an image using bilinear interpolation
    """
    img.index_put_((pys,   pxs  ), weights*(1.0-dxs)*(1.0-dys), accumulate=True)
    img.index_put_((pys,   pxs+1), weights*dxs*(1.0-dys), accumulate=True)
    img.index_put_((pys+1, pxs  ), weights*(1.0-dxs)*dys, accumulate=True)
    img.index_put_((pys+1, pxs+1), weights*dxs*dys, accumulate=True)
    return img

def events_to_image_torch(xs, ys, ps,
        device=None, sensor_size=(180, 240), clip_out_of_range=True,
        interpolation=None, padding=True):
    """
    Method to turn event tensor to image. Allows for bilinear interpolation.
        :param xs: tensor of x coords of events
        :param ys: tensor of y coords of events
        :param ps: tensor of event polarities/weights
        :param device: the device on which the image is. If none, set to events device
        :param sensor_size: the size of the image sensor/output image
        :param clip_out_of_range: if the events go beyond the desired image size,
            clip the events to fit into the image
        :param interpolation: which interpolation to use. Options=None,'bilinear'
        :param padding if bilinear interpolation, allow padding the image by 1 to allow events to fit:
    """
    if device is None:
        device = xs.device
    if interpolation == 'bilinear' and padding:
        img_size = (sensor_size[0]+1, sensor_size[1]+1)
    else:
        img_size = list(sensor_size)

    mask = torch.ones(xs.size(), device=device)
    if clip_out_of_range:
        zero_v = torch.tensor([0.], device=device)
        ones_v = torch.tensor([1.], device=device)
        clipx = img_size[1] if interpolation is None and padding==False else img_size[1]-1
        clipy = img_size[0] if interpolation is None and padding==False else img_size[0]-1
        mask = torch.where(xs>=clipx, zero_v, ones_v)*torch.where(ys>=clipy, zero_v, ones_v)

    img = torch.zeros(img_size).to(device)
    if interpolation == 'bilinear' and xs.dtype is not torch.long and xs.dtype is not torch.long:
        pxs = (xs.floor()).float()
        pys = (ys.floor()).float()
        dxs = (xs-pxs).float()
        dys = (ys-pys).float()
        pxs = (pxs*mask).long()
        pys = (pys*mask).long()
        masked_ps = ps.squeeze()*mask
        interpolate_to_image(pxs, pys, dxs, dys, masked_ps, img)
    else:
        if xs.dtype is not torch.long:
            xs = xs.long().to(device)
        if ys.dtype is not torch.long:
            ys = ys.long().to(device)
        img.index_put_((ys, xs), ps, accumulate=True)
    return img

def events_to_image(xs, ys, ps, sensor_size=(180, 240), interpolation='bilinear' , padding=False):
    """
    Place events into an image using numpy
    """
    if interpolation == 'bilinear' and xs.dtype is not torch.long and xs.dtype is not torch.long:
        # xt, yt, pt = torch.from_numpy(xs), torch.from_numpy(ys), torch.from_numpy(ps)
        # xt, yt, pt = xt.float(), yt.float(), pt.float()
        # img = events_to_image_torch(xt, yt, pt, clip_out_of_range=True, interpolation='bilinear', padding=padding)
        pt = torch.from_numpy(ps)
        pt = pt.float()
        img = events_to_image_torch(xs, ys, pt, sensor_size=sensor_size,clip_out_of_range=True, interpolation='bilinear', padding=padding)
        img = img.numpy()
    else:
        coords = np.stack((ys, xs))
        try:
            abs_coords = np.ravel_multi_index(coords, sensor_size)
        except ValueError:
            print("Issue with input arrays! coords.shape={}, sum(coords)={}, sensor_size={}. \n minx={}, maxx={}, miny={}, maxy={}".format(coords.shape, np.sum(coords), sensor_size, np.min(xs), np.max(xs), np.min(ys), np.max(ys)))
            raise ValueError
        img = np.bincount(abs_coords, weights=ps, minlength=sensor_size[0]*sensor_size[1])
    img = img.reshape(sensor_size)
    return img




def time_window(xs, ys, ts, ps, s, win):
    loc = np.where((ts <= s + win) & (ts >= s))

    ts, xs, ys, ps = ts[loc], xs[loc], ys[loc], ps[loc]

    return xs, ys, ts, ps

if __name__ == "__main__":
    """
    Example use
    """
    file_name_list = ['violin','sofa','man','girl']

    # img = events_to_image(xs, ys, ps,  interpolation="None", sensor_size=(260, 346))
    h,w,c = 256,448,3
    # current_frame = numpy.ones((h,w,c)) * 255
    current_frame = numpy.zeros((h, w, c))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    aug = 1.5
    for f in range(len(file_name_list)):
        input_file = './data/event/%s.h5'%file_name_list[f]
        output_path = './data/edge/%s.mp4'%file_name_list[f]
        video = cv2.VideoWriter(output_path, fourcc, 30, (w, h))

        with h5py.File(input_file, "r") as f:
            # events = np.sort(f['events'][:,:3],axis=0)
            # events =np.array(f['events'])
            events = f['events']
            ts,xs,ys,ps = events[:,0], events[:,1], events[:,2], events[:,3]
        event_num = len(xs)
        slice_len = event_num//7
        for t in range(6):
            for i in range(slice_len):
                current_frame[ys[i+t*slice_len], xs[i+t*slice_len]] += (1,1,1)
            video.write(np.uint8(current_frame/(current_frame.max()-current_frame.min())*255*aug))
            current_frame = numpy.zeros((h, w, c))
        for i in range(event_num-slice_len,event_num):
            current_frame[ys[i], xs[i]] += (1, 1, 1)
        video.write(np.uint8(current_frame / (current_frame.max() - current_frame.min()) * 255*aug))
        current_frame = numpy.zeros((h, w, c))
        cv2.destroyAllWindows()
        video.release()

    print('-------------------------------------------------------------------------------------------------------')
    print('| Event streams are all processed to extract edges, which could be found in the \'./data/edge\' folder. |')
    print(
        '-------------------------------------------------------------------------------------------------------')
    # current_ti = ts[0]
    # frame_id = 0
    #
    # # slice_len = event_num // 16
    # for i in range(event_num):
    #     if ts[i] == current_ti:
    #         current_frame[ys[i], xs[i],:] = 255, 255, 255
    #         # current_frame[ys[i], xs[i], :] = 0,0,0
    #     else:
    #         # print('here',ts[i])
    #         current_ti = ts[i]
    #         cv2.imwrite('temp/frame%02d.png'%frame_id, current_frame)
    #         # current_frame = numpy.ones((h, w, c)) * 255
    #         current_frame = numpy.zeros((h, w, c))
    #         frame_id +=1
    # print(frame_id)

        # current_frame[ys[i*slice_len:(i+1)*slice_len], xs[i*slice_len:(i+1)*slice_len],:] = 255,255,255
        # current_frame[ys[i * slice_len:(i + 1) * slice_len], xs[i * slice_len:(i + 1) * slice_len], :] = 255, 255, 255
        # cv2.imwrite('temp11.png',current_frame)
        # exit()