# This script converts jpegs to movies

FRAMES="/path/to/frames-2/frame-%06d.jpeg"
OUTPUT="/path/to/guest.mov"

ffmpeg -y -i ${FRAMES} -vb 20M -c:v libx264 -vf fps=25 -pix_fmt yuv420p ${OUTPUT}
