import cv2
from deepface import DeepFace
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 0, 255), 1)
        try:
            analyze = DeepFace.analyze(frame, actions=['emotion'])
            emotion = analyze['dominant_emotion']
            cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        except:
            print("no face")
        
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
