
import json as JS 
import xml.etree.cElementTree as e
import os

cwd = os.getcwd()

l= r"D:\off\final_data\json"
cwd_xml 	= cwd + "\\" + "xml\\"
for filename in os.listdir(l):
    
    file = os.path.join(l,filename)
    
    with open(file, "r") as json_file: 
        print(filename)
        print(filename[:-5])
        # loading json file data 
        # to variable data 
        data = JS.load(json_file)
        # print(data)
        # print(json2xml(data))
        r = e.Element("root")
        # e.SubElement(r,"folder").text = d["f  older"]
        e.SubElement(r,"FileName").text = data[ "FileName"]
        # e.SubElement(r,"NumOfAnno").text = str(data["NumOfAnno"])
        # e.SubElement(r,"Annotations").text = str(data["Annotations"])
        
        ann = e.SubElement(r,"object")
        for z in data["Annotations"]:
            e.SubElement(ann,"name").text = z["classname"]
            # e.SubElement(ann,"Confidence").text = "Confidence"
            # e.SubElement(ann,"xmin").text =str( z["BoundingBox"][0])
            bbox = e.SubElement(ann,"bndbox")
            for b in data["Annotations"]:
                print(b)
                e.SubElement(bbox,"xmin").text =str( b["BoundingBox"][0])
                e.SubElement(bbox,"ymin").text =str( b["BoundingBox"][1])
                e.SubElement(bbox,"xmax").text =str( b["BoundingBox"][2])
                e.SubElement(bbox,"ymax").text =str( b["BoundingBox"][3])
        a = e.ElementTree(r)
        f = filename[:-5]
        f = f + ".xml"
        f = cwd_xml + '\\' + f
        a.write(f)