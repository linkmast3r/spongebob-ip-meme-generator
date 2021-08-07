from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
import random, re, os, cv2, sys
import animation
import numpy as np
import random
import PIL
from PIL import Image

get_imgs = os.listdir("img")
images = []
for f in get_imgs:
    if(re.search("\w*.png", f)):
        images.append(f)


# list all videos
get_files = os.listdir("vid")
videos = []
for f in get_files:
    if(re.search("\w*.mp4", f)):
        videos.append(f)

# list all videos
get_songs = os.listdir("music")
songs = []
for f in get_songs:
    if(re.search("\w*.mp3", f)):
        songs.append(f)

# choose random song, video and image
random_video = random.choice(videos)
random_img = random.choice(images)
random_song = random.choice(songs)



def getIP():
    ip = ".".join(map(str, (random.randint(0, 255) 
                        for _ in range(4))))

    return ip

def create_video(image, song):
    
    # create a video from an image
    img = ["img/" + str(image)]

    clips = [ImageClip(m).set_duration(9)
      for m in img]

    # create a clip from a song
    audioclip = AudioFileClip("music/" + song).subclip(0, 9)
    
    image_video = concatenate_videoclips(clips, method="compose")

    # put together images and audio
    video_name = "vid/" + str(image).split(".")[0] + ".mp4"

    videoclip = image_video.set_audio(audioclip)

    videoclip.write_videofile(video_name,fps=25,codec='mpeg4')

def make_animate_letters(img, ip, song, color):
    rotMatrix = lambda a: np.array( [[np.cos(a),np.sin(a)], 
                            [-np.sin(a),np.cos(a)]] )
    
    
    image = "img/" + str(img)

   
    imag = PIL.Image.open(image)

    wid, hgt = imag.size

    height = int(hgt)
    width = int(wid)


    
    #size_font = area*120/624600
    size_font = height/8

    screensize = (int(wid) - random.randint(0,150),int(hgt) - random.randint(0,150))
    txtClip = TextClip(ip,color=color, font="Arial", kerning = 5, fontsize=size_font)

    txtClip = txtClip.set_pos('center')



    letters = findObjects(txtClip)

    # WE ANIMATE THE LETTERS

    animations = [animation.vortexout, animation.vortex, animation.cascade, animation.arrive]
    random_anim = random.choice(animations)
    
    clips = [ CompositeVideoClip( animation.moveLetters(letters,funcpos),
                                size = screensize).subclip(0,5)
            for funcpos in [random_anim] ]

    # WE CONCATENATE EVERYTHING AND WRITE TO A FILE

    audioclip = AudioFileClip("music/" + song).subclip(0, 9)

    final_clip = concatenate_videoclips(clips)
    image_clip =  ImageClip(image, duration=final_clip.duration)
    final_clip = CompositeVideoClip([image_clip,final_clip.set_pos('center')])

    videoclip = final_clip.set_audio(audioclip)
    video_name = "./" + str(img).split(".")[0] + ".mp4"




    
    videoclip.write_videofile(video_name,fps=25,codec='mpeg4')
    return video_name


def make_video(source, ip):
    clip = VideoFileClip("vid/" + source)

    # gets size of the video
    file_path = "./vid/" +  source
    vid = cv2.VideoCapture(file_path)

    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))



    #size_font = area*120/624600
    size_font = height/8

    colors = ["red", "white", "green", "black", "blue", "purple"]

    # generates the text
    txt_clip = TextClip(ip,fontsize=size_font,color=random.choice(colors),kerning = 5)


    animations = ["center", "slow", "lmao", "lmao", "lmao", "lmao"]
    # random.choice(animations)
    random_animation = random.choice(animations)

    if random_animation == "center":
        txt_clip = txt_clip.set_pos('center').set_duration(clip.duration-3)
        video = CompositeVideoClip([clip,txt_clip.set_start(1).crossfadein(2)])
    elif random_animation == "slow":
        txt_clip = txt_clip.set_position(lambda t:(30*t,50*t)).set_duration(clip.duration-3)
        video = CompositeVideoClip([clip,txt_clip.set_start(1).crossfadein(2)])
    elif random_animation == "lmao":
        video_name = make_animate_letters(random_img, getIP(), random_song, random.choice(colors))
        os.system("ffmpeg -i " + video_name + " " + source + "_ready_edited.mp4) 
        sys.exit(0)


    # puts together both parts

    src_name = source.split('.')[0]
    video_name = './' + src_name + "-edited.mp4"
    video.write_videofile(video_name,fps=25,codec='mpeg4')

    ## Si se comenta esta línea, hay un bug en discord en el cual no se muestra la IP
    os.system("ffmpeg -i " + video_name + " " + source + "_ready_edited.mp4)



