#!/usr/bin/python
#
#	@author Med Amine Ben Asker (twitter) @asker_amine
#	                            github.com/yurilaaziz
#
#		:: solution the Misc300 "BombZip" task 
#

from PIL import Image
import os
import base64

(width,height) = (236, 285)
output ="result.jpg"
path = "misc300/"

result = Image.new("RGB", (width,height) )
img = result.load()
listdir = os.listdir(path)

print "[+] Misc folder      : %s " % path
print "[+] Building image   : %s " % output
print "----------------------------------------------"
for image in listdir :
	namedecoded = image.replace('\n.jpg','')
	
	# fixing the b64 invalid padding 
	if image[-1] != '=':
		namedecoded = namedecoded + "="

	name = base64.b64decode(namedecoded)

	name = name.replace(")", '')
	name = name.replace("(", '')
	(x,y) = map(int,name.split(','))
	
	im = Image.open(path + image)
	px = im.load()
	print "[+] Pixel (%d,%d) : SET RGB %s " %(x, y, px[0,0])
	img[x,y] = px[0,0]

result.save(output)
