
import time
import cv2
from Models.improvedCode import utils as u



def Plank(camera):
        eang1=0
        plankTimer=None
        plankDuration=0
        while True:

            frame=camera.get_frame()
            _, results=u.findPose(frame, False)
            # Extract landmarks
            idx_to_coordinates=u.get_idx_to_coordinates(frame, results)
            # t = u.CountDown(10)
            try:
                # shoulder - back - ankle
                if 11 in idx_to_coordinates and 23 in idx_to_coordinates and 27 in idx_to_coordinates:  # left side of body

                    eang1=u.angle((idx_to_coordinates[11], idx_to_coordinates[23]),
                                  (idx_to_coordinates[23], idx_to_coordinates[27]))
                    cv2.putText(frame, str(round(eang1, 2)),
                                (idx_to_coordinates[23][0]-40, idx_to_coordinates[23][1]-50),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.8, color=(0, 255, 0), thickness=3)
                    if 160 < eang1 < 180:
                        cv2.line(frame, (idx_to_coordinates[11]), (idx_to_coordinates[23]), thickness=3,
                                 color=(0, 255, 0))
                        cv2.line(frame, (idx_to_coordinates[23]), (idx_to_coordinates[27]), thickness=3,
                                 color=(0, 255, 0))
                        cv2.circle(frame, (idx_to_coordinates[11]), 5, (0, 255, 0), cv2.FILLED)
                        cv2.circle(frame, (idx_to_coordinates[11]), 15, (0, 255, 0), 2)
                        cv2.circle(frame, (idx_to_coordinates[23]), 5, (0, 255, 0), cv2.FILLED)
                        cv2.circle(frame, (idx_to_coordinates[23]), 15, (0, 255, 0), 2)
                        cv2.circle(frame, (idx_to_coordinates[27]), 5, (0, 255, 0), cv2.FILLED)
                        cv2.circle(frame, (idx_to_coordinates[27]), 15, (0, 255, 0), 2)
                        cv2.putText(frame, "Valid, continue!", (390, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2,
                                    cv2.LINE_AA)
                    elif eang1 < 160:
                        cv2.line(frame, (idx_to_coordinates[11]), (idx_to_coordinates[23]), thickness=3,
                                 color=(0, 0, 255))
                        cv2.line(frame, (idx_to_coordinates[23]), (idx_to_coordinates[27]), thickness=3,
                                 color=(0, 0, 255))
                        cv2.circle(frame, (idx_to_coordinates[11]), 5, (0, 0, 255), cv2.FILLED)
                        cv2.circle(frame, (idx_to_coordinates[11]), 15, (0, 0, 255), 2)
                        cv2.circle(frame, (idx_to_coordinates[23]), 5, (0, 0, 255), cv2.FILLED)
                        cv2.circle(frame, (idx_to_coordinates[23]), 15, (0, 0, 255), 2)
                        cv2.circle(frame, (idx_to_coordinates[27]), 5, (0, 0, 255), cv2.FILLED)
                        cv2.circle(frame, (idx_to_coordinates[27]), 15, (0, 0, 255), 2)
                        cv2.putText(frame, "Correct your form", (340, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                                    2,
                                    cv2.LINE_AA)

            except:
                pass

            try:

                if 160 < eang1 < 180:
                    if plankTimer == None:
                        plankTimer=time.time()
                    plankDuration+=time.time()-plankTimer
                    plankTimer=time.time()
                else:
                    plankTimer=None


            except:
                pass
            if 0 in idx_to_coordinates:
                cv2.putText(frame, "Plank Timer : "+str(round(plankDuration))+" sec",
                            (idx_to_coordinates[0][0]-60, idx_to_coordinates[0][1]-240),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=0.9, color=(0, 255, 0), thickness=4)
            # u.affich(frame, "plank", counter, stage)
            frame_processed=cv2.imencode('.jpg', frame)[1].tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n'+frame_processed+b'\r\n')


