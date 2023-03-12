import cv2
import numpy as np

src_img = cv2.imread("wear_mask_woman.png")
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
            cv2.line(src_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            cv2.imshow('img', src_img)

        prev_point = point
        if len(capture_point) == 4:
            show_result()
            cv2.line(src_img, prev_point, capture_point[0], COLOR, THICKNESS, cv2.LINE_AA)
            cv2.imshow('img', src_img)
        
def show_result():
    global capture_point
    
    width, height = 530, 710
    src = np.float32(capture_point)
    dst = np.array([[0, 0], [width, 0], [width, height] ,[0, height]], dtype=np.float32)
    
    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(src_img, matrix, (width, height))
    
    cv2.imshow('result', result)
        
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()