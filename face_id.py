import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyecascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.3,5)
    eyes= eyecascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    

    cv2.imshow('video', frame)

    k=cv2.waitKey(1) &0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
