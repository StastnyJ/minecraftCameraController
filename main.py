import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import time
from visualize_hand import draw_landmarks_on_image
from detect_action import Gesture_Manager
# import keyboard
import random as rd
from add_crosshairs_to_camera import add_crosshairs_to_camera

# set up camera
cam = cv2.VideoCapture('/dev/video1', cv2.CAP_V4L2)

# setup gesture recognizer model
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


# gesture_recognizer_modelpath = '/home/michael/Documents/GitHub/KSP-MFF-CUNI/jednorázové/k-scuk-26/minecraftCameraController/gesture_recognizer.task'
gesture_recognizer_modelpath = '/home/stastnyj/Dev/minecraftControll/gesture_recognizer.task'
gesture_recognizer_base_options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=gesture_recognizer_modelpath),
    running_mode=VisionRunningMode.IMAGE,
    min_hand_detection_confidence=0.05,
    min_hand_presence_confidence=0.05,
    min_tracking_confidence=0.05,
    num_hands=2
)

# with HandLandmarker.create_from_options(hand_landmarker_options) as landmarker:
with GestureRecognizer.create_from_options(gesture_recognizer_base_options) as recognizer:
    gm = Gesture_Manager()
    while True:
        ret, frame = cam.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        recognized_gestures = recognizer.recognize(mp_image)
        # if recognized_gestures.gestures:
        #     category_name = recognized_gestures.gestures[0][0].category_name
        #     if category_name == "Closed_Fist":
        #         keyboard.press('q')
        if (len(recognized_gestures.gestures)) == 2:
            Gesture_Manager().detect_action(recognized_gestures)
        # if recognized_gestures.hand_landmarks:
        #     x = recognized_gestures.hand_landmarks[0][0].x
        #     y = recognized_gestures.hand_landmarks[0][0].y
        # print(recognized_gestures.gestures[0][3] if len(recognized_gestures.gestures[0]) > 3 else "No gesture detected")

        

        cv2.imshow('Camera', cv2.flip(draw_landmarks_on_image(add_crosshairs_to_camera(frame), recognized_gestures), 1))