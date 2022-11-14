import io
from turtle import home
import string
from PIL import Image
from pytesseract import pytesseract
from wand.image import Image as wi

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
pdfFile = wi(filename="goa3.pdf", resolution=300)
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
extract = (text.split())
extract1=(text.split('\n'))


# for imgBlob in imageBlobs:
# 	image = Image.open(io.BytesIO(imgBlob))
# 	text = pytesseract.image_to_string(image, lang='eng')
# 	extract.append(text)
extract = extract[16:]
clean_tweet = []
trash = ["Photo is","Available","|__|"]
for word in extract:
    if word not in string.punctuation and word not in trash:
        clean_tweet.append(word)

print("clean_tweet = {}".format(clean_tweet))
#print(clean_tweet)
name=[]
num=[]
age=[]
dadname={}
husname={}
pos=0
lis=extract1=(text.split('\n'))
for i in range(len(lis)):
    if lis[i][:4]=="Name":
        name.append(lis[i][6:])
    if lis[i][:4]=="Age:":
        age.append(lis[i][5:7])
    if lis[i][:13]=="Father's Name":
        dadname[pos]=lis[i][15:]
        pos+=1
    if lis[i][:14]=="Husband's Name":
        husname[pos]=lis[i][16:]
        pos+=1

lis1=clean_tweet
for i in range(len(lis1)):
    if lis1[i]=="House" and (lis1[i+1]=="Number:" or lis1[i+1]=="Number"):
        num.append(lis1[i+2])
print(len(name),len(age),len(num))
dic={}
pos=0
for i in num:
    if i not in dic:
        dic[i]=[[name[pos]],age[pos]]
    else:
        dic[i].append([[name[pos]],age[pos]])
    pos+=1

for i in dic:
    print("house number=",i)
    print(dic[i])
    print()
pos=0
check="Rajesh Yadu Karmalkar"
for i in range(len(name)):
    if name[i]==check:
        pos=i
key=num[pos]
print("family of ",check,"is",dic[key])
if pos in husname:
    print("husband=",husname[pos])
elif pos in dadname:
    print("fathers name=",dadname[pos])