from sys import argv
import cv2

def getPixelEquivalentChar(pixel, chars):
  char_index = round(pixel / 255 * len(chars))

  return chars[char_index - 1]

def get_img(image_path, max_width = 50):
  source_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

  width, height = source_img.shape

  if width > max_width:
    source_img = cv2.resize(source_img, (max_width, max_width))
    
    width, height = source_img.shape
    
  return source_img

def img2ascii(source, chars):
  lines = []
  
  width, height = source.shape
  
  for col in range(height):
    line = ''

    for row in range(width):
      pixel = source_img[col][row]

      char = getPixelEquivalentChar(pixel, chars)

      line += char + ' '

      if row == width - 1:
        lines.append(line + '\n')
    
  return lines
