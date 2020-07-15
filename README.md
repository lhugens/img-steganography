## About

Given a .png picture and a .txt file, this script changes the RGB values of some pixels slightly so as to enconde the message on the text file. Given only a .png picture with a hidden message previously encoded by this script, it will decode it.

## NOTES

The specific usage of the .png format resides in the fact that it is a lossless format, as opposed to  .jpg files, which is a compressed file format, which means that uppon saving the altered picture it compresses it by altering the RGB values, destroying the hidden message.

## Dependencies

Python Image Library (PIL)
```
$ pip install Pillow
```

## Usage

To encode a pic.png with text.txt:
```
python sten.py -f pic.png -m text.txt
```

To decode pic-new.png:
```
python sten.py -f pic-new.png
```

## How it works

Each pixel of a picture has an RGB code in the form of a tuple, ex: (124, 35, 12).\
Each letter of the message has an 8bit representation, ex: l is 01101100.\
The encoding is done by associating 3 pixels to each letter by associating a letter bit to one value of the RGB code. If that bit is 0, we make the value even, and if its 1 we make the value even. We also make remaining 9th color value even if the message is not over, and odd if it is. Thus the 'l' would  be encoded in a certain set of 3 pixels like so:

```
original: (124, 35, 12) (34, 4, 89) (23, 9, 4)
             0   1   1    0  1   1    0  0 
encoded:  (124, 35, 13) (34, 5, 89) (24, 8, 3)
```
