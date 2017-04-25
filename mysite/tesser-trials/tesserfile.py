import tesserocr
from PIL import Image

#print (tesserocr.tesseract_version())  # print tesseract-ocr version
#print (tesserocr.get_languages())  # prints tessdata path and list of available languages

image = Image.open('chocolate-1.jpg')
text = tesserocr.image_to_text(image)  # print ocr text from image
print(text)
# or
#print (tesserocr.file_to_text('sample.jpg'))
