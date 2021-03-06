


import numpy as npm #importing numpy module
import cv2  #importing cv module

capture = cv2.VideoCapture(0) #capturing video
while( capture.isOpened() ) :  #untill the video is running the following code is to be executed.
    return_image,image = capture.read()  #reading the data.
    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
    blurr = cv2.GaussianBlur(grey,(5,5),0) #image cleaning 
    return_image,thres = cv2.threshold(blurr,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
  
    con, hier= cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    draw = npm.zeros(image.shape,npm.uint8)

    mx_ar=0
   
    for h in range(len(con)):
            ct=con[h]
            ara = cv2.contourArea(ct)
            if(ara>mx_ar): 
                mx_ar=ara
                cp=h
    ct=con[cp]
    hul = cv2.convexHull(ct)
    moment = cv2.moments(ct)
    if moment['m00']!=0:
                c_x = int(moment['m10']/moment['m00']) 
                c_y = int(moment['m01']/moment['m00']) 
              
    center=(c_x,c_y)       
    cv2.circle(image,center,5,[0,0,255],2)       
    cv2.drawContours(draw,[ct],0,(0,255,0),2) 
    cv2.drawContours(draw,[hul],0,(0,0,255),2) 
          
    cnt = cv2.approxPolyDP(ct,0.01*cv2.arcLength(ct,1),1)
    hul = cv2.convexHull(ct,returnPoints = 0)
    
    if(True):
               defects = cv2.convexityDefects(ct,hul)
               min_d=0
               max_d=0
               for j in range(defects.shape[0]):
                    p,q,r,d = defects[j,0]
                    s = tuple(ct[p][0])
                    e = tuple(ct[q][0])
                    f = tuple(ct[r][0])
                    dis = cv2.pointPolygonTest(cnt,center,1)
                    cv2.line(image,s,e,[0,255,0],2)
                    
                    cv2.circle(image,f,5,[0,0,255],-1)
               print(j)
               j=0 
    cv2.imshow('input',image)    #displaying output
    cv2.imshow('output',draw)
   
                
    t = cv2.waitKey(10)
    if t== 27:
        break                   #infite loop will be breaked






