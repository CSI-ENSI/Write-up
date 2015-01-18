#!/usr/bin/python
#
#	@author Med Amine Ben Asker (twitter) @asker_amine
#	                            github.com/yurilaaziz
#
#		:: solution the Misc400 "Tree" task 
#
import os 

path = "misc/"
result = ""

folders = [i for i in os.listdir(path) if os.path.isdir(path+i)]
while folders != [] :
	folder1 = folders[ 0 ]
	folder2 = folders[ 1 ]
	if [] == [i for i in os.listdir(path + folder1) if os.path.isdir(path + folder1 + "/" + i)]:
		(folder1, folder2) = (folder2, folder1) 

	result += str(folder2) + str(folder1)
	path   += folder1 + "/"
	folders = [i for i in os.listdir(path) if os.path.isdir(path + i)]

print "Hidden Text : %s " %result
