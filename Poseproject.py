import cv2 
import mediapipe as mp 
import time 
import Posemodule as Pm
 
 
cap = cv2.VideoCapture('V3.mp4')
ptime = 0
detector = Pm.posedetector()
while True :
 success,img = cap.read()
 img = detector.findPose(img)
         #Lmlist = detector.findPosition(img)
 Lmlist = detector.findPosition(img,draw =False)
 if len(Lmlist) != 0:
   print(Lmlist[20])
   cv2.circle(img,(Lmlist[20][1],Lmlist[20][2]),14,(0,0,255),cv2.FILLED)
 ctime = time.time()
 fps = 1/(ctime - ptime)
 ptime = ctime

 cv2.putText(img,str(int(fps)),(20,20),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
 cv2.imshow("Image",img)

 cv2.waitKey(1)