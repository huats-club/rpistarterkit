import os
from PIL import Image

#file = os.path.realpath('ball.png')
#print("File Directory is {}".format(file))
#file = 'C:\Users\YWFU\Documents\GitHub\EGL314starterkit\"Tutorial Sample"\ball.png'
#file = 'C:/Users/YWFU/Documents/GitHub/EGL314starterkit/Tutorial Sample/ball.png'
#file = 'ball.png'
#myImage = Image.open(file)
#myImage.show()


""" path = str(os.path.realpath('ball.png'))
file = path.replace('\\','/')
print("Path is {}".format(file))
#myImage = Image.open(file)
#myImage.show() """

#dir_path = os.path.dirname(os.path.realpath('ball.png'))
path = os.path.abspath('images') + '\\' + 'ball.png'
file = path.replace('\\', '/')
print("File path is {}".format(file))
myImage = Image.open(file)
myImage.show()