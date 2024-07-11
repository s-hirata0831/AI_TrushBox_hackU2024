import cv2
capture = cv2.VideoCapture(0)
def getFrame():
  ret = False
  while not ret:
    ret, frame = capture.read()
  return frame