import cv2

cam = cv2.VideoCapture('/dev/video33', cv2.CAP_V4L2)



while True:
    ret, frame = cam.read()
    print(frame.shape)

    cv2.imwrite('test.png', frame)
    

    # # Display the captured frame
    cv2.imshow('Camera', frame)

    # # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()