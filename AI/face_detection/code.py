import cv2
from random import randrange

# prebuilt data
trained_face_data = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")


# get video from webcam
webcam = cv2.VideoCapture(0)
# this is for the video for existing video
# video = cv2.VideoCapture('./video.mp4')

# iterate for realtime frames:
while True:
    successful_frame_read, frame = webcam.read()
    # successful_frame_read, frame = video.read()
    grayscaled_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_video)

    for x, y, w, h in face_coordinates:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (randrange(128, 256), randrange(128, 256), randrange(128, 256)),
            2,
        )

    cv2.imshow("Face Detection App", frame)
    # cv2.waitKey(1)  # 1 milliseconds - realtime, and go to the next frame, if no value then only stay in a frame and you can press any key to change the frame

    # for quitting
    if cv2.waitKey(10) == ord("x"):
        break
# for disabling the webcam
webcam.release()
# for disabling the video
# video.release()

print("Code run with 0 errors")
