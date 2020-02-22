import cv2
import numpy as np
import analyze as az

SUBSCRIPTION_KEY_ENV_NAME = "e0a4ec68847644849409dce0a433d785"
f=0

text = ''' Keep blood pressure lower than 80 mmHg.
patient has a busted vain in the right arm.
have to ensure unconsious anesthesia levels.
patient has a weak spine and is anemic.
'''
extract=''

phrases = ['BP less than 80mmHg', 'Busted vein right arm', 'Uncon. Anesthesia levels','anemic and weak spine']

cap = cv2.VideoCapture("eye_recording.mp4")
#cap = cv2.VideoCapture(0)
x1=[]
'''
for i in text:
            if i != '\n':
                extract+=i
            else:
                #display
                phrases = az.key_phrases(SUBSCRIPTION_KEY_ENV_NAME,extract)
                if phrases:
                    print(phrases[1])
                    extract=''
                    break
                break
            break
'''
print('ON DISPLAY: ',phrases[0])
i=0
while True:
    
    ret, frame = cap.read()
    if ret is False:
        break

    roi = frame[269: 795, 537: 1416]
    rows, cols, _ = roi.shape
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

    _, threshold = cv2.threshold(gray_roi, 3, 255, cv2.THRESH_BINARY_INV)
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        #cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        #print(x,y,w,h)
        #print(x1)
        if y < 225 or x < 300:
            #print('Looking left')
            x1.append(1)
        elif y > 245 or x > 480:
            #print('Looking Right')
            x1.append(1)
        else:
            #print('Looking Straight')
            x1.append(-1)
        
        extract=''
        if x1==[1,-1]:
            f = 1
            print('Is Focused on the operation')
        if f == 1 and x1 == [-1,1]:
            if i < 3:
                i+=1
            else:
                i=i-4
            x = phrases[i]
            print('ON DISPLAY: ',x,' Looked At the text') 
        if len(x1)==2:
            x1.remove(x1[0])
        


        break

    cv2.imshow("Threshold", threshold)
#cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.destroyAllWindows()
