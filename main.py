import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import time
from visualize_hand import draw_landmarks_on_image


# set up camera
cam = cv2.VideoCapture('/dev/video33', cv2.CAP_V4L2)

# setup gesture recognizer model
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

gesture_recognizer_modelpath = '/home/stastnyj/Dev/minecraftControll/gesture_recognizer.task'
gesture_recognizer_base_options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=gesture_recognizer_modelpath),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=2
)

# with HandLandmarker.create_from_options(hand_landmarker_options) as landmarker:
with GestureRecognizer.create_from_options(gesture_recognizer_base_options) as recognizer:

    while True:
        ret, frame = cam.read()

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        recogn = recognizer.recognize(mp_image)
        print(recogn.gestures[0].category_name if len(recogn.gestures) > 0 else "No gesture detected")

        

        cv2.imshow('Camera', cv2.flip(draw_landmarks_on_image(frame, recogn), 1))