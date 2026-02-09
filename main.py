import cv2

fase_cap=cv2.CascadeClassifier("C:/Users/Acer/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_fullbody.xml")
v=cv2.VideoCapture(0)
while True:
    ret,vi=v.read()
    col=cv2.cvtColor(vi,cv2.COLOR_BGR2GRAY)
    faces=fase_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(vi,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("video_live",vi)
    if cv2.waitKey(10)==ord("a"):
        break
v.release()

