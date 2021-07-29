#!/usr/bin/python3

import cv2
from sys import argv
import argparse
import cv2

parser = argparse.ArgumentParser(
    description='Map image pixels to ASCII characters')

parser.add_argument('-i', '--input', help='Source image', required=True)
parser.add_argument('-sc', '--scale', help='Output scale')
parser.add_argument('-c', '--chars', help='Custom ASCII chars to map')

args = vars(parser.parse_args())

input_filename = args['input']

  resized_image = cv2.resize(source_img, (round(width * scale), round(height * scale)))

  return resized_image

def img2ascii(source, chars):
  lines = []

  width, height = source.shape

  for col in range(height):
    line = ''

    for row in range(width):
      pixel = source[row][col]

      char = getPixelEquivalentChar(pixel, chars)

      line += char + ' '

      if row == width - 1:
        lines.append(line)

  return lines

if len(argv) != 2:
  print('Usage: python3 img2ascii input.jpg')

  exit(1)

chars = ' .,:;%#@'

input_filename = argv[1]

source_img = get_img(input_filename, 0.2)

ascii_text_lines = img2ascii(source_img, chars)
ascii_text = '\n'.join(ascii_text_lines)

print(ascii_text)
