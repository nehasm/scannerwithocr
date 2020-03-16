# `scannerwithocr`
The aim of this project is to make a scanner that takes raw image as a input to produce scanned copy by performing transformation and then the scanned copy acts as input to ocr engine to extract text from it.

## `There are two part of this project:`
* Scanner
* OCR

### `Scanner`
The Scanner performs following operations to convert raw image into scanned image:
* `Edge detection`
* `Cropping image`
* `Enhancement of cropped image`

##### `Flow of scanner`
<p>Once you put raw image as a input to scanner through command prompt,an edge detection is performed on it to detect the boundaries of paper.<br/>
With this the window will popup which contains the detected boundaries of the image.These boundaries are fexible enough such that the user can change these boundaries.<br/>
The image will be cropped with respect to the final boundaries of this window.<br/>
After getting the final boundaries the enhancement transformations will be performed on the image to remove noise and make it a scanned image.<br/>
The scanned image will get saved into the output folder with same name as of raw image.
</p>

#### Screens
<a href="https://ibb.co/XWhz00P"><img width="200" src="https://i.ibb.co/S6hKYYg/darkbackground.jpg" alt="darkbackground" border="0"></a>
<a href="https://ibb.co/Jqfrjn5"><img width="200" height="270" src="https://i.ibb.co/2SDc3qg/darkout.png" alt="darkout" border="0"></a>
<a href="https://ibb.co/vZjStWt"><img width="200" height="270" src="https://i.ibb.co/hDmSqNq/dark-background.jpg" alt="dark-background" border="0"></a>
* Image 1: Raw Image
* Image 2: Window with detected edge
* Image 3: Scanned image

#### `Uniqueness of this repository` 
* In case of white paper with less contrast background or white background the edge detection run efficiently,this is possible through EAST TEXT DETECTION algorithm
##### Screens
<a href="https://ibb.co/hVjp7h3"><img width="200" height="270" src="https://i.ibb.co/rHSn7TD/whitebackground.jpg" alt="whitebackground" border="0"></a>
<a href="https://ibb.co/dMzSpqX"><img width="200" height="270" src="https://i.ibb.co/pw9gK8N/whiteout.png" alt="whiteout" border="0"></a>
<a href="https://ibb.co/TTS9SvF"><img width="200" height="270" src="https://i.ibb.co/N3PcPVH/white-background.jpg" alt="white-background" border="0"></a>

* <p>The scanner asks the user whether the input image has watermark or not.<br/>If the watermark is present in the raw image it will be removed through watermark removal algorithm.</p>

#####  Screens
<a href="https://ibb.co/6P1MXRk"><img width="200" height="270" src="https://i.ibb.co/VSQ1wWs/invoice-paid-watermark.png" alt="invoice-paid-watermark" border="0"></a>
<a href="https://ibb.co/NZxLx1M"><img width="200" height="270" src="https://i.ibb.co/jghLhVS/watermarkout.png" alt="watermarkout" border="0"></a>
<a href="https://ibb.co/Jp6BW2T"><img width="200" height="270" src="https://i.ibb.co/3F6r5Wb/invoice-paidwatermark.png" alt="invoice-paidwatermark" border="0"></a>

### `OCR`
In this way the scanner gives us the scanned image,as said earlier the scanned image is input of OCR engine.
The ocr.py contains all the required code for extracting the text from scanned image.
##### Screens
<a href="https://ibb.co/JqxdPmY"><img width="300" height="350" src="https://i.ibb.co/HCN2QBc/watermarkocr.png" alt="watermarkocr" border="0"></a>
* Image contains the extract text from the watermark image.
#### `Note:`
You are free to use any of the ocr engine(the ocr engine use here is pytesseract)
### Important:
To run the scanner model file is required which can be downloaded through this [link](https://drive.google.com/file/d/1pmWIdYNNszmdG5b9C806vlXvnv6BqJ1z/view?usp=sharing) and that need to be placed in the scanner folder.
### `How to use?`
#### `Scanner`
```
python scan.py (--images <IMG_DIR> | --image <IMG_PATH>) [-i]
```
* The `-i` flag enables interactive mode, where you will be prompted to click and drag the corners of the document. For example, to scan a single image with interactive mode enabled:
```
python scan.py --image image_name.JPG -i
```
* Alternatively, to scan all images in a directory without any input:
```
python scan.py --images images_folder_name
```
* After this the user will be asked for watermark with a message:
```
If watermark present?put[Y] or [N]
```
Put Y if watermark is present,otherwise N.
#### `OCR`
The ocr engine executes with file name ocr.py.
```
python ocr.py
```
Then the user will be asked for the scanned image with a message:
```
Define image name for ocr
```
After getting the input image the ocr engine will perform its operation to give the text which will be printed on command prompt.


The **Scanner app** can be made with the same algorithm in java by using java version of opencv.[see here](https://github.com/burhanuday/codesquad-PS1)

