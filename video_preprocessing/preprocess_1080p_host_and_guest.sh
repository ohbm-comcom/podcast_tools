# This script downscales, add black bars to two 1080p videos and stacks them

HOST="/home/faruk/podcast/host.mov"
GUEST="/home/faruk/podcast/guest.mov"

OUTPUT="/home/faruk/podcast/episode4_ready_to_edit.mov"

# =============================================================================
# STAGE 1: Rescale
ffmpeg -i ${HOST} -max_muxing_queue_size 1024 -vf scale=960:540 "${HOST%.mov}_step-01.mov"
ffmpeg -i ${GUEST} -max_muxing_queue_size 1024 -vf scale=960:540 "${GUEST%.mov}_step-01.mov"

# =============================================================================
# STAGE 2: Add black bars
ffmpeg -i "${HOST%.mov}_step-01.mov" -vf "pad=width=960:height=1080:x=0:y=270:color=black" "${HOST%.mov}_step-02.mov"
ffmpeg -i "${GUEST%.mov}_step-01.mov" -vf "pad=width=960:height=1080:x=0:y=270:color=black" "${GUEST%.mov}_step-02.mov"

# =============================================================================
# STAGE 2: Stack horizontally
ffmpeg -i "${HOST%.mov}_step-02.mov" -i "${GUEST%.mov}_step-02.mov" -filter_complex hstack=inputs=2 ${OUTPUT}

echo "Finished."
