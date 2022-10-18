
import cv2
from Models.improvedCode import utils as u

def Dips(camera):
    counter=0
    stage=None

    while True:
        frame = camera.get_frame()
        _, results =u.findPose(frame, False)
        lmlist=u.get_idx_to_coordinates(frame, results)

        try:
            if 12 in lmlist and 14 in lmlist and 16 in lmlist:  # left side of body
                # calculate angle function version alpha
                angle=u.findAngle(frame, 12, 14, 16, True, 50, 180, 30, angleError1=80, angleError2=120)
                # Curl counter logic

                if 40 < angle < 50:
                    stage="down"
                if 180 > angle > 150 and stage == 'down':
                    stage="up"
                    counter+=1
                    print(counter, stage)

            else:  # right side of body
                # calculate angle function version alpha
                angle2=u.findAngle(frame, 11, 13, 15, True, 40, 180, 30, angleError1=80, angleError2=120)
                # Curl counter logic

                if 40 < angle2 < 50:
                    stage="down"
                if 180 > angle2 > 150 and stage == 'down':
                    stage="up"
                    counter+=1
                    print(counter, stage)

        except:
            pass
        u.affich(frame, "Dips", counter, stage)
        frame_processed = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_processed + b'\r\n')

