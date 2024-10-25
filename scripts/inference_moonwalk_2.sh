python inference.py \
    --prompt "An astronaut does the moonwalk on the moon." \
    --condition "canny" \
    --video_path "../data/moonwalk.mp4" \
    --output_path "outputs/" \
    --video_length 15 \
    --smoother_steps 19 20 \
    --width 512 \
    --height 512
    #--is_long_video
