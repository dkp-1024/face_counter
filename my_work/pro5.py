#resizing the fucking image
from PIL import Image
 
def main():
    try:
         #Relative Path
        img = Image.open("zzz.jpg")
        width, height = img.size
  
        img = img.resize((width/2, height/2))
         
        #Saved in the same relative location
        img.save("resized_picture.jpg") 
    except IOError:
        print ("error")
 
if __name__ == "__main__":
    main()
