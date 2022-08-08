import drive
import os
import datetime
import camera
import cv2

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    file_name = 'test_' + str(datetime.datetime.now()) + '.m4v'
    file_info = os.path.normpath(os.path.join(base, '../video/' + file_name))

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    DELTA_MAX = 255
    DOT_TH = 20
    MOTION_FACTOR_TH = 0.20
    avg = None
    
    while True:
        _, frame = cap.read()
        motion_detected = False
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if avg is None:
            avg = gray.copy().astype('float')
            continue
            
        cv2.accumulateWeighted(gray, avg, 0.6)
        frame_delta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))

        thresh = cv2.threshold(frame_delta, DOT_TH, DELTA_MAX, cv2.THRESH_BINARY)[1]

        motion_factor = thresh.sum() * 1.0 / thresh.size / DELTA_MAX

        if motion_factor > MOTION_FACTOR_TH:
            motion_detected = True
            print("log: motion_detected True")

        if motion_detected == True:
            print("log: recording start")
            
            # recording
            camera.record(file_info, cv2, cap)

            # upload to Google drive
            drive.upload(file_info, file_name)
            print("log: movie upload done")

        cv2.imshow('camera', frame)

        k = cv2.waitKey(1000)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    #camera.record(file_info)


if __name__ == '__main__':
    main()