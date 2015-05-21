from sys import exit
import time
import psutil
from PIL import Image
	
def blue_galaxy():
	print "Voila, this place called as Blue Galaxy."
	img = Image.open('C:/Users/Macroice Deviance/Desktop/Galaxy Game/01 Blue Galaxy.jpg')
	img.show()
	
	
	time.sleep(5)
	
	for proc in psutil.process_iter():
		if proc.name == "display":
			proc.kill()
	
	print "Here, you can ride the wind to travel stars.\n\n"
	time.sleep(1)
	print "There 2 regions in stars as East and West."
	print "West is cold. East is hot."
	print "Do you wanna see the stars?\n\n"
	next = raw_input("> ")
	if next == "yes":
		print "Here you have!"
		img = Image.open('C:/Users/Macroice Deviance/Desktop/Galaxy Game/03 Blue Stars.jpeg')
		img.show()
		print "Now do you wanna go to Red Galaxy?"
		nextie = raw_input("> ")
		if nextie == "yes":
			print "Then hold on tight!"
			red_galaxy()
		else:
			dead("Okay, as you wish..")
	else:
		dead("No stars for you..")
	
def red_galaxy():
	print "Come in, little boy welcome."
	img = Image.open('C:/Users/Macroice Deviance/Desktop/Galaxy Game/02 Red Galaxy.jpg')
	img.show()
	
	print "Here, you can use explosions to reach other planets.\n\n"
	print "There 2 areas in planets as North and South"
	print "North is bright. South is dark"
	print "Do you wanna see the planets?"
	next = raw_input("> ")
	if next == "yes":
		print "Right in front of you."
		img = Image.open('C:/Users/Macroice Deviance/Desktop/Galaxy Game/04 Red Planets.jpg')
		img.show()
	else:
		dead("No planets for you..")
		
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