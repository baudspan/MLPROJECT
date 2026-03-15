import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

videocapture=cv2.VideoCapture(0)

print('-'*50)
print('face detection started')
print('position your face in front of camera')
print('press \'q\' to quit')
print('-'*50)

while True:
    ret,frame=videocapture.read()
    if not ret:
        print("faliled to capture frame")
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('face detection-press "q" to exit',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("\n exiting...")
        break
videocapture.release()
cv2.destroyAllWindows()
print("camera released.see you soon cutiee!!")