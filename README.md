# Timelapse
Create a timelapse from GoPro timelapse folders using ffmpeg

Install ffmpeg
```
sudo brew install ffmpeg
```

Get the python script. Clone, download, copy/paste, etc.

For better use you can make it executable:
```
sudo chmod 775 /path/to/timelapse.py
```

Go to the folder where you have the partitioned images in subfolders. It should look like this:

```
cool-timelapse/
  105GOPRO/
    G0017253.JPG
    G0017254.JPG
    G0017255.JPG
    ...
  106GOPRO/
    G0018252.JPG
    G0018253.JPG
    G0018254.JPG
    ...
  ...
```

You should be in folder cool-timelapse.

Run the script:
```
timelapse.py
```

or (if you did not make it executable)

```
python timelapse.py
```

------

P.S. The script will move all the images from the subfolders to the root folder (cool-timelapse), create the video then move them back. The images will also be sorted by timestamp and by name after that for chronology.
