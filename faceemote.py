import cv2
from fer import FER

# Load the face detector and emotion recognition model
emotion_detector = FER(mtcnn=True)  # Using MTCNN for better face detection

# Initialize the webcam video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        break

    # Detect emotions in the current frame
    emotion_results = emotion_detector.detect_emotions(frame)

    # Loop through all detected faces and emotions
    for result in emotion_results:
        (x, y, w, h) = result["box"]
        emotions = result["emotions"]
        
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display all detected emotions with their confidence
        y_offset = y - 10
        for emotion, score in emotions.items():
            # Check if the emotion and score are valid
            if emotion and score is not None:
                # Safely display the detected emotion and its confidence score
                cv2.putText(frame, f'{emotion.capitalize()} ({int(score * 100)}%)',
                            (x, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                y_offset -= 30
            else:
                print("Error: Invalid emotion or score detected")

    # Display the frame with the emotion and face bounding box
    cv2.imshow('Emotion Detector', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
