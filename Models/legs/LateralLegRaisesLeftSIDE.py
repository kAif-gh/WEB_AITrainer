import mediapipe as mp
from Models.improvedCode.ThreadedCamera import ThreadedCamera
from Models.improvedCode.Exercise import Exercise
import cv2
from Models.improvedCode import utils as u


def LateralLegRaisesLeftSIDE(camera):
    counter=0
    stage=None

    while True:
        frame = camera.get_frame()
        # the process you will do on the video (on each frame of the video)
        # frame_processed = detect_mask_in_frame(frame)
        try:
            # create new landmarks for the back position
            # x, y = u.createLandmark(img, True, 12, 11)

            # calculate angle function version alpha
            # the left side
            angle=u.findAngle(frame, 11, 23, 25, True, 110, 180, 20, angleError1=100, angleError2=150)
            # caculating the distance between two legs with landmarks : (28,27)
            distance=u.Distance(frame, 28, 27)
            # Counter logic
            # Distance check
            if 180 > angle > 160:
                if distance > 10:
                    stage="down"
            if 110 < angle < 130 and stage == 'down':
                if distance > 10:
                    stage="up"
                    counter+=1
                    print(counter)
        except:
            pass

        u.affich(frame, "Lateral Leg Raises", counter, stage)
        frame_processed = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_processed + b'\r\n')



#
# mp_drawing=mp.solutions.drawing_utils
# mp_pose=mp.solutions.pose
# pose=mp_pose.Pose()
#
# class LateralLegRaiseLS(Exercise):
#     def __init__(self):
#         pass
#
#     def exercise(self, source):
#         threaded_camera = ThreadedCamera(source)
#         # Curl counter variables
#         counter=0
#         stage=None
#         ## Setup mediapipe instance
#         with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
#             while threaded_camera.capture.isOpened():
#                 ret, img = threaded_camera.show_frame()
#                 if not ret or img is None:
#                     continue
#                 # test of the findPose function
#                 img, results=u.findPose(img, False)
#                 # image.flags.writeable = True
#                 # Extract landmarks
#                 try:
#                     # create new landmarks for the back position
#                     # x, y = u.createLandmark(img, True, 12, 11)
#
#                     # calculate angle function version alpha
#                     # the left side
#                     angle=u.findAngle(img, 11, 23, 25, True, 120, 175, 20)
#                     # caculating the distance between two legs with landmarks : (28,27)
#                     distance = u.Distance(img,28,27)
#                     # print (distance)
#                     # Counter logic
#                     # Distance check
#                     if 175 > angle > 160:
#                         if distance > 10:
#                             stage="down"
#                     if 110 < angle < 130 and stage == 'down':
#                         if distance > 10:
#                             stage="up"
#                             counter+=1
#                             print(counter)
#                 except:
#                     pass
#
#                 u.affich(img, "Lateral Leg Raises", counter, stage)
#
#                 cv2.imshow('Mediapipe Feed', img)
#
#                 if cv2.waitKey(10) & 0xFF == ord('q'):
#                     break
#             pose.close()
#
