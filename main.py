import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller
import time

detector  = HandDetector(detectionCon = 0.8, maxHands=1)
keyboard = Controller()

video = cv2.VideoCapture(0)
time.sleep(0.5)
while(True):
    ret , frame=video.read()
    hands,img = detector.findHands(frame)

    if(hands):
        lmlist = hands[0]
        hand_side = lmlist['type']
        fingureUp = detector.fingersUp(lmlist)
        print(fingureUp)
        if(fingureUp == [0,1,0,0,0]):
            keyboard.press(Key.right)
        elif(fingureUp == [1,0,0,0,0] or fingureUp == [1,1,0,0,0]):
            keyboard.press(Key.left)

        else:
            keyboard.release(Key.left)
            keyboard.release(Key.right)    

    cv2.imshow("Frame",frame)
    k = cv2.waitKey(1)
    if(k==ord('q')):
        break

video.release()
cv2.destroyAllWindows()
