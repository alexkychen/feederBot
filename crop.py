import cv2
import numpy as np

filename = input("Enter file name: ")

file_path = "images/"+filename

try:
    img = cv2.imread(file_path)
    #check if the file convertable, if not, meaning the file not exist
    img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
except:
    print("File not found")
    exit()

#Resize input image to better fit the screen
#get image width
width_origin = img.shape[1]
#calculate a factor to change width to 1200 px
downsize_perc = 1200 / width_origin
#calculate new height
height_new = int(img.shape[0]*downsize_perc)
#resize image
img_resize = cv2.resize(img, (1200, height_new))

#define mouse call back function
drawing = False
ix, iy = -1, -1

def draw_rect(event, x, y, flags, param):
    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.retangle(img_resize, (ix, iy), (x, y), (0,0,255), 3)


#display image
while(1):
    cv2.imshow("img", img_resize)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
