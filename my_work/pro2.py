from PIL import Image
 
filename = "zzz.jpg"
with Image.open(filename) as image:
    width, height = image.size
    print (width, height)

#this fucking prints the size of the image
