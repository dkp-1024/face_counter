#this will create a thumbnail
from PIL import Image
def main():
    try:
        #Relative Path
        img = Image.open("zzz.jpg") 
         
        #In-place modification
        img.thumbnail((200, 200)) 
         
        img.save("thumb.jpg")
    except IOError:
        pass
 
if __name__ == "__main__":
    main()