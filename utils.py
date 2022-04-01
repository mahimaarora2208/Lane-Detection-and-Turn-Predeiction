import cv2
import numpy as np
import glob
 
img_array = []
for filename in glob.glob('/home/mahima/spring_2022/ENPM673/project2/data_1/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()