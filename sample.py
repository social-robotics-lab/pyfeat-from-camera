import cv2
from feat import Detector

detector = Detector()
cap = cv2.VideoCapture(0)
try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break

        # Convert the frame to RGB (Py-Feat expects RGB images)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect facial expressions in the frame
        detected_faces = detector.detect_faces(rgb_frame)
        detected_landmarks = detector.detect_landmarks(rgb_frame, detected_faces)
        predictions = detector.detect_emotions(rgb_frame, detected_faces, detected_landmarks)

        if cv2.waitKey(1) & 0xFF == ord('q'): raise KeyboardInterrupt
        cv2.imshow('image', frame)

        # detect_emotionsの返り値は
        # anger, disgust, fear, hapiness, sadness, surprise, neutral
        # の7つの要素のarrayです。
        print(f"anger={predictions[0][0][0]}, disgust={predictions[0][0][1]}, fear={predictions[0][0][2]}, \
               hapiness={predictions[0][0][3]}, sadness={predictions[0][0][4]}, surprise={predictions[0][0][5]}, \
               neutral={predictions[0][0][6]}")


except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()
