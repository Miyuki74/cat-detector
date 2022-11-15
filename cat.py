import cv2
import requests
import time
# 
# # load the required trained XML classifiers 
# # https://github.com/Itseez/opencv/blob/master/ 
# # data/haarcascades/haarcascade_frontalcatface.xml 
# # Trained XML classifiers describes some features of some 
# # object we want to detect a cascade function is trained 
# # from a lot of positive(faces) and negative(non-faces) 
# # images. 
face_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.7/dist-packages/cv2/data/haarcascade_frontalcatface.xml') 
# 
# 
# # capture frames from a camera 
cap = cv2.VideoCapture(0) 
# 
# # loop runs if capturing has been initialized. 
while 1: 
 
     # reads frames from a camera
     ret, img = cap.read()
     img = cv2.rotate(img, cv2.ROTATE_180)
     # convert to gray scale of each frames 
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     # Detects faces of different sizes in the input image
     faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

     for (x,y,w,h) in faces: 
         # To draw a rectangle in a face 
         cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
         roi_gray = gray[y:y+h, x:x+w] 
         roi_color = img[y:y+h, x:x+w]
         
         time.sleep(1)
         
         cv2.imwrite('cat_data/FileName.jpg', img)
         print("----Captured!----")
          
         payload = {'message': 'Meow!'}                  # 送信メッセージ
         url = 'https://notify-api.line.me/api/notify'
         token = "Z6vJLdRx9666joaoVakxD0FG6VIOxMzDTweYfGepwqS"
         headers = {'Authorization': 'Bearer ' + token}
         files={"imageFile":open('cat_data/FileName.jpg',"rb")}
         res = requests.post(url, data=payload, headers=headers,files=files,)  # LINE NotifyへPOST
         print(res)  #検出画像出力
         time.sleep(30)
         break
 
     # Display an image in a window
     cv2.imshow('img',img) 
 
     # Wait for Esc key to stop
     k = cv2.waitKey(30) & 0xff
     if k == 27: 
         break

　# Close the window
 cap.release() 
 
 #De-allocate any associated memory usage
 cv2.destroyAllWindows() 

