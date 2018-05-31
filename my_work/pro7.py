#transposing the image
from PIL import Image
 
def main():
    try:
        #Relative Path
        img = Image.open("image.png") 
         
        #transposing image 
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
         
        #Save transposed image
        transposed_img.save("transposed.jpg")
    except IOError:
        pass
 
if __name__ == "__main__":
    main()