import datetime

def record(file_path, cv2, cap):
    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = 20.0
    size = (640, 360)
    limit = datetime.datetime.now() + datetime.timedelta(seconds=10)
    writer = cv2.VideoWriter(file_path, fmt, fps, size)

    while True:
        _, frame = cap.read()
        frame = cv2.resize(frame, size)
        writer.write(frame)

        if datetime.datetime.now() >= limit:
            break
    
    writer.release()
