#converting image to bitmap
def main():
    try:
        #Relative Path
        img = Image.open("picture.jpg") 
        print img.mode
         
        #converting image to bitmap
        print img.tobitmap()
         
        print type(img.tobitmap())
    except IOError:
        pass
 
if __name__ == "__main__":
    main()