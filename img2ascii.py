from sys import argv
import cv2

if len(argv) != 3:
  print('Usage: python3 img2ascii input.jpg output.txt')

  exit(1)

chars = '@#%;:,. '
