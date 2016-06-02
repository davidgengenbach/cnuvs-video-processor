# :)
```shell
# If you use windows, I feel bad for you son
# I got 99 problems, but windows portability ain't one
./create-video.sh [FOLDER]
```
## Instructions
Files needed for conversion:
- `slides.json`
- `video.mp4`

Place them in a folder [FOLDER].
You can get the `video.mp4` and `slides.json` from the lecture site:

`http://clls.rbg.informatik.tu-darmstadt.de:8080/recording/c1e7e95bf36082f4-59f138e30e8ce800`

The [ID] of the lecture is the last URL part (here `c1e7e95bf36082f4-59f138e30e8ce800`).

The [ID_SPLITTED] is the [ID] with the '-' replaced with '/' (here `c1e7e95bf36082f4/59f138e30e8ce800`).

You can get the `slides.json` by downloading:

`http://clls.rbg.informatik.tu-darmstadt.de:8080/api/slides/[ID]`

and the `videos.mp4` by downloading:

`http://clls.rbg.informatik.tu-darmstadt.de/clls/lecturematerial/[ID_SPLITTED]/videos/video.mp4`


Now you are ready to convert