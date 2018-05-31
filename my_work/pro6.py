#pasting of the image on another image
from PIL import Image
 
def main():
    try:
        #Relative Path
        #Image on which we want to paste
        img = Image.open("picture.jpg") 
         
        #Relative Path
        #Image which we want to paste
        img2 = Image.open("picture2.jpg") 
        img.paste(img2, (50, 50))
         
        #Saved in the same relative location
        img.save("pasted_picture.jpg")
         
    except IOError:
        pass
 
if __name__ == "__main__":
    main()
 
##An additional argument for an optional image mask image is also available.
