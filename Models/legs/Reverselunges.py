
import cv2
from Models.improvedCode import utils as u


def ReverseLungs(camera):
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
            # calculate angle function version alpha
            if 28 in lmlist and 24 in lmlist and 26 in lmlist:
                angle=u.findAngle(frame, 24, 26, 28, True, 70, 175, 30)
                draw=True
                angle2=u.findAngle(frame, 23, 25, 27, draw, 70, 175, 30)
                # if angle2 < 175:
                #     draw=True
                #     angle2=u.findAngle(img, 23, 25, 27, draw, 70, 175, 30)
                # Curl counter logic
                if 180 > angle > 150:
                    stage="up"
                if 70 < angle < 100 and stage == "up":
                    stage="down"
                    counter+=1
                    print(counter)
            elif 27 in lmlist and 23 in lmlist and 25 in lmlist:
                angle2=u.findAngle(frame, 24, 26, 28, True, 70, 175, 30, angleError1=80, angleError2=120)
                angle=u.findAngle(frame, 23, 25, 27, True, 70, 175, 30, angleError1=80, angleError2=120)
                # Counter logic
                if 180 > angle > 150:
                    stage="up"
                if 70 < angle < 100 and stage == "up":
                    stage="down"
                    counter+=1
                    print(counter)
        except:
            pass

        u.affich(frame, "Reverse Lunges", counter, stage)
        frame_processed=cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n'+frame_processed+b'\r\n')

