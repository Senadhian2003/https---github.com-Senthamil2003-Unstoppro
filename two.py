# import io
# from turtle import home
# import string
# from PIL import Image
# from pytesseract import pytesseract
# from wand.image import Image as wi
#
# path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# pytesseract.tesseract_cmd = path_to_tesseract
# pdfFile = wi(filename="goa2.pdf", resolution=300)
# image = pdfFile.convert('jpeg')
#
# imageBlobs = []
#
# for img in image.sequence:
#     imgPage = wi(image=img)
#     imageBlobs.append(imgPage.make_blob('jpeg'))
#
# l = []
# l = imageBlobs[2:]
# dummyVar = 78
# effectiveDummy = dummyVar // 30
# print(effectiveDummy)
#
# extract = []
#
# image = Image.open(io.BytesIO(l[effectiveDummy]))
# text = pytesseract.image_to_string(image, lang='eng')
# extract = (text.split())
#
#
# # for imgBlob in imageBlobs:
# # 	image = Image.open(io.BytesIO(imgBlob))
# # 	text = pytesseract.image_to_string(image, lang='eng')
# # 	extract.append(text)
# extract = extract[16:]
#
# clean_tweet = []
# trash = ["Photo", "is", "Available", "|__|"]
# for word in extract:
#     if word not in string.punctuation and word not in trash:
#         clean_tweet.append(word)
#
# print("clean_tweet = {}".format(clean_tweet))
#
#
# # print(clean_tweet)


# VIJAYASRIII


import io
from turtle import home
import string
from PIL import Image
from pytesseract import pytesseract
from wand.image import Image as wi

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
pdfFile = wi(filename="goa2.pdf", resolution=300)
image = pdfFile.convert('jpeg')

imageBlobs = []

for img in image.sequence:
    imgPage = wi(image=img)
    imageBlobs.append(imgPage.make_blob('jpeg'))

l = []
l = imageBlobs[2:]
dummyVar = 78
effectiveDummy = dummyVar // 30
print(effectiveDummy)

extract = []

image = Image.open(io.BytesIO(l[effectiveDummy]))
text = pytesseract.image_to_string(image, lang='eng')

extract1=(text.split('\n'))


# for imgBlob in imageBlobs:
# 	image = Image.open(io.BytesIO(imgBlob))
# 	text = pytesseract.image_to_string(image, lang='eng')
# 	extract.append(text)
extract = extract1[16:]
clean_tweet = []
trash = ["Photo is","Available","|__|"]
for word in extract:
    if word not in string.punctuation and word not in trash:
        clean_tweet.append(word)

clean_tweet=format(clean_tweet)

print((clean_tweet))





