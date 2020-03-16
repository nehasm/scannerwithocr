# `scannerwithocr`
The aim of this project is to make a scanner that take raw image as a input to produce scanned copy by perform transformation and then the scanned copy act as a input to ocr engine to extract text from it.

## `There is two part of this project:`
* Scanner
* OCR

### `Scanner`
The Scanner perform following operation to convert raw image into scanned image:
* `Edge detection`
* `Cropping image`
* `Enhancement of cropped image`

##### `Flow of scanner`
<p>Once you put raw image as a input to scanner through command prompt,an edge detection is perform on it to detect the boundaries of paper.<br/>
With this the window will popup which contains the detected boundaries of image.These boundaries are fexible and the user can change this boundaries.<br/>
The image will be cropped with respect to the final boundaries of that window.<br/>
After getting the final boundaries the enhancement transformation is performed on image to remove noise and make it as a scanned image.<br/>
The scanned image will get save into output folder with same name as a raw image.
</p>

#### Screens
<a href="https://ibb.co/XWhz00P"><img width="200" src="https://i.ibb.co/S6hKYYg/darkbackground.jpg" alt="darkbackground" border="0"></a>
<a href="https://ibb.co/Jqfrjn5"><img width="200" height="270" src="https://i.ibb.co/2SDc3qg/darkout.png" alt="darkout" border="0"></a>
<a href="https://ibb.co/vZjStWt"><img width="200" height="270" src="https://i.ibb.co/hDmSqNq/dark-background.jpg" alt="dark-background" border="0"></a>
* Image 1:Raw Image
* Image 2:Window with detected edge
* Image 3:Scanned image

#### `Uniqueness of this repository` 
The edge detection will also run on one of the most difficult case of white or less contrast background with white paper,it is possible through EAST TEXT DETECTION algorithm.
##### Screens
<a href="https://ibb.co/hVjp7h3"><img width="200" height="270" src="https://i.ibb.co/rHSn7TD/whitebackground.jpg" alt="whitebackground" border="0"></a>
<a href="https://ibb.co/dMzSpqX"><img width="200" height="270" src="https://i.ibb.co/pw9gK8N/whiteout.png" alt="whiteout" border="0"></a>
<a href="https://ibb.co/TTS9SvF"><img width="200" height="270" src="https://i.ibb.co/N3PcPVH/white-background.jpg" alt="white-background" border="0"></a>
#### `Countinuing the uniqueness of this repository`
<p>The scanner ask the user whether the input image has watermark or not.<br/>
If there is watermark in the raw image it will be removed.</p>

#####  Screens
<a href="https://ibb.co/6P1MXRk"><img width="200" height="270" src="https://i.ibb.co/VSQ1wWs/invoice-paid-watermark.png" alt="invoice-paid-watermark" border="0"></a>
<a href="https://ibb.co/NZxLx1M"><img width="200" height="270" src="https://i.ibb.co/jghLhVS/watermarkout.png" alt="watermarkout" border="0"></a>
<a href="https://ibb.co/Jp6BW2T"><img width="200" height="270" src="https://i.ibb.co/3F6r5Wb/invoice-paidwatermark.png" alt="invoice-paidwatermark" border="0"></a>

### `OCR`
In these way the scanner give us the scanned image,as said earlier the scanned image is input of OCR engine.
The ocr.py contains all the require code for extracting text from scanned image.
##### Screens
<a href="https://ibb.co/JqxdPmY"><img width="300" height="350" src="https://i.ibb.co/HCN2QBc/watermarkocr.png" alt="watermarkocr" border="0"></a>
* Image contain the extract text from the watermark image.
#### `Note:`
The ocr engine used here in pytesseract,you can use any of the ocr engine.

### `Usage`
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
* After this the user will be asked for watermark with message:
```
If watermark present?put[Y] or [N]
```
Put Y if watermark is present,otherwise N.
#### `OCR`
The ocr engine executes with file name ocr.py
```
python ocr.py
```
Then the user will be asked for the scanned image with meassage:
```
Define image name for ocr
```
After getting input image the ocr engine will performed its operation to give the text which will be printed on command prompt.


The **Scanner app** can be made with the same algorithm in java by using java version of opencv.[see here](https://github.com/burhanuday/codesquad-PS1)
