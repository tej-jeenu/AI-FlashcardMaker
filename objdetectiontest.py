from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import os
import cv2
import numpy
import openai
import csv
import time
openai.api_key = //your open api key here


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


def converttoq(specpoint:str):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user", "content": "can you turn '" + specpoint + "' into a question that can be used for a flashcard"}]
    )
    return str(completion.choices[0].message.content)

# Simple image to string
#print(pytesseract.image_to_string(Image.open('2.png')))


#model = YOLO("yolov8s.pt")
model = YOLO("newspecextract.pt")
#model.train(data="coco128.yaml", epochs=100, imgsz=640)

firstpage = int(input("What is the first page to start scanning: "))
lastpage = int(input("what is the last page you wanna start scanning: "))
images = convert_from_path('compsci.PDF')

data = []
for j in range(lastpage):
      # Save pages as images in the pdf
    if(j >= firstpage - 1):
       images[j].save('page'+ str(j) +'.png', 'PNG')
       results = model.predict(source='page'+ str(j) +'.png', show=False)
       img = cv2.imread('page'+ str(j) +'.png')
       for result in results:
          boxes = result.boxes.cpu().numpy()
          for i, box in enumerate(boxes):
            r = box.xyxy[0].astype(int)
            crop = img[r[1]:r[3], r[0]:r[2]]
            cv2.imwrite(str(i) + ".png", crop)
            speccontent = str(pytesseract.image_to_string(Image.open(str(i) + ".png")))
        
            rawqlist = speccontent.split(".")
            qlist = []

            for spec in rawqlist:
               spec = spec.replace("\n\n","\n")
               #use the converttoq() method here for the q
               q = spec #converttoq(spec)
               q = q.replace('"','') #usually q qould be here
               print(q)
               qlist.append(q.strip())#replace q with the actual rephrased spec point as a q
               #time.sleep(60)

            qlist.remove(qlist[len(qlist)-1])
        
            os.remove(str(i) + ".png")
        
            for q in qlist:
               data.append([q, 'Enter answer here'])
       os.remove('page'+ str(j) +'.png')

with open('specpoints.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    f.close()
    

'''
q = converttoq(str(pytesseract.image_to_string(Image.open("2.png"))))
print(q)
https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/ for doing PDF conversion
'''
