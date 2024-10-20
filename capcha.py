import cv2
import numpy as np

# Load the original image and the piece of the puzzle
original_image = cv2.imread('original_image.png')
puzzle_piece = cv2.imread('puzzle_piece.png')

# Convert images to grayscale
original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
piece_gray = cv2.cvtColor(puzzle_piece, cv2.COLOR_BGR2GRAY)

# Apply template matching to find the piece in the original image
result = cv2.matchTemplate(original_gray, piece_gray, cv2.TM_CCOEFF_NORMED)

# Get the best match position
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Draw a rectangle around the matched area
top_left = max_loc
h, w = puzzle_piece.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(original_image, top_left, bottom_right, (0, 255, 0), 2)

# Show the result
cv2.imshow('Detected Puzzle Piece', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
