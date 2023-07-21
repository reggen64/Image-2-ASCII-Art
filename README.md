# Image-2-ASCII-Art
This code converts a given image to an equivalent ascii art. 

Firstly, you'd need to have ascii characters sorted according to their "brightness" (i.e. just sum of their pixel values) in the same text font that is begin used by your terminal (it would be better if it
is monospaced because this script does not take care of differenct spacing of fonts). `sort.py` sorts the files according to the sum of their pixel values of the font style (the one used here is obtained from  wfonts). Run `sort.py` in the same directory with the font images.

After obtaining the brightness level, `script.py` first converts the image to grayscale and then spits out the characters in accordance with a mapping from the grayscale pixel values to the sorted array of 
the ascii characters

You can see an example below:

![Example](/image.png)
