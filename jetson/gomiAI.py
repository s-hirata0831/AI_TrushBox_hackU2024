import cv2
from ultralytics import YOLO
from cam import getFrame
#import torch

# Load a model
model = YOLO(r'jetson/best.pt')

def getResultAI():
  img = getFrame();
  cv2.imshow("123", img)
  result =  model.predict(source=img,
                conf=0.50,
                project="mypredict", # 出力先
                name="mypredict.jpg", #フォルダ名
                exist_ok=True, #上書きOKか
                save=True,
                max_det=1)

  for single_result in result:
    if len(single_result.boxes) > 0:
      result_label_num = single_result.boxes.cls.item()
      if(result_label_num == 0):
        result_label = 'CAN'
      else:
        result_label = 'PET'
    else:
      result_label = None

  return result_label

print(getResultAI())