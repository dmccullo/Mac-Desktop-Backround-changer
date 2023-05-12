import urllib.request
import urllib.parse
import re
import os
import random
import subprocess

def get_image_urls():
    page_url = 'https://wallpaperswide.com/new_wallpapers/page/{}/'
    urls = []
    for page in range(1, 11): # scrape 10 pages of new wallpapers
        url = page_url.format(page)
        with urllib.request.urlopen(url) as url:
            page_bytes = url.read()
            page_html = page_bytes.decode('utf-8')
            image_blocks = re.findall(r'<div class="thumb">(.*?)<\/div>', page_html, re.DOTALL)
            for block in image_blocks:
                match = re.search(r'<a href="(.*?)"', block)
                if match:
                    url = match.group(1)
                    urls.append(url)
    return urls

def download_image(url):
    with urllib.request.urlopen(url) as img_url:
        img_bytes = img_url.read()
    filename = os.path.basename(url)
    with open(filename, 'wb') as img_file:
        img_file.write(img_bytes)
    return filename

def set_desktop_image(filename):
    cmd = 'osascript -e \'tell application "Finder" to set desktop picture to POSIX file "{}"\''
    subprocess.call(cmd.format(os.path.abspath(filename)), shell=True)

if __name__ == '__main__':
    urls = get_image_urls()
    url = random.choice(urls)
    filename = download_image(url)
    set_desktop_image(filename)

