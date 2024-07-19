import cv2
from ultralytics import YOLO
import time
#from cam import getFrame
#import torch

# Load a model
model = YOLO(r'best.pt')

capture = cv2.VideoCapture(0)

def getFrame():
    ret = False
    while ret == False:
      ret, frame = capture.read()
    return frame

def getResultAI():
  img = getFrame();
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

if __name__ == "__main__":
    while True:
        label = getResultAI()
        print(label)
        time.sleep(0.5)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
#print(getResultAI())