
import cv2
from Models.improvedCode import utils as u


def BentOverRow(camera):
    counter=0
    stage=None

    while True:
        frame = camera.get_frame()


        try:

            # calculate angle function version alpha
            angle=u.findAngle(frame, 12, 14, 16, True, 70, 180, 20, angleError1=80, angleError2=120)
            angle2=u.findAngle(frame, 11, 13, 15, True, 70, 180, 20, angleError1=80, angleError2=120)

            # Curl counter logic
            if 180 > angle > 160:
                stage="down"
            if 70 < angle < 110 and stage == 'down':
                stage="up"
                counter+=1
                print(counter)

        except:
            pass
        u.affich(frame, "Bent Over Row", counter, stage)
        frame_processed = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_processed + b'\r\n')


