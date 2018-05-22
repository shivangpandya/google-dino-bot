from PIL import Imagegrab,ImageOps
import pyautogui
from numpy import *

class Cordinates:
	replayBtn = (340,390). #coordinates here
	dinosour = (171,95) # Coord of dino front
	#240 = x coordinante to check for the tree
	# y coordinate =420

def restartGame():
	pyautogui.click(Cordinates.replayBtn)

def pressSpace():
	pyautogui.keyDown('space')
	time.sleep(0.05)
	print("Jump")
	pyautogui.keyUp('space')

def  Imagegrab():
	box = (Cordinates.dinosour[0] + 100,Cordinates.dinosour[1]+30)
	image = Imagegrab.grab(box)
	grayImage = ImageOps.grayscale(image)
	a = array(grayImage.getcolors)
	print a.sum()

def main:
	restartGame()
	while True:
		if(Imagegrab() == 1447)
		pressSpace()
		time.sleep(0.1)

restartGame()
time.sleep(1)
pressSpace()