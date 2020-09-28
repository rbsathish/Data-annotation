For xml to yolo you need to specify the classes first in xml_to_yolo.py:

for eg:
	lut["with_mask"] =0
	lut["without_mask"]       =1
	lut["mask_weared_incorrect"]    =2
eg 2:	
	# lut["bag"]       =1
	# lut["shoes"]     =2

run the xml_to_yolo.py in xml files folder.
