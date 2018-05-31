import cv2
from PIL import Image
import numpy
import matplotlib.pyplot as plt

def crop():
	try:
		#Relative Path
		img = Image.open("new.jpg")
		# width, height = img.size
		area = (x, y, w, h)
		img = img.crop(area)
		# cv2.imshow("wait what???", img)
		# cv2.waitKey(0)
		img.save("result.jpg") 
         
	except IOError:
		print ("what the hell is this")

def main():
	# Get user supplied values
	imagepath = "ex.png"
	cascPath = "haarcascade_frontalface_default.xml"

	faceCascade = cv2.CascadeClassifier(cascPath)

	# Read the image
	image = cv2.imread(imagepath)
	backtorgb = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
	gray = cv2.cvtColor(backtorgb, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
	    backtorgb,
	    scaleFactor=1.3,
	    minNeighbors=5,
	    minSize=(30, 30)
	)

	print("Found {0} faces!".format(len(faces)))

	for (x, y, w, h) in faces:
	    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	
	plt.imshow(image, cmap='gray')
	plt.show()
	# crop()

if __name__ == "__main__":
    main()
