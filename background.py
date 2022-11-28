import cv2  # opencv for image processing

# creating a videocapture object
cap = cv2.VideoCapture(0)  # this is my webcam

# getting the background image
while cap.isOpened():
    ret, background = cap.read()  # siply reading from the web cam
    if ret:
        cv2.imshow("image", background)  # here it is capturing background
        # for every 5ms it will refresh image and after pressing q it will click image
        if cv2.waitKey(5) == ord('q'):
            # save the background image
            cv2.imwrite("image.jpg",background)
            break
cap.release()

cv2.destroyAllWindows()
