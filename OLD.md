# Links:
http://forum.videohelp.com/threads/349492-Force-left-audio-channel-to-both-speakers
https://ffmpeg.org/ffmpeg.html
https://trac.ffmpeg.org/wiki/AudioChannelManipulation

# Copy left to right channel tests:
ffmpeg -i audio.mp3 -ac 2 out.mp3
ffmpeg -i audio.mp3 -map_channel 0.0.1 -map_channel 0.0.0 out.mp3
ffmpeg -i audio.mp3 -map_channel -1 -map_channel 0.0.1 out.mp3
ffmpeg -i audio.mp3 -map_channel 0.0.1 out.mp3
ffmpeg -i audio.mp3 -map_channel 0.1.1 -map_channel 0.1.1 out.mp3
ffmpeg -i audio.mp3 -af "pan=stereo|c0<c0+c1|c1<c0+c1" out.mp3
ffmpeg -i audio.mp3 -ac 2 -map_channel 0.1.0 -map_channel 0.1.0 out.mp3
ffmpeg -i audio.mp3 -vcodec copy -acodec libfaac -ab 220k -ar 48000 -ac 1 out.mp4
ffmpeg -i video.mp4 -q:a 0 -map a -vcodec copy -ab 220k -ar 48000 -ac 1 audio2.ogg