python inference.py \
    --prompt "an old man wearing a glass, cartoon." \
    --condition "canny" \
    --video_path "data/man.mp4" \
    --output_path "outputs/" \
    --video_length 7 \
    --smoother_steps 19 20 \
    --width 448 \
    --height 256
    #--is_long_video
    
echo "DONE! an old man wearing a glass, cartoon."

python inference.py \
    --prompt "an old man wearing a glass, laughing." \
    --condition "canny" \
    --video_path "data/man.mp4" \
    --output_path "outputs/" \
    --video_length 7 \
    --smoother_steps 19 20 \
    --width 448 \
    --height 256
    #--is_long_video
    
echo "DONE! an old man wearing a glass, laughing."

python inference.py \
    --prompt "an old man wearing a glass, oil painting." \
    --condition "canny" \
    --video_path "data/man.mp4" \
    --output_path "outputs/" \
    --video_length 7 \
    --smoother_steps 19 20 \
    --width 448 \
    --height 256
    #--is_long_video
    
echo "DONE! an old man wearing a glass, oil painting."
