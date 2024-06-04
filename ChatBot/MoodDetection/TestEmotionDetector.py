import time
import cv2
import numpy as np
from keras.models import model_from_json

sad = 0
happy = 0 
angry = 0
fearful = 0
surprised = 0
neutral = 0
init = time.time()
comment = ""
def moodDetect():
    
    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

    # load json and create modelpython_try\MoodDetection
    json_file = open('ChatBot/MoodDetection/model/emotion_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    emotion_model = model_from_json(loaded_model_json)

    # load weights into new model
    emotion_model.load_weights("ChatBot/MoodDetection/model/emotion_model.h5")
    print("Loaded model from disk")
 
    # start the webcam feed
    # cap = cv2.VideoCapture(0)

    # pass here your video path or on web cam using "0"
    # cap = cv2.VideoCapture("python_try/MoodDetection/video.mp4")
    cap = cv2.VideoCapture("ChatBot/MoodDetection/mood.mp4")

    while True:
        # Find haar cascade to draw bounding box around face
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720))
        if not ret:
            break
        face_detector = cv2.CascadeClassifier('ChatBot\MoodDetection\haarcascades\haarcascade_frontalface_default.xml')
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces available on camera
        num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        # take each face available on the camera and Preprocess it
        for (x, y, w, h) in num_faces:
            global sad, happy, angry, fearful, surprised, neutral
            global comment
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
            roi_gray_frame = gray_frame[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

            # predict the emotions
            emotion_prediction = emotion_model.predict(cropped_img)
            maxindex = int(np.argmax(emotion_prediction))
            cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            # print(emotion_dict[maxindex])

            if emotion_dict[maxindex] == "Sad":
                sad += 1
            elif emotion_dict[maxindex] == "Happy":
                happy += 1
            elif emotion_dict[maxindex] == "Angry":
                angry += 1
            elif emotion_dict[maxindex] == "Fearful":
                fearful += 1
            elif emotion_dict[maxindex] == "Surprised":
                surprised += 1
            elif emotion_dict[maxindex] == "Neutral":
                neutral += 1
            

        cv2.imshow('Emotion Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            

        if (time.time() - init) > (0.5 * 60) :
            if sad > 50:
                sad = 0
                comment="You look sad,...hum abhi joke marenge"
                print(comment)
                time.sleep(1)
                pass
            elif happy > 50:
                happy = 0
                comment="You look happy today,..."
                print(comment)
                time.sleep(1)
                pass
            elif angry > 50:
                angry = 0
                comment="You look angry today,..."
                print(comment)
                time.sleep(1)
                pass
            elif fearful > 50:
                fearful = 0
                comment="You look fearful today,..."
                print(comment)
                time.sleep(1)
                pass
            elif surprised > 50:
                surprised = 0
                comment="You must be surprised today,..."
                print(comment)
                time.sleep(1)
                pass
            elif neutral > 50:
                neutral = 0
                comment="You neutral today,..."
                print(comment)
                time.sleep(1)
                pass
            else:
                comment="Your behaviour is ok today"
                time.sleep(1)


        # if stop():
        #     cap.release()
        #     cv2.destroyAllWindows()
        #     break


# moodDetect()