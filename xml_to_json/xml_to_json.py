
import os
import json 
import xmltodict 
def resizer_fun(location):
    l =location
    # w = w
    # h = h
    # print(w,h)
    for filename in os.listdir(l):
        
        file = os.path.join(l,filename)
        
        with open(file) as xml_file: 
        
            data_dict = xmltodict.parse(xml_file.read()) 
            xml_file.close() 
        json_data = json.dumps(data_dict) 
    	# Write the json data to output 
        # json file 
        n = filename + ".json"
        with open(n, "w") as json_file: 
            json_file.write(json_data) 
            json_file.close() 
	
        # print(img)
    # for root, directories, files in os.walk(l, topdown=False):
    #     # for name in files:
    #     print(root)
            # path = os.path.join(root, name)
        # rez = cv2.resize(img,(w,h),interpolation=cv2.INTER_AREA)
        # #writing the resized image
        # n = filename + ".jpg"
        # cv2.imwrite(filename,rez) 
        #loading the resized image and seeing the height & width
        # resized = cv2.imread("resized_image.jpg")  
        # (height,width) = resized.shape[:2]
        # print ("Resized Height & Width  ---> \n Height : {} Width : {}".format(height,width))
    
