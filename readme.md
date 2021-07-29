# img2ascii

A CLI tool that maps image pixels to ASCII characters.

Built with Python, once you have Python installed, you're good to run it. :)

See the [CS50 final video](https://youtu.be/lqiHoTr5LDA)

## How it works

This project uses OpenCV to read your images.

It iterates through all pixels on the image, and maps each one with a character from a collection of ASCII chars.

## How to use

First, make sure you have Python3 and pip3 installed, then install OpenCV using pip3:

`pip3 install opencv-python`, then, inside the folder containing the script run the following command:

`./img2ascii -i input_image.jpg`

or

`./img2ascii -i input_image.jpg -sc 0.2`

## Todo

* Add output file name CLI option
* Print to the terminal instead of save to a file so user can be able pass th output directly to other CLI tools
