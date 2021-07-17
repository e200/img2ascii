from sys import argv
import cv2

if len(argv) != 3:
  print('Usage: python3 img2ascii input.jpg output.txt')

  exit(1)

chars = ' .,:;%#@'[::-1]

output_width = 50

input_filename = argv[1]
output_filename = argv[2]

source_img = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)

width, height = source_img.shape

if width > output_width:
  source_img = cv2.resize(source_img, (output_width, output_width))
  
  width, height = source_img.shape

