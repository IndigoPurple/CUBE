python inference.py \
    --prompt "A blue sofa in a house." \
    --condition "canny" \
    --video_path "data/sofa.mp4" \
    --output_path "outputs/" \
    --video_length 7 \
    --smoother_steps 19 20 \
    --width 448 \
    --height 256
    #--is_long_video
    
echo "DONE! A blue sofa in a house."

python inference.py \
    --prompt "A green sofa in a house." \
    --condition "canny" \
    --video_path "data/sofa.mp4" \
    --output_path "outputs/" \
    --video_length 7 \
    --smoother_steps 19 20 \
    --width 448 \
    --height 256
    #--is_long_video
    
echo "DONE! A green sofa in a house."

python inference.py \
    --prompt "A modern sofa in a house." \
    --condition "canny" \
    --video_path "data/sofa.mp4" \
    --output_path "outputs/" \
    --video_length 7 \
    --smoother_steps 19 20 \
    --width 448 \
    --height 256
    #--is_long_video
    
echo "DONE! A modern sofa in a house."
