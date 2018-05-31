print "done"

import numpy as np
print "one passes"
from PIL import Image 
print "one passes"
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import os

print "now we are in the program"
cascadePath = "haarcascade_frontalface_default.xml" 
faceCascade = cv2.CascadeClassifier(cascadePath);
print "so far so good."
