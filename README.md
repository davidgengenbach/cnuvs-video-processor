# :)
```shell
# If you use windows, I feel bad for you son
# I got 99 problems, but windows portability ain't one
./download-and-create-video FOLDER_TO_HOLD_DATA LECTURE_URL
```
## Instructions
The `FOLDER_TO_HOLD_DATA` gets created if not existent.

Grab the lecture url from the cls site (for example `http://clls.rbg.informatik.tu-darmstadt.de:8080/recording/c1e7e95bf36082f4-59f138e30e8ce800`).

Then just:
```
./download-and-create-video 'TESTUNDSO' 'http://clls.rbg.informatik.tu-darmstadt.de:8080/recording/c1e7e95bf36082f4-59f138e30e8ce800'
```
This will take a while since it downloads the video if not existent in that folder.