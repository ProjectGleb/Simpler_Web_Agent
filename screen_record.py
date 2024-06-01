import pyautogui
import cv2
import numpy as np
import os
import time

# Specify the duration of the recording in seconds
duration = 1000
end_time = time.time() + duration

# Create a directory to save the frames
output_folder = "frames"
if not os.path.exists(output_folder):
    os.makedirs(output_folder, exist_ok=True)

no_of_frames = 0

while True:
    img = pyautogui.screenshot()

    frame = np.array(img)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Save the frame as an image file
    frame_filename = os.path.join(output_folder, f"frame_{no_of_frames:04d}.png")
    cv2.imwrite(frame_filename, frame[:, :, :3])

    no_of_frames += 1

    # Stop recording when we press 'q' or when the duration is reached
    if time.time() > end_time:
        break

print('Number of frames:', no_of_frames)

# Destroy all windows
cv2.destroyAllWindows()

