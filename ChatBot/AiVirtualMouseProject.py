import cv2                                              #computer vision library
import numpy as np                                      #(Numerical Python) for working with arrays and matrices
import HandTrackingModule as htm             
import time                                             #to handle time-related tasks
import autopy                                           #for controlling the keyboard and mouse

def virMouse():
    ##########################
    wCam, hCam = 640, 480
    frameR = 100                                            # Frame Reduction
    smoothening = 7
    ##########################

    pTime = 0                                               #initializing previous time to 0
    plocX, plocY = 0, 0                                     #initializing the previous location of X,Y
    clocX, clocY = 0, 0                                     #initializing the current location of X,Y

    # To capture a video, you need to create a VideoCapture object.
    cap = cv2.VideoCapture(0)                               #Function to Capture from the camera and display it.

    #to have a fixed width and height of the camera (propId for width:3 and height:4) {note: propIds Each number denotes a property of the video}
    cap.set(3, wCam)                                        #to set the width
    cap.set(4, hCam)                                        #to set the height

    detector = htm.handDetector(maxHands=1)                 #to get the landmarks(maxHands=1 bcoz we are expecting just one hand)
    wScr, hScr = autopy.screen.size()                       #give us the size of the screen
    # print(wScr, hScr)

    while True:

        # 1. Find hand Landmarks
        success, img = cap.read()                           # success = If the frame is read correctly, it will be True     #img = frame values
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)           #marks the points & fingers and a bounding box

        # 2. Get the tip of the index and middle fingers
        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]                          #to get the index finger
            x2, y2 = lmList[12][1:]                         #to get the middle finger
            # print(x1, y1, x2, y2)
            
            # 3. Check which fingers are up
            fingers = detector.fingersUp()                  #will return the array of 0 and 1 indicating which fingers and up and which are down
            # print(fingers)
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
            (255, 0, 255), 2)                               #the frame in which the mouse will be working
            # 4. Only Index Finger : Moving Mode
            if fingers[1] == 1 and fingers[2] == 0:         #index finger is up and middle finger is down
                # 5. Convert Coordinates
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                # 6. Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
            
                # 7. Move Mouse
                autopy.mouse.move(wScr - clocX, clocY)       #wScr - clocX : to  flip the direction
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)    # to draw a circle around the tip
                plocX, plocY = clocX, clocY
                
            # 8. Both Index and middle fingers are up : Clicking Mode
            if fingers[1] == 1 and fingers[2] == 1:          #index finger is up and middle finger is down
                # 9. Find distance between fingers
                length, img, lineInfo = detector.findDistance(8, 12, img)   #would return the distance between index finger and middle finger
                # print(length)
                # 10. Click mouse if distance short
                if length < 40:                              #if the distance between both fingers is less than 40
                    cv2.circle(img, (lineInfo[4], lineInfo[5]),
                    15, (0, 255, 0), cv2.FILLED)             #drawing a green circle to indicate click
                    autopy.mouse.click()                     #clicking the mouse
            
        # 11. Frame Rate
        cTime = time.time()                                  #to get the time in seconds since epoch
        fps = 1 / (cTime - pTime) +1                           #calculating framerate
        pTime = cTime                                        #assigining current time to previous time
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
        (255, 0, 0), 3)                                      #displaying the frame rate on the window

        # 12. Display
        cv2.imshow("Image", img)                             #display an image in a window                
        cv2.waitKey(1)                                       #waits for delay milliseconds

        # if stop():
        #         break
virMouse()