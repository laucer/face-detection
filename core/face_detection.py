import cv2
import uuid
from django.conf import settings
from pathlib import Path

def detect_faces_and_generate_image(image_path):
    img = cv2.imread(str(image_path))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    detections = faces.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in detections:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    output_name = f"{uuid.uuid4()}.jpg"
    output_path = Path(settings.MEDIA_ROOT) / output_name
    cv2.imwrite(str(output_path), img)
    return output_name


