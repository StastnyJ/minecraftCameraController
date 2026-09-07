import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import time
from visualize_hand import draw_landmarks_on_image


cam = cv2.VideoCapture('/dev/video33', cv2.CAP_V4L2)


model_path = '/home/stastnyj/Dev/minecraftControll/hand_landmarker.task'


BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode


base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    min_hand_detection_confidence=0.2,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5,
    num_hands=2
)


with HandLandmarker.create_from_options(options) as landmarker:
  # The landmarker is initialized. Use it here.
  # ...

    while True:
        ret, frame = cam.read()
        result = landmarker.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=frame))
        # Display the captured frame
        cv2.imshow('Camera', cv2.flip(draw_landmarks_on_image(frame, result), 1))

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    
