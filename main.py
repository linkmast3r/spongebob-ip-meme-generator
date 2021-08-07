import functions, os, re, random, reddit_scrappe
from PIL import Image
rotMatrix = lambda a: np.array( [[np.cos(a),np.sin(a)], 
                    [-np.sin(a),np.cos(a)]] )


root_path = 'img' # Download folder (Default: scrape)
sub_list = [
            'CursedSpongebob'
            ] # Subreddit list
post_limit = 15 # Sumbission limit to check and download

## scrappe reddit
for sub in sub_list:
    reddit_scrappe.download_images(sub, post_limit)
else:
    print("\n" + "\n" + "Scrape Completed." + "\n")


os.system("rm -rf img/*\)* && rm -rf vid/*\)*")
# get random image to make a video
get_imgs = os.listdir("img")
images = []
for f in get_imgs:
    if(re.search("\w*.jpg", f)):
        im = Image.open("img/" + str(f))
        name = "img/" + str(f).split(".")[0] + ".png"
        im.save(name)
    elif(re.search("\w*.png", f)):
        images.append(f)



os.system("rm -rf img/*jpg && rm -rf img/*).jpg && rm -rf vid/*).mp4")
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

# create video from image and music
functions.create_video(random_img, random_song)

# generates the meme from a video and an IP form random proxies
functions.make_video(random_video, functions.getIP())
os.system("rm -rf img/*jpg && rm -rf img/*\).jpg && rm -rf vid/*\).mp4")
