#this will fucking rotate the image
from PIL import Image
 
def main():
    try:
        #Relative Path
        img = Image.open("zzz.jpg") 
         
        #Angle given
        img = img.rotate(180) 
         
         #Saved in the same relative location
        img.save("rotated_picture.jpg")
    except IOError:
        print "something went wrong"
 
if __name__ == "__main__":
    main()
