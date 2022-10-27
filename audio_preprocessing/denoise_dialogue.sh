# This script **might** help if the audio is poor quality

INPUT="audio_audio.wav"
OUTPUT="audio_guest_denoised.wav"

ffmpeg -i ${INPUT} -af "highpass=f=300,asendcmd=0.0 afftdn sn start,asendcmd=1.5 afftdn sn stop,afftdn=nf=-20,lowpass=f=3000" ${OUTPUT}
