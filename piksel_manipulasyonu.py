import cv2 as cv

#img=cv.imread(r'TechIstComputerVision-main/zoom_kodlar/yesil_elma.jpg')
img=cv.imread(r'data/yesil_elma.jpg')
#görüntü boyutunu alma
height,width=img.shape[:2]
print("Genişlik ve yükseklik : " , width,height)

#beyaz kare
kare_boyut=50
baslangic_x=(width//2)-25
baslangic_y=(height//2)-25

for y in range(baslangic_y,baslangic_y+kare_boyut):
    for x in range(baslangic_x,baslangic_x+kare_boyut):
        img[y,x]=[255,255,255]

cv.imshow("ELma",img)
cv.waitKey(0)
cv.destroyAllWindows()

