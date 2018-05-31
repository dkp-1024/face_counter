#don't use this, this will fucking destroy the fucking image
from PIL import Image
 
def main():
    try:
        #Relative Path
        img = Image.open("image.png") 
         
        #splitting the image
        print img.split()
    except IOError:
        print "some error"
 
if __name__ == "__main__":
    main()