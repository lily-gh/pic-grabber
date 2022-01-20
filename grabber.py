# -*- coding: utf-8 -*-
import os, errno, re, urllib, uuid, csv

# Open URLs file 
urls_file = open('pic-urls.txt', 'r') 

count = 0  
print("Fetching pictures...")
for url in urls_file: 
    count += 1
    print("[Count: {}] Downloading: {}".format(count, url.strip()))

    try:
        filename = os.path.basename(url.strip())
        file_fullpath = 'output/' + filename
        urllib.urlretrieve(url, 'output/' + filename)
    except Exception:
        print("Error saving picture locally.")
        pass
  
# Close file
urls_file.close() 
