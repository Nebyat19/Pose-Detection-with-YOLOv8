import cv2
import cvzone
import numpy as np
from ultralytics import YOLO

# Load the pose detection model
model = YOLO("yolov8/yolov8n-pose.pt")  

# Open webcam
cap = cv2.VideoCapture(0)

# connections
connections = [
(3, 1), (1, 0), (0, 2), (2, 4), (1, 2),(4, 6), (3,5),
(5, 6), (5, 7), (7, 9),
(6, 8), (8, 10),
(11, 12), (11, 13), (13, 15),
(12, 14), (14, 16),
(5, 11), (6, 12)
]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        cap=cv2.VideoCapture("video.MOV")
        continue

    # Resize the frame to fit the model input size 
    frame = cv2.resize(frame, (640, 480))
    width,height=frame.shape[:2]

    # Create a blank black image (no background)
    blank_image = np.zeros((width,height,3),dtype=np.uint8) 

    # Perform pose detection 
    results = model(frame)


    for keypoints in results[0].keypoints.data:
        keypoints=keypoints.cpu().numpy()
        for i,keypoint in enumerate(keypoints):
            x,y, confidence = keypoint
            if confidence > 0.7:
                cv2.circle(blank_image, (int(x),int (y)), radius=5, color=(0,250,50), thickness=1)
                cv2.putText(blank_image, f'{i}', (int(x), int(y)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1, cv2.LINE_AA)

   
    for part_a,part_b in connections:
          if keypoints.any():
            x1,y1, conf1 = keypoints[part_a]
            x2,y2, conf2 = keypoints[part_b]

            if conf1 >0.5 and conf2 >0.5:
                cv2.line(blank_image,(int(x1),int(y1)),(int(x2),int (y2)),  (50,250,250), thickness=2)


    # Plot pose keypoints and skeleton (without the bounding boxes and labels)
    frame = results[0].plot(labels=False, conf=False, boxes=False)

    # Stack images
    output = cvzone.stackImages([frame, blank_image], cols=2, scale=0.80)

    # Display the result
    cv2.imshow("Pose Keypoints and Skeleton", output)
   
    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

