#!/usr/bin/env python3

"""Scrapes the list of provided subreddits for images and downloads them to a local directory"""

__author__ = "Patrick Guelcher"
__copyright__ = "(C) 2016 Patrick Guelcher"
__license__ = "MIT"
__version__ = "4.0"

import json
import os
import requests
import urllib.error
import wget

# Configuration
root_path = 'img' # Download folder (Default: scrape)
sub_list = [
            'CursedSpongebob'
            ] # Subreddit list
post_limit = 15 # Sumbission limit to check and download

# Do not edit beyond this comment
def create_folders():
    os.makedirs(root_path, exist_ok=True)
    for sub in sub_list:
        os.makedirs(os.path.join(root_path,str(sub)), exist_ok=True)
    # else:
    #     print("DirectoryError: Could not create directory for " + sub)

def download_images(sub, post_limit):
    r = requests.get('https://www.reddit.com/r/' + sub + '.json?limit=' + str(post_limit), headers = {'User-agent': 'Image Scraper by /u/AeroBlitz'})
    print('https://www.reddit.com/r/' + sub + '.json?limit=' + str(post_limit))
    sub_json = json.loads(r.text)
    # print(sub_json)
    download_path = root_path + '/'
    for n in range(0, post_limit):
        url = sub_json["data"]["children"][n]["data"]["url"]
        if url is not None:
            file_name = url
            extension = url[-4:]
            if extension == '.jpg' or extension == '.png':
                print ("\n" + url)
                try:
                    wget.download(url, download_path)
                except (IndexError, urllib.error.HTTPError):
                    print ("\n" + "DownloadError: Skipping file download.")
                    pass
            else:
                pass
        else:
            pass

def main():
    
    for sub in sub_list:
        download_images(sub, post_limit)
    else:
        print("\n" + "\n" + "Scrape Completed." + "\n")

if __name__ == '__main__':
    main()