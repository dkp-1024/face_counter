#this will fucking crop the image by the width and height given 
from PIL import Image
 
def main():
    try:
        #Relative Path
        img = Image.open("zzz.jpg")
        width, height = img.size
         
        area = (0, 0, width/2, height/2)
        img = img.crop(area)
         
        #Saved in the same relative location
        img.save("fuckoff.jpg") 
         
    except IOError:
        print "what the fuck is this"
 
if __name__ == "__main__":
    main()