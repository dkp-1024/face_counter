#img = Image.open(path) 
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)
from PIL import Image

try: 
	img = "zzz.jpg"
 
	with Image.open(img) as image:
	    width, height = image.size
	print "successfully read"
except IOError:
	print "something went wrong"
# Use the above statement within try block, as it can 
# raise an IOError if file cannot be found, 
# or image cannot be opened.

