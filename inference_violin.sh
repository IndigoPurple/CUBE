python inference.py \
    --prompt "A girl wearing glasses is playing a violin." \
    --condition "canny" \
    --video_path "data/violin.mp4" \
    --output_path "outputs/" \
    --video_length 7 \
    --smoother_steps 19 20 \
    --width 448 \
    --height 256
    #--is_long_video
    
echo "DONE! A girl wearing glasses is playing a violin."

