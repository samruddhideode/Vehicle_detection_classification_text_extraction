import cv2
import numpy as np


class vehicle_detection:
    def detect(self, col_images, video_no, veh_no):
        print('extracting cars from ', video_no)
        frame_array_for_video = []

        for j in range(0, len(col_images)-1):
            framei = j

            # convert the frames to grayscale
            grayA = cv2.cvtColor(col_images[framei], cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(col_images[framei + 1], cv2.COLOR_BGR2GRAY)
            diff_image = cv2.absdiff(grayB, grayA)

            # plot the image after frame differencing
            # plt.imshow(diff_image, cmap='gray')
            # plt.title("subtraction of grayscale images")
            # plt.show()

            # image threshold -> 30
            ret, thresh = cv2.threshold(
                diff_image, 30, 255, cv2.THRESH_BINARY)

            # plot image after thresholding
            # plt.imshow(thresh, cmap='gray')
            # plt.title('thresholding')
            # plt.show()

            # smoothening of images
            kernel = np.ones((5, 5), np.uint8)
            dilated = cv2.dilate(thresh, kernel, iterations=1)

            # plot dilated image
            # plt.imshow(dilated, cmap='gray')
            # plt.title("smoothened")
            # plt.show()

            # find initial contours: gives multiple contours for one car
            contours, hierarchy = cv2.findContours(
                dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            valid_cntrs = []
            for i, cntr in enumerate(contours):
                x, y, w, h = cv2.boundingRect(cntr)
                if (y >= 600) & (cv2.contourArea(cntr) >= 1000):
                    valid_cntrs.append(cntr)

            dmy = col_images[framei+1].copy()
            dmy = cv2.line(dmy, (0, 500), (1280, 500), (100, 0, 0), 2)

            # filled rectangles (merged)
            img_merged_rect = np.zeros(dmy.shape)
            sorted_contours = sorted(
                valid_cntrs, key=cv2.contourArea, reverse=True)

            # merge all prev contours
            for cnt in sorted_contours:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img_merged_rect, (x, y),
                              (x+w, y+h), (0, 255, 0), -1)

            # cv2.imshow("colored",img_merged_rect)
            # cv2.waitKey()
            # conv to grayscale

            # count of discovered contours
            # print('len of valid contours', len(sorted_contours))

            img_float32 = np.float32(img_merged_rect)
            grey = img_float32.astype(np.uint8)
            grey = cv2.cvtColor(grey, cv2.COLOR_BGR2GRAY)

            # plt.title("grey scale image")
            # plt.imshow(grey)
            # cv2.waitKey()
            # find contours

            cntrs, hierarchy = cv2.findContours(
                grey.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            # mark contours
            merged = col_images[framei+1].copy()
            cv2.drawContours(merged, cntrs, -1, (0, 255, 0), 3)
            # cv2.imshow("merged",merged)
            # cv2.waitKey()

            for cnt in cntrs:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(merged, (x, y), (x+w, y+h), (0, 255, 0), 3)
                car = merged[y:y+h, x:x+w]
                # cv2.imshow("car",car)
                # cv2.waitKey()
                cv2.imwrite('output/extracted_vehicles/veh' +
                            str(veh_no)+'.jpg', car)
                veh_no += 1

            height, width, layers = dmy.shape
            size = (width, height)
            frame_array_for_video.append(merged)

            pathOut = 'vehicle_detection_video_compiled'+str(video_no)+'.mp4'

            # frames per second
            fps = 14.0
            out = cv2.VideoWriter(
                pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
            for i in range(len(frame_array_for_video)):
                # writing to a image array
                out.write(frame_array_for_video[i])
            out.release()

        return veh_no
