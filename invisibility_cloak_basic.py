import cv2
import numpy as np
import time

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
time.sleep(3)

background = 0
for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("LH", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("LS", "Trackbars", 120, 255, nothing)
cv2.createTrackbar("LV", "Trackbars", 70, 255, nothing)
cv2.createTrackbar("UH", "Trackbars", 10, 180, nothing)
cv2.createTrackbar("US", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("UV", "Trackbars", 255, 255, nothing)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "Trackbars")
    ls = cv2.getTrackbarPos("LS", "Trackbars")
    lv = cv2.getTrackbarPos("LV", "Trackbars")
    uh = cv2.getTrackbarPos("UH", "Trackbars")
    us = cv2.getTrackbarPos("US", "Trackbars")
    uv = cv2.getTrackbarPos("UV", "Trackbars")

    lower_bound = np.array([lh, ls, lv])
    upper_bound = np.array([uh, us, uv])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)
    mask_inv = cv2.bitwise_not(mask)

    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(img, img, mask=mask_inv)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisibility Cloak", final_output)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
