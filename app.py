import cv2
import csv
from datetime import datetime
import os

# Full path of attendance file
attendance_file = r"C:\Users\User\Desktop\face-recognition-attendence-systemNew folder\attendance\attendance.csv"

# Create file if it doesn't exist
if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "date", "time"])

# Open webcam
cap = cv2.VideoCapture(0)

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

attendance_marked = False

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera Error")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:

        # Draw rectangle around face
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Mark attendance only once
        if not attendance_marked:

            print("Face Found")

            now = datetime.now()

            with open(attendance_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Somanth",
                    now.strftime("%d-%m-%Y"),
                    now.strftime("%H:%M:%S")
                ])

            print("Attendance Marked Successfully")

            attendance_marked = True

    cv2.imshow("Face Detection", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()