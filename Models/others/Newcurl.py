import cv2
from Models.improvedCode import utils as u



def Curl(camera):
    counter=0
    stage=None

    while True:

        frame=camera.get_frame()
        _, results=u.findPose(frame, False)
        # Extract landmarks
        lmlist=u.get_idx_to_coordinates(frame, results)

        try:
                    # calculate angle function version alpha
                    angle=u.findAngle(frame, 12, 14, 16, True, 40, 180, 30, angleError1=100, angleError2=120)
                    angle2=u.findAngle(frame, 11, 13, 15, True, 40, 180, 30, angleError1=100, angleError2=120)
                    # Curl counter logic
                    if 180 > angle > 160:
                        stage="down"
                    if 40 < angle < 70 and stage == 'down':
                        stage="up"
                        counter+=1
                        print(counter)

        except:
            pass
        u.affich(frame, "Dumbbell Curl", counter, stage)
        frame_processed = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
                      b'Content-Type: image/jpeg\r\n\r\n' + frame_processed + b'\r\n')

