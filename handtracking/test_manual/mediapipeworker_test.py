from queue import Queue

from app.threads import HandTrackingWorker
import cv2

data = Queue(maxsize=1)

process = HandTrackingWorker(cap=cv2.VideoCapture(0), queue=data, debug_video=True)

process.start()
