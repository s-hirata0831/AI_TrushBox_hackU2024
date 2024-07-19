# import cv2
# capture = cv2.VideoCapture(0)
# def getFrame():
#   ret = False
#   while not ret:
#     ret, frame = capture.read()
#     cv2.imshow("test", frame)
#   return frame

# while(True):
#   frame = getFrame()

import cv2

capture = cv2.VideoCapture(0)

def getFrame():
    ret = False
    while ret == False:
      ret, frame = capture.read()
    return frame

if __name__ == "__main__":
  while True:
      frame = getFrame()
      cv2.imshow("test", frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q'キーを押すとループを抜ける
          break

  capture.release()
  cv2.destroyAllWindows()
