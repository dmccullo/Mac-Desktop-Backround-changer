import os
import random
import urllib.request

url = 'http://wallpaperswide.com/vintage-desktop-wallpapers.html' # the url of the website with images
res = '2048x1152' #the desired resolution of the images
path = "/Users/don.mccullough/Pictures/DWM Desktops" # the path where the downloaded images will be stored

# retrieve the source code of the website
response = urllib.request.urlopen(url)
source_code = response.read().decode()
start_index = 0
while start_index != -1: # find all the links to the images
    img_start = source_code.find('<img src="', start_index)
    if img_start == -1:
        break
    img_start += len('<img src="')
    img_end = source_code.find('"', img_start)
    img_url = source_code[img_start:img_end]
    if res in img_url: # check if the image has the desired resolution
        img_name = os.path.basename(img_url)
        img_path = os.path.join(path, img_name)
        urllib.request.urlretrieve(img_url, img_path) # download the image
    start_index = img_end

# select a random image from the downloaded ones
img_list = os.listdir(path)
img_name = random.choice(img_list)

# set the selected image as desktop background
osascript = f'tell application "Finder" to set desktop picture to POSIX file "{os.path.join(path, img_name)}"'
os.system(f"osascript -e '{osascript}'")
