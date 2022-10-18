
import cv2
from Models.improvedCode import utils as u


def Deadlift(camera):
    counter=0
    stage=None

    while True:
        frame = camera.get_frame()
        _, results=u.findPose(frame, False)
        # Extract landmarks
        lmlist=u.get_idx_to_coordinates(frame, results)

        try:
            # create new landmarks for the back position
            # x, y = u.createLandmark(img, True, 12, 11)

            # right arm must be 180°
            cv2.line(frame, (lmlist[12]), (lmlist[14]), thickness=4,
                     color=(255, 255, 255))
            cv2.line(frame, (lmlist[14]), (lmlist[16]), thickness=4,
                     color=(255, 255, 255))
            # left arm must be 180°
            cv2.line(frame, (lmlist[11]), (lmlist[13]), thickness=4,
                     color=(255, 255, 255))
            cv2.line(frame, (lmlist[13]), (lmlist[15]), thickness=4,
                     color=(255, 255, 255))

            # calculate angle function version alpha
            angle=u.findAngle(frame, 24, 26, 28, True, 100, 180, 30, angleError1=80, angleError2=120)
            angle2=u.findAngle(frame, 23, 25, 27, True, 100, 180, 30, angleError1=80, angleError2=120)

            # counter logic
            if 180 > angle > 150:
                stage="up"
            if 100 < angle < 130 and stage == "up":
                stage="down"
                counter+=1
                print(counter)
        except:
            pass

        u.affich(frame, "Deadlift", counter, stage)
        frame_processed = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_processed + b'\r\n')



