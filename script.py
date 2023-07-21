import PIL.Image

def mapping(val, s1, s2, n1, n2):
	nval=n1+((n2-n1)*(val-s1))//(s2-s1)
	return nval

# ascii characters used to build the output text
#density=list('Ñ@#W$9876543210?!abc;:+=-,._ ')
density=list("""B0AbgDHaGd8EN6Q9h#e@KM45O3F21Ckfpjq$J7Pm&cIoRW%nSiUsXLwltyVZ/uTY;x()vz:?".r,'! """)
charLength=len(density)-1

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/ width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([density[mapping(pixel,0,255, charLength, 0)] for pixel in pixels])
    return(characters)    

def main(new_width=100):
    # attempt to open image from user-input
    path = input("Enter Image location:") 
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return
  
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(resize_image(image), new_width)))

    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
 
# run program
main(190)
