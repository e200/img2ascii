from sys import argv
import cv2

if len(argv) != 3:
  print('Usage: python3 img2ascii input.jpg output.txt')

  exit(1)

chars = ' .,:;%#@'[::-1]

max_default_size = 40

input_filename = argv[1]
output_filename = argv[2]

source_img = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)

width, height = source_img.shape

if width > max_default_size:
  source_img = cv2.resize(source_img, (max_default_size, max_default_size))
  
  width, height = source_img.shape

with open(output_filename, 'w') as output_file:
  for col in range(height):
    line = ''
    
    for row in range(width):
      char_index = round(source_img[col][row] / 255 * len(chars))

      line += chars[char_index - 1] + ' '

      if row == width - 1:
        output_file.write(line + '\n')
