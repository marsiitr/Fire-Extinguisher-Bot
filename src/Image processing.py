import cv2
import numpy as np

def find_centre2(white_loc):
    n = len(white_loc)
    #print(n)
    if n<120:
        print("No Flame Detected")
        return  
    arr = np.array(white_loc)
    x,y = np.sum(arr,axis=0)/n
    return (round(y), round(x))


def operate(img):

    img_in = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_out = np.zeros(img_in.shape)
    img_out[img_in>190]=255
    img_out[img_in>220]=0
    return img_out

def find_white_loc(img_in):
    white_loc=[]
    m,n = img_in.shape
    for i in range(m):
        for j in range(n):
            if img_in[i,j]==255:
                white_loc.append([i,j])
    return white_loc
count=0
while count<100:
    count=count+1
    video = cv2.VideoCapture('Fire.jpg')
    while True:
        ret,frame = video.read()
        if ret== False:
            break
    
        frame = cv2.resize(frame, (960, 540)) 
 
        blur = cv2.GaussianBlur(frame, (21, 21), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
 
        lower = [18, 50, 50]
        upper = [60, 255, 255]
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(frame, hsv, mask=mask)
        no_red = cv2.countNonZero(mask)
    
        mask = operate(frame)
        white_loc = find_white_loc(mask)
        centre = find_centre2(white_loc)

        if int(no_red) > 15000:
            print("FIRE DETECTED")
            print(centre)
            
            text_file = open("CentreCoordinates.txt", "w")

            text_file.write('1')
            text_file.write(str(centre[0]))
            text_file.write(' ')
            text_file.write(str(centre[1]))

            text_file.close()

        else:

            text_file = open("CentreCoordinates.txt", "w")
            text_file.write('2')
            text_file.close()

        cv2.circle(frame,centre,60,(255,0,255),2)
        #cv2.imshow('gray',mask)
        cv2.imshow('flame',frame)    
        #cv2.imshow('output',output)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cv2.destroyAllWindows()
video.release()