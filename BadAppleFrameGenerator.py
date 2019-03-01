# Code to extract every 5th frame from the original Bad Apple video

import cv2
vidcap = cv2.VideoCapture('BadApple.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 5