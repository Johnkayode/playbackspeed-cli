#import os for file paths
import os
#importing google fire library to create beautiful CLIs
import fire
#importing moviepy library for video manipulation
from moviepy.editor import *

def convert(video=None,speed=None):
    '''
    This function receives two parameters "video", relative path to the video and "speed", the wanted  video playback speed
    It rewrites the video with the speed parameter into a new file and saves it in the project directory
    '''

    if video==None and speed==None:
        print("You can simply change playback speed of a video with python videoplayback.py change_playback_speed --video {video_filename} --speed {speed}")
        print("E.g python videoplayback.py change_playback_speed --video path\\to\\video.mp4 --speed 2")
        video = input('$ Video filename (ensure it is a relative path): ')
        
        speed = input('$ Type speed here: ')
        
    try:  
        video_name = os.path.basename(video)
    except:
        video_name = video

    
    try:
        print(f'{video_name} playback speed will be increased by {speed}')
        clip = VideoFileClip(video)
        print('Play back speed will be changed in a moment....')
        final = clip.fx(vfx.speedx, speed)
        new_filename = f"new_{video_name}"
        final.write_videofile(new_filename)
        print(f'Video saved as {new_filename}')
    except:
        print('Oops, an error occured. Try again!')
    



class Pipeline(object):
    def __init__(self):
        #assigns a command to a function
        self.change_playback_speed = convert

if __name__ == '__main__':
    fire.Fire(Pipeline)
    

