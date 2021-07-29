#!/usr/bin/python3

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

scale = args['scale']
chars = (args['chars'] or ' .,:;%#@')[::-1]


def get_pixel_equivalent_char(pixel, chars):
  char_index = round(pixel / 255 * len(chars))

  return chars[char_index - 1]


source_img = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)

height, width = source_img.shape

if scale:
  scale = float(scale)

  source_img = cv2.resize(source_img, (int(width * scale), int(height * scale)))

height, width = source_img.shape

with open('output.txt', 'w') as output_file:
  for col in range(height):
    line = ''

    for row in range(width):
      char_index = round(source_img[col][row] / 255 * len(chars))

      line += chars[char_index - 1] + ' '
  
    output_file.write(line + "\n")
