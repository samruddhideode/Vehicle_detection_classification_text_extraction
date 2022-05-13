import cv2
from numpy import array
from detection import vehicle_detection
from classification import vehicle_classification


col_images = []

for v in range(1, 3):
    video_frames = []

    # convert video into frame format
    video1 = cv2.VideoCapture('input/video'+str(v)+'.mp4')
    print(v, ' ', video1.isOpened())

    cnt = 0
    while(video1.isOpened()):
        ret, frame = video1.read()
        if(ret == True):
            # print("True")
            cv2.imwrite('Frames'+str(v)+'/frame%d.jpg' % cnt, frame)
            video_frames.append(frame)
            cnt += 1
        else:
            break

    col_images.append(video_frames)
    print('stored frames for video ', v)
print('total images', len(col_images))

# extracts vehicles from frames and stores in extracted_cars/
vh = vehicle_detection()

print('video1')
veh_no = vh.detect(col_images[0], 1, 0)
print('video2')
veh_no = vh.detect(col_images[1], 2, veh_no)

'''
print('video3')
veh_no = vh.detect(col_images[2], 3, veh_no)
'''

vc = vehicle_classification()
vc.classify()
