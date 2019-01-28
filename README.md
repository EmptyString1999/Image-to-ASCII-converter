# Image-to-ASCII-converter
This is an simple Image to ASCII converter using the python package Pillow using only 1s and 0s.

To try this yourself first install python and pillow, if you dont know how to do this follow the instructions below 

### --------------------------------------------------------------------

## How to download and install Python and Pillow
1. Download and install Anaconda for Pyhton version 3.7 from this website: https://www.anaconda.com/download
2. Once installed open the Anaconda prompt and type: conda install pillow

### --------------------------------------------------------------------

## How to use the converter
1. Downlaod or clone the git page
2. Once downloaded open the folder and place the image you want to convert in to the folder 
3. Open the file called converter.py in IDLE or your prefered IDE
4. On line 4 change the variable filename to the name of the image
5. On line 5 chnage the numbers to the width and height of the image respectivley 
6. Run the file in either command line or through the IDE 
7. open the file result to see the converted image

## Runtimes compared to image sizes

1. 10px by 10px
  - 0.07283
2. 100px by 50px
  - 0.02893
3. 200px by 100px
  - 0.06087
4. 1200px by 635px (original image size)
  - 0.81083

## Future plans for project
- [ ] Make it use more characters than just 1s and 0s (this will be done by color density)
- [ ] Add a propper interface rather than having users go through code


