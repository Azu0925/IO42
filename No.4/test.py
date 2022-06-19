# coding: utf-8
from curses.ascii import alt
import RPi.GPIO as GPIO
import spidev
import time
import sys

# GPIO
SwitchPIN = 22
switchINPUT = 0
LEDPIN = 23
LEDPIN2 = 24
LEDPIN3 = 25

# flag
altFlag = False
momFlag = False
mode = False

# 時間設定(固定値)
highTime = 30
lowTime = 20

# time = 0.0

# ディレイ時間設定
# highTime = int(input("オンディレイの時間を入力："))
# lowTime = int(input("オフディレイの時間を入力："))

pushTime = 0
noPushTime = lowTime

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN,GPIO.OUT)
GPIO.setup(LEDPIN2,GPIO.OUT)
GPIO.setup(LEDPIN3,GPIO.OUT)
GPIO.output(LEDPIN,GPIO.LOW)
GPIO.output(LEDPIN2,GPIO.LOW)
GPIO.output(LEDPIN3,GPIO.LOW)
GPIO.setup(SwitchPIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# 開始前合図
print("オンディレイ："+str(highTime)+"s")
print("オフディレイ："+str(lowTime)+"s")
# time.sleep(1)
# for num in range(3,0,-1):
#     print(num)
#     time.sleep(1)
print("start!!!\nボタンを押してね＾＾")

try:
    while True:
        # ボタンの状態取得
        switchINPUT = GPIO.input(SwitchPIN)
        log = ""
        timeLog = ""
        
        # プッシュ時間計測
        time.sleep(0.1)
        if(switchINPUT):
            pushTime = pushTime + 1
            noPushTime = lowTime
            timeLog = str(pushTime)+"ms"
        else:
            if(momFlag == True):
                noPushTime = noPushTime - 1
            pushTime = 0
            if(noPushTime == 0):
                momFlag = False
                mode = False
            elif(noPushTime < 0):
                noPushTime = lowTime
        
        # 処理
        if(pushTime != 0 and not(mode)):
            if(pushTime >= highTime and altFlag):
                altFlag = False
                momFlag = True
                mode = True
                log = "「オフディレイモード」\nmom_high alt_low ["+timeLog+"]"
                # print(log)
            elif(pushTime >= highTime and not(altFlag)):
                altFlag = True
                momFlag = True
                mode = True
                log = "「オンディレイモード」\nmom_high alt_high ["+timeLog+"]"

        # 実行
        # ソフトの制御
        # オルタネイト
        if(altFlag == True):
            GPIO.output(LEDPIN , GPIO.HIGH)
        else:
            GPIO.output(LEDPIN , GPIO.LOW)
        # モーメンタリ
        if(momFlag == True):
            GPIO.output(LEDPIN2 , GPIO.HIGH)
        else:
            GPIO.output(LEDPIN2 , GPIO.LOW)
        # ボタンの制御
        if(switchINPUT):
            GPIO.output(LEDPIN3,GPIO.HIGH)
        else:
            GPIO.output(LEDPIN3,GPIO.LOW)
        
        # # プッシュ経過時間ログ
        # if(timeLog != "" and not(momFlag)):
        #     print("押してる：残り時間"+timeLog)
        # elif(noPushTime != 0):
        #     print("離してる：残り時間"+noPushTime)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("終了")
    sys.exit()