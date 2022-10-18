
import cv2
from Models.improvedCode import utils as u

def RomanionSquats(camera):
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
            cv2.line(frame, (lmlist[24]), (lmlist[23]), thickness=4,
                     color=(255, 255, 255))
            cv2.line(frame, (lmlist[28]), (lmlist[32]), thickness=4,
                     color=(255, 255, 255))
            cv2.line(frame, (lmlist[32]), (lmlist[30]), thickness=4,
                     color=(255, 255, 255))
            cv2.line(frame, (lmlist[30]), (lmlist[28]), thickness=4,
                     color=(255, 255, 255))
            cv2.line(frame, (lmlist[27]), (lmlist[29]), thickness=4,
                     color=(255, 255, 255))
            cv2.line(frame, (lmlist[29]), (lmlist[31]), thickness=4,
                     color=(255, 255, 255))
            cv2.line(frame, (lmlist[31]), (lmlist[27]), thickness=4,
                     color=(255, 255, 255))
            # calculate angle function version alpha
            angle=u.findAngle(frame, 24, 26, 28, True, 30, 180, 30, angleError1=80, angleError2=120)
            angle2=u.findAngle(frame, 23, 25, 27, True, 30, 180, 30, angleError1=80, angleError2=120)

            # Counter logic
            if 180 > angle > 150:
                stage="up"
            if 30 < angle < 60 and stage == "up":
                stage="down"
                counter+=1
                print(counter)
        except:
            pass

        u.affich(frame, "Romanion Squats", counter, stage)
        frame_processed = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_processed + b'\r\n')
