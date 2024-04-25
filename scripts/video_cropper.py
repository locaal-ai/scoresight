import cv2
import tkinter as tk
from tkinter import filedialog
import os
import sys
import os
import uuid
import numpy as np
from tqdm import tqdm

points = []


def draw_rectangle(event, x, y, flags, param):
    global drawing, points
    if event == cv2.EVENT_LBUTTONDOWN:
        frame_copy = frame.copy()
        if len(points) < 4:
            points.append((x, y))
            if len(points) > 1:
                for i in range(1, len(points)):
                    cv2.line(frame_copy, points[i - 1], points[i], (0, 255, 0), 2)
            for pt in points:
                cv2.circle(frame_copy, pt, 5, (0, 255, 0), -1)
        cv2.imshow("First Frame", frame_copy)
        if len(points) == 4:
            cv2.destroyWindow("First Frame")


if len(sys.argv) < 2:
    print("Please provide a video file path")
    sys.exit(1)

video_path = sys.argv[1]
if not os.path.exists(video_path):
    print("Error: video file does not exist")
    sys.exit(1)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

if not ret:
    print("Error: unable to read the video file")
    sys.exit(1)

drawing = False
top_left_pt, bottom_right_pt = (-1, -1), (-1, -1)

cv2.namedWindow("First Frame")
cv2.setMouseCallback("First Frame", draw_rectangle)

cv2.imshow("First Frame", frame)
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if len(points) == 4:
        break

cv2.destroyAllWindows()

if len(points) == 4:
    video_folder = os.path.dirname(video_path)
    # get the video base name
    video_base_name = os.path.splitext(os.path.basename(video_path))[0]
    # use the base name without the extension as the out folder name
    out_folder = os.path.join(video_folder, video_base_name)
    os.makedirs(out_folder, exist_ok=True)

    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    frame_count = 0
    cropped_frame = None
    written_frames = 0

    print("Cropping and saving frames...")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    progress_bar = tqdm(total=total_frames)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % 75 == 0:
            # calculate the new cropped frame using the homography
            # the new shape should be the bounding box of the 4 points
            pts = np.array(points, dtype=np.float32)
            pts = pts.reshape(-1, 1, 2)
            new_shape = cv2.boundingRect(pts)
            # calculate the width by the ration in the 4 corner points
            distance_pt1_pt2 = np.linalg.norm(np.array(points[0]) - np.array(points[1]))
            distance_pt2_pt3 = np.linalg.norm(np.array(points[1]) - np.array(points[2]))
            new_shape = (
                new_shape[0],
                new_shape[1],
                int(distance_pt1_pt2),
                int(distance_pt2_pt3),
            )
            # calculate the homography from the points to the new shape
            h, _ = cv2.findHomography(
                pts,
                np.array(
                    [
                        [0, 0],
                        [new_shape[2], 0],
                        [new_shape[2], new_shape[3]],
                        [0, new_shape[3]],
                    ],
                    dtype=np.float32,
                ),
            )
            # warp the frame
            new_cropped_frame = cv2.warpPerspective(
                frame, h, (new_shape[2], new_shape[3])
            )
            # otsu thresholding
            new_cropped_frame = cv2.cvtColor(new_cropped_frame, cv2.COLOR_BGR2GRAY)
            _, new_cropped_frame = cv2.threshold(
                new_cropped_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )
            # check if the frame is the first one
            if cropped_frame is None:
                cropped_frame = new_cropped_frame
            else:
                # check if the frame is the same as the previous one with a threshold
                diff = cv2.absdiff(cropped_frame, new_cropped_frame)
                # _, diff = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)
                if cv2.countNonZero(diff) > 400:
                    cropped_frame = new_cropped_frame
                else:
                    frame_count += 1
                    progress_bar.update(1)
                    continue

            frame_id = str(uuid.uuid4())
            cv2.imwrite(f"{out_folder}/frame_{frame_id}.png", cropped_frame)
            written_frames += 1

        # skip 25 frames
        frame_count += 1
        progress_bar.update(1)

    cap.release()
    progress_bar.close()

print(f"{written_frames} frames cropped and saved successfully!")
