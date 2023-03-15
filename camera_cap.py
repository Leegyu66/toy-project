import cv2
import numpy as np
cap = cv2.VideoCapture(0)

point = 0
prev_point = None
capture_point = []

COLOR = (255, 0, 0)
THICKNESS = 3

def mouse_handler(event, x, y, flags, param):
    global prev_point
    global capture_point
    
    if event == cv2.EVENT_LBUTTONDOWN:
        point = ((x, y))
        capture_point.append((x, y))
        if prev_point:
            cv2.line(frame, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            cv2.imshow('frame', frame)

        prev_point = point
        if len(capture_point) == 4:
            show_result()
            cv2.line(frame, prev_point, capture_point[0], COLOR, THICKNESS, cv2.LINE_AA)
            cv2.imshow('frame', frame)
        
def show_result():
    global capture_point
    
    width, height = 530, 710
    src = np.float32(capture_point)
    dst = np.array([[0, 0], [width, 0], [width, height] ,[0, height]], dtype=np.float32)
    
    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(frame, matrix, (width, height))
    
    cv2.imshow('result', result)

while cap.isOpened:
    ret, frame = cap.read()
    if not ret:
        break
        
    
    if cv2.waitKey(1) == ord('q'):
        break
    cv2.imshow('frame', frame)
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', mouse_handler)

cap.release()
cv2.destroyAllWindows()    