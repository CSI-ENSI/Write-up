#!/usr/bin/python
#
#	@author Med Amine Ben Asker (twitter) @asker_amine
#	                            github.com/yurilaaziz
#
#		:: This how I made the Misc300 "BombZip" task 
#		 

from PIL import Image

im = Image.open("flag.jpg")
(width,height) = im.size

for x in range(width) :
	for y in range(height):
		single = Image.new("RGB", (1, 1), im.getpixel((x,y)))
		name = "("+ str(x) + "," + str(y) + ")"
		name = name.encode("base64")
		single.save("misc300/"+ name + ".jpg")
