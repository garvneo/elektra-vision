import speech_recognition as sr
import pyttsx3
import os
import cv2
from imutils.video import VideoStream
import time
import pyttsx
import threading
import sys
import urllib3
#import RPi.GPIO as GPIO
from multiprocessing import Process
voice_command=False
on=True
r = sr.Recognizer()
#GPIO.setmode(GPIO.BCM)
#set GPIO Pins
#GPIO_TRIGGER = 18
#GPIO_ECHO = 24
#set GPIO direction (IN / OUT)
#GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#GPIO.setup(GPIO_ECHO, GPIO.IN)

def btn_intrupt():
    global mode
    mode=1
    global button_pressed
    button_pressed=True
    try:
        while button_pressed:
            #input_state=GPIO.input(26)
            #if input_state==False:
            #print_lcd("Voice Mode","")
                    say("Give command please")
                    with sr.Microphone() as source:
                        print("say something")
                        audio = r.listen(source)
                    # Speech recognition using Google Speech Recognition
                    try:
                        out = r.recognize_google(audio)
                        print(out)
                        if out=="switch on the fan":
                            say("you said switch on the fan")
                        elif out=="switch on the light":
                            say("you said switch on the light")
                        elif out=="switch off the light":
                            say("you said switch off the light")
                        elif out == "switch off the fan":
                            say("you said switch off the fan")
                        elif out == "activate object mode":
                            say("object mode activated")
                            mode = 0
                        elif out == "activate distance mode":
                            say("distance mode activated")
                            mode = 2

                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        say("Sorry say again")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                        say("Sorry say again")
                    audio=None
                    button_pressed=False
                    time.sleep(1)
    except Exception as e:
        print(e.message)
        #GPIO.cleanup()
        sys.exit(0)



def object_detection():
    try:
        print("Starting Object Detection Mode")
        # start the video stream thread
        print("[INFO] starting video stream thread...")
        vs = VideoStream(src=0).start()
        # vs = VideoStream(usePiCamera=True).start()
        time.sleep(1.0)
        while True:
            if mode == 0:
                time.sleep(3)
                frame = vs.read()
                #frame = imutils.resize(frame, width=450)
                face = detect_face(frame)
                if (len(face) != 0):
                    #draw_rectangle(frame,face)
                    out=str(len(face))+" face detected successfully."
                    print(out)
                    say(out)
                time.sleep(1)
                cars = detect_car(frame)
                if (len(cars) != 0):
                    #draw_rectangle(frame,cars)
                    out=str(len(cars))+" car detected successfully."
                    print(out)
                    say(out)

        vs.stop()
    except Exception as e:
        print(e.message)


def draw_rectangle(img, rects):
    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

def say(out):
    try:
        threading.Thread(target=sayout, args=(out,)).start()
    except Exception as e:
        print(e.message)

def sayout(out):
    try:
        engine = pyttsx.init()
        engine.say(out)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("hello")

def detect_car(img):
    # convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # load OpenCV face detector, I am using LBP which is fast
    # there is also a more accurate but slow Haar classifier
    face_cascade = cv2.CascadeClassifier('cascade_classifier/car3.xml')

    # let's detect multiscale (some images may be closer to camera than others) images
    # result is a list of faces
    fruits = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    # return only the face part of the image
    return fruits

def detect_face(img):
    # convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # load OpenCV face detector, I am using LBP which is fast
    # there is also a more accurate but slow Haar classifier
    face_cascade = cv2.CascadeClassifier('cascade_classifier/haarcascade_frontalface_alt.xml')

    # let's detect multiscale (some images may be closer to camera than others) images
    # result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    # return only the face part of the image
    return faces


def http_connection(url):
    response = manager.request('GET',url)
    print(response.status)

def distance_mode():
    try:
        while True:
            if mode==2:
                #dist = distance()
                print("distance mode")
                #print ("Measured Distance = %.1f cm" % dist)
                time.sleep(1)

                #Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        #GPIO.cleanup()


def distance():
    distance=0
    print(distance)
    # set Trigger to HIGH
    #GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    #GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
   # while GPIO.input(GPIO_ECHO) == 0:
        #StartTime = time.time()

    # save time of arrival
    #while GPIO.input(GPIO_ECHO) == 1:
        #StopTime = time.time()

    # time difference between start and arrival
    #TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    #distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    manager = urllib3.PoolManager()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key/get-set-fuel-51c090999504.json"
    t2 = threading.Thread(target=btn_intrupt, args=())
    t2.start()
    t1 = threading.Thread(target=object_detection, args=())
    t1.start()
    #t3 = threading.Thread(target=distance_mode, args=())
    #t3.start()

