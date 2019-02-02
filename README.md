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
3. Run the file called converter either through command line or your prefered IDE
4. Enter name width and height of the image remebering to include the file extenison (e.g. bird.jpg)
5. And you're done

To see a before and after of the image open greyscale.png and the result.txt files 

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
- [x] Make it use more characters than just 1s and 0s (this will be done by color density)
- [x] Add a propper interface rather than having users go through code
- [ ] Add a GUI


