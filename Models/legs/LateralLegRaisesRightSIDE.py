
import cv2
from Models.improvedCode import utils as u




def LateralLegRaisesRightSIDE(camera):
    counter=0
    stage=None

    while True:
        frame = camera.get_frame()
        try:
            # create new landmarks for the back position
            # x, y = u.createLandmark(img, True, 12, 11)

            # calculate angle function version alpha
            # the left side
            angle=u.findAngle(frame, 12, 24, 26, True, 110, 180, 20, angleError1=100, angleError2=150)
            # caculating the distance between two legs with landmarks : (28,27)
            distance=u.Distance(frame, 28, 27)
            # print (distance)
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


