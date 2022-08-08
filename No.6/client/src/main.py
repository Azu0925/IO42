from fileinput import filename
import drive
import os
import cv2
import datetime

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    cap = cv2.VideoCapture(0)
    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = 20.0
    size = (640, 360)
    file_name = 'test_' + str(datetime.datetime.now()) + '.m4v'
    file_info = os.path.normpath(os.path.join(base, '../video/' + file_name))
    writer = cv2.VideoWriter(file_info, fmt, fps, size)
    limit = datetime.datetime.now() + datetime.timedelta(seconds=10)
    
    while True:
        _, frame = cap.read()
        frame = cv2.resize(frame, size)
        writer.write(frame)
        # cv2.imshow('frame', frame)

        if datetime.datetime.now() >= limit:
            break
    
    writer.release()
    cap.release()
    cv2.destroyAllWindows()

    # upload to Google drive
    drive.upload(file_info, file_name)

if __name__ == '__main__':
    main()