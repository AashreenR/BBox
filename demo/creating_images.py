import cv2
import numpy as np
import json
import os
import glob





folder_path="/Users/aashreenraorane/Desktop/BBox/demo/Sanskrit/arya/" #insert path of the folder containing images


bbx_name= "tesserocr-arya.bbx" #insert name of bbx file present in folder_path

bbx_path=folder_path+bbx_name
file = open(bbx_path, 'r') #insert full path of the bbx file of folder
data_in = json.load(file)
file.close()



for i in data_in["images"].keys():
	img_path=folder_path+i
	thresh1= cv2.imread(img_path,0)
	# ret,thresh1 = cv2.threshold(im,127,255,cv2.THRESH_BINARY)
	height, width = thresh1.shape[:2]
	f=1
	img_name= i[:-4]
	new_path=folder_path + img_name
	if(os.path.isdir(new_path)):
		files = glob.glob(new_path, recursive=True)

		for file in files:
			try:
				os.remove(file)
			except OSError as e:
				print()
	else:
		os.mkdir(new_path)
	for annot in data_in["images"][i]["annotations"]:
		xmin=int(annot['bbox']["xmin"]*width)
		xmax=int(annot['bbox']["xmax"]*width)
		ymin=int(annot['bbox']["ymin"]*height)
		ymax=int(annot['bbox']["ymax"]*height)
		new_name = folder_path + img_name + "/" + img_name +"_" + str(f)
		if (xmax-xmin>22): #to ignore small boxes like pg. nos
			cv2.imwrite(new_name+".jpg",thresh1[ymin:ymax,xmin:xmax])
			f=f+1










		










