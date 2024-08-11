# coded by iensarkok


# importing the necessary libraries
# (for pytesseract doesn't enought 'pip install pytesseract' command
# it is necessary to install this file https://github.com/UB-Mannheim/tesseract/wiki)

import cv2
import pytesseract

# adding pytesseract.exe path
# (if you don't use this command you may get "PATH ERROR")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# declaring the image path
img_path = r'D:\GitHub\PythonRepo\optical-character-recognition\image.png'

#reading the image
img = cv2.imread(img_path)

# cv2 read image as BGR but pytesseract use RGB format.
# so converting the RGB format
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# reading the text in the image
text = pytesseract.image_to_string(image_rgb, lang='eng')

# exporting the text as pdf document
pdf = pytesseract.image_to_pdf_or_hocr(image_rgb, extension='pdf')
with open('text.pdf', 'w+b') as f:
    f.write(pdf)

# printing the text in the image
print('Texto: ',text)


# displaying the image
cv2.imshow('Image',image_rgb)

# waits for user press any key
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()