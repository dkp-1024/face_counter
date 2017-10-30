from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image,ImageTk
import os
import cv2
import matplotlib.pyplot as plt

latest=''
last=''
fileopened=''
lastfile=''
undo='yes'

class Window(Frame):

    def __init__(self,master='none'):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title('Mini_Project 2017')
        self.pack(fill=BOTH,expand=1)
        menu=Menu(self.master)
        self.master.config(menu=menu)

        file=Menu(menu)
        file.add_command(label='New File',command=self.client_newfile)
        file.add_command(label='Save',command=self.client_save)
        file.add_command(label='Delete',command=self.client_del)
        file.add_command(label='Exit',command=self.client_exit)
        menu.add_cascade(label='File',menu=file)

        edit=Menu(menu)
        edit.add_command(label='Undo',command=self.client_undo)
        edit.add_command(label='Redo',command=self.client_redo)
        menu.add_cascade(label='Edit',menu=edit)

        op=Menu(menu)
        op.add_command(label='Rotate',command=self.client_rotate)
        op.add_command(label='Crop I quadrant',command=self.client_cropI)
        op.add_command(label='Crop II quadrant',command=self.client_cropII)
        op.add_command(label='Crop III quadrant',command=self.client_cropIII)
        op.add_command(label='Crop IV quadrant',command=self.client_cropIV)
        op.add_command(label='Overlap two images',command=self.client_overlap)
        op.add_command(label='Image Transpose',command=self.client_transpose)
        op.add_command(label='Create Thumbnail',command=self.client_thumbnail)
        op.add_command(label='Face Detection',command=self.client_face)
        menu.add_cascade(label='Operations',menu=op)

        dev=Menu(menu)
        dev.add_command(label='Amit Kumar Singh',command=self.client_dev)
        dev.add_command(label='Anshul Varshney',command=self.client_dev)
        dev.add_command(label='Deepak Kumar Pathak',command=self.client_dev)
        menu.add_cascade(label='Developed By',menu=dev)

        hlp=Menu(menu)
        hlp.add_command(label='About Project',command=self.client_abt)
        menu.add_cascade(label='Help',menu=hlp)

    def client_exit(self):
        exit()

    def client_face(self):
        imagepath = fileopened
        cascPath = "haarcascade_frontalface_default.xml"

        faceCascade = cv2.CascadeClassifier(cascPath)

        image = cv2.imread(imagepath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (30, 30)
        )

        print("Found {0} faces!".format(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        plt.imshow(image, cmap = 'gray')
        plt.show()
        # cv2.waitKey(1)



    def client_newfile(self):
        load=Image.open('capture1.png')
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        load=Image.open('capture1.png')
        load=load.resize((300,300),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render)
        img.image=render
        img.place(x=100,y=200)
        load=Image.open('capture1.png')
        load=load.resize((300,300),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render)
        img.image=render
        img.place(x=500,y=200)
        filename=askopenfilename()
        global fileopened
        global lastfile
        lastfile=fileopened
        fileopened=filename
        load=Image.open(filename)
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        global latest
        global last
        last=latest
        latest='open_new'

    def client_dev(self):
        load=Image.open('capture1.png')
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        load=Image.open('Amit.jpg')
        load=load.resize((300,300),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render)
        img.image=render
        img.place(x=100,y=200)
        load=Image.open('Anshul1.jpg')
        load=load.resize((300,300),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render)
        img.image=render
        img.place(x=500,y=200)
        global latest
        global last
        last=latest
        latest='dev'

    def client_del(self):
        try:
            load=Image.open('capture1.png')
            load=load.resize((550,550),Image.ANTIALIAS)
            render=ImageTk.PhotoImage(load)
            img=Label(self,image=render,anchor=CENTER)
            img.image=render
            img.place(x=400,y=70)
            global fileopened
            global lastfile
            os.remove(fileopened)
            fileopened=''
            lastfile=''
        except Exception as e:
            print('Some error')

    def client_undo(self):
        global lastfile
        global fileopened
        load=Image.open(lastfile)
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        x=lastfile
        lastfile=fileopened
        fileopened=x
        undo='no'

    def client_redo(self):
        if undo=='yes':
            global lastfile
            global fileopened
            load=Image.open(lastfile)
            load=load.resize((550,550),Image.ANTIALIAS)
            render=ImageTk.PhotoImage(load)
            img=Label(self,image=render,anchor=CENTER)
            img.image=render
            img.place(x=400,y=70)
            x=lastfile
            lastfile=fileopened
            fileopened=x

    def client_abt(self):
        global latest
        if latest=='dev':
            load=Image.open('capture1.png')
            load=load.resize((300,300),Image.ANTIALIAS)
            render=ImageTk.PhotoImage(load)
            img=Label(self,image=render)
            img.image=render
            img.place(x=100,y=200)
            load=Image.open('capture1.png')
            load=load.resize((300,300),Image.ANTIALIAS)
            render=ImageTk.PhotoImage(load)
            img=Label(self,image=render)
            img.image=render
            img.place(x=500,y=200)
        else:
            load=Image.open('capture1.png')
            load=load.resize((550,550),Image.ANTIALIAS)
            render=ImageTk.PhotoImage(load)
            img=Label(self,image=render,anchor=CENTER)
            img.image=render
            img.place(x=400,y=70)
        load=Image.open('about_project.jpg')
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        global last
        last=latest
        latest='abt'

    def client_rotate(self):
        global fileopened
        global lastfile
        img=Image.open(fileopened)
        rotated_small = img.rotate(90, resample=Image.BICUBIC, expand=True)
        save_path='C:/Users/HP/Desktop/Mini_Project/1.jpg'
        rotated_small.save(save_path)
        load=Image.open('capture1.png')
        load=load.resize((700,500),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=300,y=100)
        load=Image.open('1.jpg')
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        lastfile=fileopened
        fileopened=save_path
        global latest
        global last
        last=latest
        latest='rotate'

    def client_save(self):
        global fileopened
        x=asksaveasfilename()
        z=x.split('/')
        x=z[-1]
        y='C:/Users/HP/Desktop/Mini_Project/Saved Images/'+x+'.jpg'
        img=Image.open(fileopened)
        rotated_small = img.rotate(360, resample=Image.BICUBIC, expand=True)
        rotated_small.save(y)
        load=Image.open(y)
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        fileopened=y

    def client_cropI(self):
        global fileopened
        global lastfile
        img=Image.open(fileopened)
        width,height=img.size
        area=(width/2,0,width,height/2)
        img=img.crop(area)
        img.save('C:/Users/HP/Desktop/Mini_Project/2.jpg')
        load=Image.open('C:/Users/HP/Desktop/Mini_Project/2.jpg')
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        lastfile=fileopened
        fileopened='C:/Users/HP/Desktop/Mini_Project/2.jpg'
        global latest
        global last
        last=latest
        latest='crop1'

    def client_cropII(self):
        global fileopened
        global lastfile
        img=Image.open(fileopened)
        width,height=img.size
        area=(0,0,width/2,height/2)
        img=img.crop(area)
        img.save('C:/Users/HP/Desktop/Mini_Project/2.jpg')
        load=Image.open('C:/Users/HP/Desktop/Mini_Project/2.jpg')
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        lastfile=fileopened
        fileopened='C:/Users/HP/Desktop/Mini_Project/2.jpg'
        global last
        global latest
        last=latest
        latest='crop2'

    def client_cropIII(self):
        global fileopened
        global lastfile
        img=Image.open(fileopened)
        width,height=img.size
        area=(0,height/2,width/2,height)
        img=img.crop(area)
        img.save('C:/Users/HP/Desktop/Mini_Project/2.jpg')
        load=Image.open('C:/Users/HP/Desktop/Mini_Project/2.jpg')
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        lastfile=fileopened
        fileopened='C:/Users/HP/Desktop/Mini_Project/2.jpg'
        global latest
        global last
        last=latest
        latest='crop3'

    def client_cropIV(self):
        global fileopened
        global lastfile
        img=Image.open(fileopened)
        width,height=img.size
        area=(width/2,height/2,width,height)
        img=img.crop(area)
        img.save('C:/Users/HP/Desktop/Mini_Project/2.jpg')
        load=Image.open('C:/Users/HP/Desktop/Mini_Project/2.jpg')
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        lastfile=fileopened
        fileopened='C:/Users/HP/Desktop/Mini_Project/2.jpg'
        global last
        global latest
        last=latest
        latest='crop4'

    def client_overlap(self):
        img=Image.open(askopenfilename())
        img1=Image.open(askopenfilename())
        width,height=img.size
        width1,height1=img1.size
        img=img.resize((550,550),Image.ANTIALIAS)
        img1=img1.resize((550,550),Image.ANTIALIAS)
        img.paste(img1,(275,0))
        img.save('C:/Users/HP/Desktop/Mini_Project/3.jpg')
        x='C:/Users/HP/Desktop/Mini_Project/3.jpg'
        load=Image.open(x)
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        global fileopened
        global lastfile
        lastfile=fileopened
        fileopened='C:/Users/HP/Desktop/Mini_Project/3.jpg'
        global last
        global latest
        last=latest
        latest='overlap'

    def client_transpose(self):
        global fileopened
        global lastfile
        img=Image.open(fileopened)
        transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
        transposed_img.save('C:/Users/HP/Desktop/Mini_Project/4.jpg')
        load=Image.open('C:/Users/HP/Desktop/Mini_Project/4.jpg')
        load=load.resize((550,550),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render,anchor=CENTER)
        img.image=render
        img.place(x=400,y=70)
        lastfile=fileopened
        fileopened='C:/Users/HP/Desktop/Mini_Project/4.jpg'
        global last
        global latest
        last=latest
        latest='trasnpose'

    def client_thumbnail(self):
        global fileopened
        img=Image.open(fileopened)
        img.thumbnail((200,200))
        x=asksaveasfilename()
        a=x.split('/')
        y=a[-1]
        x='C:/Users/HP/Desktop/Mini_Project/Saved Images/'+y+'.jpg'
        img.save(x)

def main():
    root = Tk()
    root.geometry('1350x670+0+0')
    app=Window(root)
    root.mainloop()

if __name__=="__main__":
    main()
