python inference.py \
    --prompt "A girl with golden hair, crying, facing the sky." \
    --condition "canny" \
    --video_path "data/woman.mp4" \
    --output_path "outputs/" \
    --video_length 7 \
    --smoother_steps 19 20 \
    --width 448 \
    --height 256
    #--is_long_video
    
echo "A girl with golden hair, crying, facing the sky."

python inference.py \
    --prompt "A girl with golden hair, smiling." \
    --condition "canny" \
    --video_path "data/woman.mp4" \
    --output_path "outputs/" \
    --video_length 7 \
    --smoother_steps 19 20 \
    --width 448 \
    --height 256
    #--is_long_video
    
echo "A girl with golden hair, smiling."

python inference.py \
    --prompt "A girl with long hair, movie style." \
    --condition "canny" \
    --video_path "data/woman.mp4" \
    --output_path "outputs/" \
    --video_length 7 \
    --smoother_steps 19 20 \
    --width 448 \
    --height 256
    #--is_long_video
    
echo "A girl with long hair, movie style."
