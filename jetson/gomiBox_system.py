from time import sleep, time

from playMp3 import playMp3 as p
from gomiAI import getResultAI as ai
from servo import openPetCover as oPET, openCanCover as oCAN, closePetCover as cPET, closeCanCover as cCAN
from irSignal import readIR, resultIsCAN, setOpenSignalPin, readResetNumSw

def getUp():
  p('WindowsXP.mp3')
  cCAN()
  cPET()
  print("GOMI BOX GET UP NOW")

def waitGomi():
  result = ai()
  while(result == None):
    result = ai()
  p('WAON.mp3')
  return result

def setCanPinOutput(result):
  if(result == 'CAN'):
    resultIsCAN(True)
  else:
    resultIsCAN(False)

def openCover(result):
  if(result == 'CAN'):
    oCAN()
  else:
    oPET()
  setOpenSignalPin(True)

def waitSignal():
  start_time = time()
  while(readIR() == False):
    now_time = time()
    wait_time = now_time - start_time
    if(wait_time > 30.0):
      return False
  p('PayPay.mp3')
  return True

def countCANandPET(result):
  if(result == 'CAN'):
    can_cnt += 1
  else:
    pet_cnt += 1

def closeCover():
  cCAN()
  cPET()
  setOpenSignalPin(False)

def pushedResetNumButton():
  return readResetNumSw()

def cntCondition():
  if(can_cnt < max_can_cnt and pet_cnt < max_pet_cnt):
    return 0
  elif(can_cnt == max_can_cnt and pet_cnt < max_pet_cnt):
    return 1
  elif(can_cnt < max_can_cnt and pet_cnt == max_pet_cnt):
    return 2
  else:
    return 3

def main(cnt_condition):
  all_ok = 0
  can_full = 1
  pet_full = 2
  all_full = 3

  if(cnt_condition != all_full):
    result = waitGomi()
    if((cnt_condition == all_ok) or (cnt_condition == can_full and result != 'CAN') or (cnt_condition == pet_full and result != 'PET')):
      setCanPinOutput(result)
      openCover(result)
      if(waitSignal()):
        countCANandPET(result)
        sleep(2)
      closeCover()

#------------------------------main--------------------------
can_cnt = 0
pet_cnt = 0
max_can_cnt = 14
max_pet_cnt = 14

getUp()
while(True):
  if(pushedResetNumButton()):
    can_cnt = 0
    pet_cnt = 0
    p('error.mp3')
  else:
    main(cntCondition())
    sleep(5)
