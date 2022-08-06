import cv2
import os


path = 'Images/'
Filename =[]

pictures= []


for x in os.listdir(path):
    name,ext = os.path.splitext(x)
    if ext in ['gif', 'png', 'jpg', 'jpeg', 'jfif']:
        file_path = path + "/" +x
        pictures.append(file_path)
        print(file_path)

count = len(pictures)
frame = cv2.imread(pictures[0])
shape = frame.shape
size = (shape[0], shape[1])
print(size)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 0.8
Size = size
out= cv2.VideoWriter('proj.avi',fourcc,fps,Size)

for i in range(0, count):
    print(pictures[i])
    img = cv2.imread(pictures[i])
    out.write(img)

out.release()