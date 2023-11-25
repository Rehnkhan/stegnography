import cv2
import os 
import string

img=cv2.imread("GR1jg9L.jpg")
msg=input("enter secret msg")
password=input("enter password")
d={}
c={}
for i in range(255):
    d[chr[i]]=i
    c[i]=chr[i]

m=n=z=0

for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

cv2.imwrite("encripted.jpg",img)
os.system('start encripted.jpg')
message=''
n=m=z=0

pa=input("enter password")

if password==pa:
    for i in range(len(msg)):
        message=message+c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1)%3
    print("decripted msg is:",message)
else:
    print("not valid key")



