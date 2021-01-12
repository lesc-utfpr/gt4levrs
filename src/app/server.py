import zmq
import cv2
import numpy as np

import mediapipe as mp
import mediapipe.python.solutions.drawing_utils as mp_drawing
import mediapipe.python.solutions.hands as mp_hands


def handling_frame(frame):
    if frame.shape[0] > frame.shape[1]:
        margin = int((frame.shape[0] - frame.shape[1]) / 2)
        frame = frame[margin:-margin]
    else:
        margin = int((frame.shape[1] - frame.shape[0]) / 2)
        frame = frame[:, margin:-margin]

    frame = np.flip(frame, axis=1).copy()
    return cv2.resize(frame, (128, 128))


################################################################################
#   Creatig src and socket binding
################################################################################
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

################################################################################
#   Starting Hand-tracking
################################################################################
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

################################################################################
#   Starting WebCam
################################################################################
cap = cv2.VideoCapture(1)

while True:

    ########################################
    # Stage 01 - Waiting

    print("Waiting request ...")

    #  Wait for next request from client
    message = socket.recv_string()

    ########################################
    # Stage 02 - Receive

    print("Received request: %s" % message)

    if not (message == "handtracking"):
        socket.send(b"error1")
        continue

    ########################################
    # Stage 03 - Capture frame from cam

    success, image = cap.read()

    if not success:
        socket.send(b"error2")
        continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    ########################################
    # Stage 04 - Call mediapipe

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    ########################################
    # Stage 05 - Check result

    if not results.multi_hand_landmarks:
        socket.send(b"error3")
        continue

    coordenates = results.multi_hand_landmarks

    landmarks_count = 0
    for hand_landmarks in coordenates:
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        landmarks_count += 1

    if landmarks_count != 21:
        socket.send(b"error4")
        continue

    #relative_coordenates = converter.convert_to_relative(absolute_coordenates=coordenates)

    #new_coordenates = converter.convert_to_absolute(relative_coordenates)

    socket.send(b"ack")

    landmarks_count = 0
    for hand_landmarks in coordenates:
        mp_hands.HAND_CONNECTIONS
        message = socket.recv_string()

        if not (message == "next"):
            socket.send(b"error5")
            break

        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        landmarks_count += 1

    print(landmarks_count)


    for joint in xyz:

        socket.send_string("joint;{};{};{}".format(joint[0], joint[1], joint[2]))

    message = socket.recv_string()
    socket.send(b"end")

    ########################################

    cv2.imshow('MediaPipe Hands', image)

    if cv2.waitKey(10) & 0xFF == 27:
        break

socket.close()
hands.close()
cap.release()
