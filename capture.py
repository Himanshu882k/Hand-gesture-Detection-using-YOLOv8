import os
import cv2
import time
import uuid

IMAGE_PATH = 'CollectedImages'

labels = ['Hello', 'Yes', 'No', 'Thanks', 'Looser', 'OK']
number_of_images = 100
counter = 1

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)  # Make sure directory is created if it doesn't exist
    cap = cv2.VideoCapture(0)  # Open the camera
    print('Collecting Images for {}'.format(label))
    time.sleep(5)  # Initial delay before starting image collection

    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Could not read frame. Check camera connection.")
            continue
        
    
        # Construct the image name
        imagename = os.path.join(img_path, label + str(counter) + '.jpg')
        cv2.imwrite(imagename, frame)  # Save the original-sized image
        cv2.imshow('frame', frame_resized)  # Display the resized frame
        
        # Pause for 2 seconds between images
        time.sleep(2)
        
        counter += 1  # Increment counter for the next image
        
        # Press 'q' to break out of the loop early if needed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()  # Release the camera resource after each label

cv2.destroyAllWindows()  # Close all OpenCV windows
