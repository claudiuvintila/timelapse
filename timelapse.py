#!/usr/bin/env python

from subprocess import call
import sys

__author__ = 'claudiu.vintila@gmail.com'

import fnmatch
import os
import datetime
import time


def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


print "Gathering images..."

spinner = spinning_cursor()
imgs = []


def spin():
    sys.stdout.write(spinner.next())
    sys.stdout.flush()
    sys.stdout.write('\b')


for root, dir_names, file_names in os.walk('./'):
    for filename in fnmatch.filter(file_names, '*.JPG'):
        img_path = os.path.join(root, filename)
        img_date_time_string = time.ctime(os.path.getctime(img_path))

        imgDateTime = datetime.datetime.strptime(img_date_time_string, "%a %b %d %H:%M:%S %Y")
        imgDateTimestamp = time.mktime(imgDateTime.timetuple())

        imgs.append({
            'file_name': filename,
            'timestamp': imgDateTimestamp,
            'src_path': os.path.join(root, filename)
        })

        spin()

imgs.sort(key=lambda item: (item['timestamp'], item['file_name']))

print "Moving images for video creation..."
i = 0
for img in imgs:
    img['dest_path'] = "./G%07d.JPG" % i
    os.rename(img['src_path'], img['dest_path'])

    i += 1

    spin()


# http://thompsonng.blogspot.ro/2013/10/ffmpeg-creating-timelapse-with-ffmpeg.html
print "Creating video..."
call(["ffmpeg", "-f", "image2", "-r", "24", "-start_number", "0000001", "-i", "G%07d.JPG", "-r", "15", "-s", "hd720",
      "-vcodec", "libx264", "timelapse.mp4"], shell=True)

print "Moving images back..."
i = 0
for img in imgs:
    os.rename(img['dest_path'], img['src_path'])

    spin()

