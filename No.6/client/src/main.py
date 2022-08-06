import upload
import os

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    upload.upload(os.path.normpath(os.path.join(base, '../sample.mp4')), 'sample.mp4')

if __name__ == '__main__':
    main()