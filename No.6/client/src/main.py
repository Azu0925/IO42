import drive
import os
import datetime
import camera

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    file_name = 'test_' + str(datetime.datetime.now()) + '.m4v'
    file_info = os.path.normpath(os.path.join(base, '../video/' + file_name))
    
    # recording
    camera.record(file_info)

    # upload to Google drive
    drive.upload(file_info, file_name)

if __name__ == '__main__':
    main()