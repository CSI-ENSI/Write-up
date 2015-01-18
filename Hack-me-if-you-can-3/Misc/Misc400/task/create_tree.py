#! /usr/bin/python
import os 

text ="Can You s3e what I s3e. Can you read what I write. Can you understand what I mean. Yes maybe. {Flag:one_way_binary_tree}"
flag = text.replace(" ","_")
flag = flag.replace(".","+")
tree ="misc"
os.mkdir(tree)
count = 0
for car in flag :
	count = count + 1
	os.mkdir(tree +"/"+ car)
	if count % 2 == 0:
		tree = tree + "/" + car