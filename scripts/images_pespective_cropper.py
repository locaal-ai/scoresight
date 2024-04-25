import os
import uuid
import cv2
import numpy as np
import glob
import sys

current_image = None
points = []
output_folder = None


def mouse_callback(event, x, y, flags, param):
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append((x, y))
            current_image_copy = current_image.copy()
            for pt in points:
                cv2.circle(current_image_copy, pt, 5, (0, 255, 0), -1)
            # draw lines between the points with polylines
            if len(points) > 1:
                cv2.polylines(
                    current_image_copy,
                    [np.array(points, dtype=np.int32)],
                    True,
                    (0, 255, 0),
                    2,
                )
            cv2.imshow("Image", current_image_copy)
            if len(points) == 4:
                # find the bounding box of the points
                x, y, w, h = cv2.boundingRect(np.array(points))
                homography, _ = cv2.findHomography(
                    np.array(points), np.array([(0, 0), (0, h), (w, h), (w, 0)])
                )
                cropped = cv2.warpPerspective(current_image, homography, (w, h))
                cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
                _, thresholded = cv2.threshold(
                    cropped, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
                )
                cv2.imshow("Cropped Image", thresholded)
                # save the cropped image into a folder called "cropped_images" in the same directory as the script
                output_path = output_folder + "/cropped_" + str(uuid.uuid4()) + ".jpg"
                print("Saving cropped image to", output_path)
                cv2.imwrite(output_path, thresholded)
                points = []


def main():
    global points, current_image, output_folder

    if len(sys.argv) < 2:
        print("Please provide the path to the image folder as a command-line argument.")
        return

    image_folder_path = sys.argv[1]
    output_folder = image_folder_path + "/cropped_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    images = glob.glob(image_folder_path + "/*")

    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", mouse_callback)

    for image_path in images:
        points = []
        current_image = cv2.imread(image_path)

        cv2.imshow("Image", current_image)
        while True:
            key = cv2.waitKey(50) & 0xFF

            if key == ord(" "):
                break
            if key == ord("q"):
                cv2.destroyAllWindows()
                return

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
