import cv2
import mediapipe as mp
import numpy as np
import math as math

from mediapipe.python.solutions.drawing_utils import _normalized_to_pixel_coordinates

mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose
pose=mp_pose.Pose()


def findPose(img, draw=True):
    """
    :param img: frames of the video stream
    :param draw: initially True to indicate that drawing is authorized

    """
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        if draw:
            mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    return img, results


def findPosition(img, draw=True):
    """
    :param img: frames of the video stream
    :param draw: initially True to indicate that drawing is authorized
    :return lmList : list of the coordinates of each landmark detected
    """
    lmList=[]
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c=img.shape
            # print(id, lm)
            cx, cy=int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])
            if draw:
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    return lmList


# improved version of findPosition() function
def get_idx_to_coordinates(image, results, VISIBILITY_THRESHOLD=0.5, PRESENCE_THRESHOLD=0.5):
    """
    :param image:  frames of the video stream
    :param VISIBILITY_THRESHOLD: parameters given by mediapipe : to add more accuracy for detection
    :param PRESENCE_THRESHOLD: parameters given by mediapipe : to add more accuracy for detection
    """
    idx_to_coordinates={}
    image_rows, image_cols, _=image.shape
    try:
        for idx, landmark in enumerate(results.pose_landmarks.landmark):
            if ((landmark.HasField('visibility') and
                 landmark.visibility < VISIBILITY_THRESHOLD) or
                    (landmark.HasField('presence') and
                     landmark.presence < PRESENCE_THRESHOLD)):
                continue
            landmark_px=_normalized_to_pixel_coordinates(landmark.x, landmark.y,
                                                         image_cols, image_rows)
            if landmark_px:
                idx_to_coordinates[idx]=landmark_px
    except:
        pass
    return idx_to_coordinates

# another way to calculate angle with putting two lines of the angle as arguments

def dot(vA, vB):
    return vA[0] * vB[0]+vA[1] * vB[1]


def angle(lineA, lineB):
    # Get nicer vector form
    vA=[(lineA[0][0]-lineA[1][0]), (lineA[0][1]-lineA[1][1])]
    vB=[(lineB[0][0]-lineB[1][0]), (lineB[0][1]-lineB[1][1])]
    # Get dot prod
    dot_prod=dot(vA, vB)
    # Get magnitudes
    magA=dot(vA, vA) ** 0.5
    magB=dot(vB, vB) ** 0.5
    # Get cosine value
    cos_=dot_prod / magA / magB
    # Get angle in radians and then convert to degrees
    angle=math.acos(dot_prod / magB / magA)
    # Basically doing angle <- angle mod 360
    ang_deg=math.degrees(angle) % 360
    ang_deg=180-ang_deg

    if ang_deg-180 >= 0:
        # As in if statement
        return 360-ang_deg
    else:

        return ang_deg


# the beta version to mesure the angle
def calculate_angle(a, b, c):
    """

    :param a: the identity of a landmark1
    :param b: the identity of a landmark2
    :param c: the identity of a landmark3
    :return: angle of (a,b,c)
    """
    a=np.array(a)
    b=np.array(b)
    c=np.array(c)
    radians=np.arctan2(c[1]-b[1], c[0]-b[0])-np.arctan2(a[1]-b[1], a[0]-b[0])
    angle=np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle=360-angle
    return angle


# the alpha version to mesure the angle
def findAngle(img, p1, p2, p3, draw, min, max, diff,angleError1, angleError2):
    """

    :param img: frames of the video stream
    :param p1: the identity of a landmark1
    :param p2: the identity of a landmark2
    :param p3: the identity of a landmark3
    :param draw: True for indicate that drawing is authorized
    :param min: the minimal angle of the margin of validity
    :param max: the maximal angle of the margin of validity
    :param diff: difference that identify the margin of validity
    :param angleError1: the minimal angle of the margin of fault
    :param angleError2: the maximal angle of the margin of fault
    :return: angle processed
    """
    lmList=findPosition(img, False)
    _, x1, y1=lmList[p1]
    _, x2, y2=lmList[p2]
    _, x3, y3=lmList[p3]

    # calculate angle
    angle=abs(math.degrees(math.atan2(y3-y2, x3-x2)-math.atan2(y1-y2, x1-x2)))
    if angle > 180.0:
        angle=360-angle

    # from showing the angle only for testing
    # cv2.putText(img, str(int(angle)), (x2-50, y2+50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    if draw:

        if max-diff < angle < max:
            #(255, 0, 255) pink color
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.line(img, (x3, y3), (x2, y2), (0, 255, 0), 3)
            cv2.circle(img, (x1, y1), 5, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 255, 0), 2)
            cv2.circle(img, (x2, y2), 5, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 255, 0), 2)
            cv2.circle(img, (x3, y3), 5, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 255, 0), 2)
            cv2.putText(img, "Valid, continue!", (390, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2, cv2.LINE_AA)

        elif min+diff > angle > min:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.line(img, (x3, y3), (x2, y2), (0, 255, 0), 3)
            cv2.circle(img, (x1, y1), 5, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 255, 0), 2)
            cv2.circle(img, (x2, y2), 5, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 255, 0), 2)
            cv2.circle(img, (x3, y3), 5, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 255, 0), 2)
            cv2.putText(img, "Valid, continue!", (390, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2, cv2.LINE_AA)

        elif angle < min:
            cv2.putText(img, "Correct your form", (340, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (0, 0, 255), 3)
            cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
        elif min+diff < angle < angleError1:
            cv2.putText(img, "Correct your form", (340, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (0, 0, 255), 3)
            cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
        elif angleError2 < angle < max-diff:
            cv2.putText(img, "Correct your form", (340, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (0, 0, 255), 3)
            cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
        else:
            cv2.putText(img, "Valid, continue!", (390, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2, cv2.LINE_AA)
    return angle


# function that guarantee the 3 landmarks are (+-) fixed
# img, p1, p2, p3, draw, min, max, diff
def fixedAngle(img, p1, p2, p3):
    """
    :param img: frames of the video stream
    :param p1: the identity of a landmark1
    :param p2: the identity of a landmark2
    :param p3: the identity of a landmark3
    """
    lmList=findPosition(img, False)
    _, x1, y1=lmList[p1]
    _, x2, y2=lmList[p2]
    _, x3, y3=lmList[p3]
    angle=abs(math.degrees(math.atan2(y3-y2, x3-x2)-math.atan2(y1-y2, x1-x2)))
    if angle > 180.0:
        angle=360-angle
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
    cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
    return angle

#  function for description

def affich(img, name, counter, stage):
    """
    :param img: frames of video stream
    :param name: the identity of an exercise
    :param counter: counting how many sets
    :param stage: stage of the exercise either Down or Up
    """
    # render the name of the exercise

    cv2.putText(img, name, (10, 450),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    # Render counter
    cv2.rectangle(img, (0, 0), (245, 73), (245, 117, 16), -1)

    # Rep data
    cv2.putText(img, 'REPS', (15, 12),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, str(counter),
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

    # Stage data
    cv2.putText(img, 'STAGE', (85, 12),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, stage,
                (85, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

# create a return to a ligne function
# (Text must have \n to indicate where will be the split)
def ReturnTextLigne(img, text ,y0, dy):
    # y0, dy=50, 4
    for i, line in enumerate(text.split('\n')):
        y= y0+i * dy
        cv2.putText(img, line, (y0, y), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0), 2, cv2.LINE_AA)

#  testing create landmark in the middle of a line
def createLandmark(img, p1, p2):
    lmList=findPosition(img, False)
    _, x1, y1=lmList[p1]
    _, x2, y2=lmList[p2]

    cx, cy=(x1+x2) // 2, (y1+y2) // 2

    cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
    cv2.circle(img, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
    cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
    return cx, cy


#  caculate the distance between two landmarks
def Distance(img, p1, p2):
    """
    :param img: frames of the video stream
    :param p1: the identity of a landmark1
    :param p2: the identity of a landmark2
    """
    lmList=findPosition(img, False)
    _, x1, y1=lmList[p1]
    _, x2, y2=lmList[p2]
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 1)
    cx, cy=(x1+x2) // 2, (y1+y2) // 2
    cv2.circle(img, (cx, cy), 5, (255, 255, 255), cv2.FILLED)
    length=math.hypot(x2-x1, y2-y1)
    return length


def draw_text(frame, text, x, y, color=(255, 0, 255), thickness=4, size=3):
    if x is not None and y is not None:
        cv2.putText(
            frame, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, size, color, thickness)


def rescale_frame(frame, percent=75):
    """
    :param frame: frames of video stream
    :param percent: percent for reducing the video shape
    """
    width=int(frame.shape[1] * percent / 100)
    height=int(frame.shape[0] * percent / 100)
    dim=(width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

