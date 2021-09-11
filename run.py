import cv2
import numpy as np
import sys
import os
from tqdm import tqdm

dir = "Thumbnail"
# If thumbnail folder doesn't exist, create it
if not os.path.exists(dir):
    os.makedirs(dir)

filename = str(sys.argv[1])
# filename = "Giga - '劣等上等'(BRING IT ON) ft.鏡音リン・レン【MV】-oEkGC2HV7rc.mp4"
resolution = 240
framerate = 5
x = 10
y = 10

filen = filename[0:filename.rindex('.')]
vidcap = cv2.VideoCapture(filename)

totalFrame = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = vidcap.get(cv2.CAP_PROP_FPS)
# print(totalFrame)
# print(fps)
# print(totalFrame / fps)
# print(totalFrame / fps / 5)

def captureFrame(vidcap, mil):
  vidcap.set(cv2.CAP_PROP_POS_MSEC, mil)
  _, image = vidcap.read()
  return image

def printTime(src,dst,img,x,y,width,height,count,f):
    # print("\n{:02d}:{:02d}:{:02d}.{:03d} --> {:02d}:{:02d}:{:02d}.{:03d}".format(
    #     int(src/1000/60/60),
    #     int((src/1000/60)%60),
    #     int((src/1000)%60),
    #     int(src%1000),
    #     int(dst/1000/60/60),
    #     int((dst/1000/60)%60),
    #     int((dst/1000)%60),
    #     int(dst%1000)
    # ))
    # print("{}#xywh={},{},{},{}".format(img,count%x*width,int(count/x)*height,width,height))

    f.write("\n\n{:02d}:{:02d}:{:02d}.{:03d} --> {:02d}:{:02d}:{:02d}.{:03d}".format(
        int(src/1000/60/60),
        int((src/1000/60)%60),
        int((src/1000)%60),
        int(src%1000),
        int(dst/1000/60/60),
        int((dst/1000/60)%60),
        int((dst/1000)%60),
        int(dst%1000)
    ))
    f.write("\n{}#xywh={},{},{},{}".format(img,count%x*width,int(count/x)*height,width,height))

def createThumbnails(vidcap, resolution = 240, framerate = 1, x = 5, y = 5):

  scale = resolution / vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
  width = int(scale * vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(scale * vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
  dim = (width,height)

  count = 0
  count_im = 0
  sec = 0
  mil = 0 

  im_h = []
  im_v = []

  f = open("{}/{}.vtt".format(dir,filen), "w")
  f.write("WEBVTT")

  trigger = False

  for i in tqdm(range(int(totalFrame / fps / framerate))):

    mil = sec * 1000

    # Get image and resize
    image = captureFrame(vidcap, mil)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    printTime(
      mil,
      mil+framerate*1000,
      "{}_{}.jpg".format(filen, count_im+1),
      x, y, width, height, count, f)

    # Add image to array
    im_h.append(image)

    # Add time
    count = count + 1
    sec = sec + framerate

    # If 1 row finished
    if (count != 0 and count % x == 0):
      image = cv2.hconcat(im_h)
      im_v.append(image)
      im_h.clear()

      # If 1 image finished
      if (count / x == y):
        count = 0
        count_im = count_im + 1
        cv2.imwrite("{}/{}_{}.jpg".format(dir,filen, count_im),cv2.vconcat(im_v))
        im_v.clear()

  # If not round
  if (sec < totalFrame / fps):
    mil = sec * 1000

    # Get image and resize
    image = captureFrame(vidcap, mil)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    printTime(
      mil,
      totalFrame/fps*1000,
      "{}_{}.jpg".format(filen, count_im+1),
      x, y, width, height, count, f)

    # Add image to array
    im_h.append(image)

    # Add time
    count = count + 1
    sec = sec + framerate

    # If 1 row finished
    if (count != 0 and count % x == 0):
      image = cv2.hconcat(im_h)
      im_v.append(image)
      im_h.clear()

      # If 1 image finished
      if (count / x == y):
        count = 0
        count_im = count_im + 1
        cv2.imwrite("{}/{}_{}.jpg".format(dir, filen, count_im),cv2.vconcat(im_v))
        im_v.clear()
  
  while (count % x != 0):
    trigger = True
    image = np.zeros([height, width, 3], np.uint8)
    im_h.append(image)
    count = count + 1

  if (trigger):
    image = cv2.hconcat(im_h)
    im_v.append(image)
    count_im = count_im + 1
    cv2.imwrite("{}/{}_{}.jpg".format(dir, filen, count_im),cv2.vconcat(im_v))
  elif (count == x):
    count_im = count_im + 1
    cv2.imwrite("{}/{}_{}.jpg".format(dir, filen, count_im),cv2.vconcat(im_v))

  f.close()

createThumbnails(vidcap, resolution, framerate, x, y)