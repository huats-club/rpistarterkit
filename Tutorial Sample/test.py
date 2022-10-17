import os
from PIL import Image

#file = os.path.realpath('ball.png')
#print("File Directory is {}".format(file))
#file = 'C:\Users\YWFU\Documents\GitHub\EGL314starterkit\"Tutorial Sample"\ball.png'
file = 'C:/Users/YWFU/Documents/GitHub/EGL314starterkit/Tutorial Sample/ball.png'
#file = 'ball.png'
myImage = Image.open(file)
myImage.show()