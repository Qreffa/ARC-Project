import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


webcam = cv2.VideoCapture(0)
cv2.waitKey(1)

while True:
    successful_frame_read,frame = webcam.read()

    #img = cv2.imread('/Users/efegonen/Desktop/Kodlama/Python/lesson.py/Photo on 3-22-21 at 11.15 PM.jpeg',1)

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cordinates = trained_face_data.detectMultiScale(grayscaled_img)


    for (x, y, w, h) in face_cordinates:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0,0, 255), 5)

    cv2.imshow('Face detect', frame)
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break

webcam.release
"""









cv2.imshow('Face detect', img)
cv2.waitKey(0)

"""

print("Code Completed")