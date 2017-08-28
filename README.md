```
 __ __   ___   __ __  ______  __ __  ____     ___        ____ ____ 
|  |  | /   \ |  |  ||      ||  |  ||    \   /  _]      |    \    |
|  |  ||     ||  |  ||      ||  |  ||  o  ) /  [_ _____ |  o  )  | 
|  ~  ||  O  ||  |  ||_|  |_||  |  ||     ||    _]     ||   _/|  | 
|___, ||     ||  :  |  |  |  |  :  ||  O  ||   [_|_____||  |  |  | 
|     ||     ||     |  |  |  |     ||     ||     |      |  |  |  | 
|____/  \___/  \__,_|  |__|   \__,_||_____||_____|      |__| |____|

```



This script can be run on a Raspberry Pi and will continuously play Youtube videos from a particular account or playlist. 

![My Youtube-PI](https://raw.githubusercontent.com/jeffcrouse/youtube-pi/master/youtube-pi.jpg)

## Requirements

- youtube-dl https://rg3.github.io/youtube-dl/

## Editing

- channelId: Change which videos are played (default: "UCceEPxhcejQiYza8bvuAA8g")
- directory: Change where the videos are stored (default: ./videos) 

## Installation

Set up a Raspberry Pi as you normally would. 

Get a Youtube API key from https://console.developers.google.com/apis/dashboard

Set an environment variable with your YouTube API key. You can do this by addint the following line to your /home/pi/.profile

``export YOUTUBE_DATA_API_KEY=AIzaSyC5uMOtb0fPlXR6PN1Ii8CtLICWv9CucRM`` (inactive key)


Put this script somewhere (I just put it right in the home directory) and run it.

``nohup python /home/pi/youtube-pi.py > youtube-pi.out &``

Optionally, you can put the following line into your /etc/rc.local

``python /home/pi/youtube-pi.py > youtube-pi.out &``