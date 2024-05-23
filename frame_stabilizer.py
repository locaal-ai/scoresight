import cv2
import numpy as np


# This class is used to stabilize the frames of the video.
# It uses ORB features to match keypoints between frames and calculate an affine transform to
# warp the frame.
class FrameStabilizer:
    def __init__(self):
        self.stabilizationFrame = None
        self.stabilizationFrameCount = 0
        self.stabilizationBurnInCompleted = False
        self.stabilizationKPs = None
        self.stabilizationDesc = None
        self.orb = None
        self.matcher = None

    def reset(self):
        self.stabilizationFrame = None
        self.stabilizationFrameCount = 0
        self.stabilizationBurnInCompleted = False
        self.stabilizationKPs = None
        self.stabilizationDesc = None

    def stabilize_frame(self, frame_rgb):
        if self.stabilizationFrame is None:
            self.stabilizationFrame = frame_rgb
            self.stabilizationFrameCount = 0
        elif not self.stabilizationBurnInCompleted:
            self.stabilizationFrameCount += 1
            # add the new frame to the stabilization frame
            frame_rgb = cv2.addWeighted(frame_rgb, 0.5, self.stabilizationFrame, 0.5, 0)
            if self.stabilizationFrameCount == 10:
                self.stabilizationBurnInCompleted = True
                # extract ORB features from the stabilization frame
                self.orb = cv2.ORB_create()
                self.stabilizationKPs, self.stabilizationDesc = (
                    self.orb.detectAndCompute(self.stabilizationFrame, None)
                )
                self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        if (
            self.stabilizationBurnInCompleted
            and self.stabilizationFrame is not None
            and self.orb is not None
            and self.matcher is not None
            and self.stabilizationKPs is not None
            and self.stabilizationDesc is not None
        ):
            # stabilization burn-in period is over, start stabilization
            # extract features from the current frame
            kps, desc = self.orb.detectAndCompute(frame_rgb, None)
            # match the features
            matches = self.matcher.match(self.stabilizationDesc, desc)
            # sort the matches by distance
            matches = sorted(matches, key=lambda x: x.distance)
            # calculate an affine transform from the matched keypoints
            src_pts = np.float32(
                [self.stabilizationKPs[m.queryIdx].pt for m in matches]
            ).reshape(-1, 1, 2)
            dst_pts = np.float32([kps[m.trainIdx].pt for m in matches]).reshape(
                -1, 1, 2
            )
            h, _ = cv2.estimateAffinePartial2D(src_pts, dst_pts)
            # warp the frame
            if h is not None:
                frame_rgb = cv2.warpAffine(
                    frame_rgb,
                    h,
                    (frame_rgb.shape[1], frame_rgb.shape[0]),
                    flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR,
                )

        return frame_rgb
