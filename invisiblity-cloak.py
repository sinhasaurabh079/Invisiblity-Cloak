import cv2  # for image processing
import numpy as np  # numerical library for handling the image

cap = cv2.VideoCapture(0)  # to access webcam

# path
#path = r'/home/saurabh/vs-code/Python/Invisility-Cloak/image.jpg'
background = cv2.imread('./image.jpg')

while cap.isOpened():
    # capture the live frame
    ret, current_frame = cap.read()
    if ret:
        # instead of using rgb value we use hsv(hue,saturation,value)
        # ex- a whole red cloth will not be detected as red as some part of it will be treated differently due to shadows
        # converting from rgb tohsv color space
        hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        # range for lower red
        l_red = np.array([0, 120, 70])
        u_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv_frame, l_red, u_red)

        # range for upper red
        l_red = np.array([170, 120, 70])
        u_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv_frame, l_red, u_red)

        # for blue color cloak
        # low_blue1=np.array([90,103,20])
        # high_blue1=np.array([119,255,255])
        # mask1=cv2.inRange(hsv_frame,low_blue1,high_blue1)

        # low_blue2=np.array([180,98,20])
        # high_blue2=np.array([170,255,255])
        # mask2=cv2.inRange(hsv_frame,low_blue2,high_blue2)

        # generating the final red mask
        red_mask = mask1+mask2

        # the below 2 lines
        red_mask = cv2.morphologyEx(
            red_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=10)
        red_mask = cv2.morphologyEx(
            red_mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

        # subsituting the red portion with backgroung image
        part1 = cv2.bitwise_and(background, background, mask=red_mask)

        # detecting the thing that are not red
        red_free = cv2.bitwise_not(red_mask)

        # if cloak is not present show the current image
        part2 = cv2.bitwise_and(current_frame, current_frame, mask=red_free)

        # final output
        cv2.imshow("cloak", part1+part2)  # here it is capturing background
        # for every 5ms it will refresh image and after pressing q it will click image
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
