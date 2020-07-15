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
