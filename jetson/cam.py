import cv2
capture = cv2.VideoCapture(0)
def getFrame():
  # ret = False
  # while not ret:
  #   ret, frame = capture.read()
  # return frame

  ret, frame = capture.read()
  return frame

while(True):
  cv2.imshow('test', getFrame())