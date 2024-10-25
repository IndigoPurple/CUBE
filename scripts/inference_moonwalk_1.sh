python inference.py \
    --prompt "James bond does the moonwalk on the desert." \
    --condition "canny" \
    --video_path "data/moonwalk.mp4" \
    --output_path "outputs/" \
    --video_length 15 \
    --video_length 15 \
    --smoother_steps 19 20 \
    --width 512 \
    --height 512
    #--is_long_video

echo "DONE! James bond does the moonwalk on the desert."

python inference.py \
    --prompt "An astronaut does the moonwalk on the moon." \
    --condition "canny" \
    --video_path "data/moonwalk.mp4" \
    --output_path "outputs/" \
    --video_length 15 \
    --video_length 15 \
    --smoother_steps 19 20 \
    --width 512 \
    --height 512
    #--is_long_video
    
echo "DONE! An astronaut does the moonwalk on the moon."

python inference.py \
    --prompt "Iron man does the moonwalk on the road." \
    --condition "canny" \
    --video_path "data/moonwalk.mp4" \
    --output_path "outputs/" \
    --video_length 15 \
    --video_length 15 \
    --smoother_steps 19 20 \
    --width 512 \
    --height 512
    #--is_long_video
    
echo "DONE! Iron man does the moonwalk on the road."
