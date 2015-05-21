from sys import exit
from PIL import Image
	
def blue_galaxy():
	print "Voila, this place called as Blue Galaxy."
	img = Image.open('C:/Users/Macroice Deviance/Desktop/Galaxy Game/01 Blue Galaxy.jpg')
	img.show()
	
def red_galaxy():
	print "Come in, little boy welcome."
	img = Image.open('C:/Users/Macroice Deviance/Desktop/Galaxy Game/02 Red Galaxy.jpg')
	img.show()
	
def dead(why):
	print why, "Good Job!"
	exit(0)
	
def start():
	print "Welcome Boy"
	print "Here, you have two chooses."
	print "1. Blue Galaxy"
	print "2. Red Galaxy\n\n\n"
	print "Where do you want to go"
	
	next = raw_input("> ")
	
	if next == "1":
		blue_galaxy()
	elif next == "2":
		red_galaxy()
	else:
		dead("Here, there is no other galaxy to live in.")	

		
start()