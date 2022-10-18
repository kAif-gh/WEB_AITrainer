
import cv2
from Models.improvedCode import utils as u



def SingleLegGlute(camera):
    counter=0
    stage=None

    while True:
        frame = camera.get_frame()
        _, results =u.findPose(frame, False)
        # Extract landmarks
        lmlist=u.get_idx_to_coordinates(frame, results)
        try:
            # create new landmarks for the back position
            # x, y = u.createLandmark(img, True, 12, 11)

            if 12 in lmlist and 24 in lmlist and 26 in lmlist and 28 in lmlist:  # left side of body
                angle=u.findAngle(frame, 12, 24, 26, True, 120, 180, 20, angleError1=100, angleError2=140)
                angle2=u.fixedAngle(frame, 24, 26, 28)
                # counter logic
                if 170 < angle2 < 180:
                    if 180 > angle > 160:
                        stage="up"
                    if 120 < angle < 140 and stage == "up":
                        stage="down"
                        counter+=1
                        print(counter)
                cv2.line(frame, (lmlist[28]), (lmlist[32]), thickness=4,
                         color=(255, 255, 255))
                cv2.line(frame, (lmlist[32]), (lmlist[30]), thickness=4,
                         color=(255, 255, 255))
                cv2.line(frame, (lmlist[30]), (lmlist[28]), thickness=4,
                         color=(255, 255, 255))

            elif 11 in lmlist and 23 in lmlist and 25 in lmlist and 27 in lmlist:  # right side of body
                angle=u.findAngle(frame, 11, 23, 25, True, 120, 180, 20, angleError1=100, angleError2=140)
                angle2=u.fixedAngle(frame, 23, 25, 27)
                # counter logic
                if 170 < angle2 < 180:
                    if 180 > angle > 160:
                        stage="up"
                    if 120 < angle < 140 and stage == "up":
                        stage="down"
                        counter+=1
                        print(counter)
                cv2.line(frame, (lmlist[27]), (lmlist[29]), thickness=4,
                         color=(255, 255, 255))
                cv2.line(frame, (lmlist[29]), (lmlist[31]), thickness=4,
                         color=(255, 255, 255))
                cv2.line(frame, (lmlist[31]), (lmlist[27]), thickness=4,
                         color=(255, 255, 255))

        except:
            pass

        u.affich(frame, "Single Leg Glute", counter, stage)
        frame_processed = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_processed + b'\r\n')


