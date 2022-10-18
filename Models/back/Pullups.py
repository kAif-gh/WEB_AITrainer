
import cv2
from Models.improvedCode import utils as u

def Pullups(camera):
    counter=0
    stage=None

    while True:
        frame = camera.get_frame()

        try:
            # calculate angle function version alpha
            angle=u.findAngle(frame, 12, 14, 16, True, 20, 180, 30, angleError1=80, angleError2=120)
            angle2=u.findAngle(frame, 11, 13, 15, True, 20, 180, 30, angleError1=80, angleError2=120)
            # Counter logic
            if 175 > angle > 160:
                stage="up"
            if 40 < angle < 70 and stage == 'up':
                stage="down"
                counter+=1
                print(counter)

        except:
            pass
        u.affich(frame, "Pull-Ups", counter, stage)
        frame_processed = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_processed + b'\r\n')

