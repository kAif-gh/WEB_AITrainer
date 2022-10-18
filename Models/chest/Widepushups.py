
import cv2
from Models.improvedCode import utils as u
import numpy as np


def WidePushups(camera):
    counter=0
    stage=None

    while True:
        frame = camera.get_frame()
        _, results=u.findPose(frame, False)
        # Extract landmarks
        lmlist=u.get_idx_to_coordinates(frame, results)
        try:
            # shoulder - ankle - wrist
            if 12 in lmlist and 28 in lmlist and 16 in lmlist:  # left side of body
                cv2.line(frame, (lmlist[12]), (lmlist[28]), thickness=4,
                         color=(255, 255, 255))
                cv2.line(frame, (lmlist[28]), (lmlist[16]), thickness=4,
                         color=(255, 255, 255))
                np.linspace(lmlist[12], lmlist[28], 100)
                np.linspace(lmlist[28], lmlist[16], 100)
            else:  # right side of body
                cv2.line(frame, (lmlist[11]), (lmlist[27]), thickness=4,
                         color=(255, 255, 255))
                cv2.line(frame, (lmlist[27]), (lmlist[15]), thickness=4,
                         color=(255, 255, 255))
                np.linspace(lmlist[11], lmlist[27], 100)
                np.linspace(lmlist[27], lmlist[15], 100)

        except:
            pass

        try:
            angle=u.findAngle(frame, 12, 14, 16, True, 90, 180, 30, angleError1=100, angleError2=120)
            angle2=u.findAngle(frame, 11, 13, 15, True, 90, 180, 30, angleError1=100, angleError2=120)
            # Counter logic
            if 180 > angle > 150:
                stage="up"
            if 90 < angle < 120 and stage == 'up':
                stage="down"
                counter+=1
                print(counter, stage)

        except:
            pass

        u.affich(frame, "Wide Push-Ups", counter, stage)
        frame_processed = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_processed + b'\r\n')

