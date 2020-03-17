import numpy as np
import argparse
import imutils
import sys
import cv2




while True:
	

	frames = []

	# loop over the number of required sample frames
	for i in range(0, SAMPLE_DURATION):
	
		(grabbed, frame) = vs.read()

		
		if not grabbed:
			print("[INFO] no frame read from stream - exiting")
			sys.exit(0)

		
		frame = imutils.resize(frame, width=400)
		frames.append(frame)





for frame in frames:
		
		cv2.rectangle(frame, (0, 0), (300, 40), (0, 0, 0), -1)
		cv2.putText(frame, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
			0.8, (255, 255, 255), 2)

		# display the frame to our screen
		cv2.imshow("Activity Recognition", frame)
		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			break