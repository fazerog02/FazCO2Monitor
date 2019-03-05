import time, os, schedule, serial
from django.utils import timezone


token = 'yourRestframeworkJwtToken'
counter = 60

def getPPM():
    GET = [0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x79]

    ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=0.1)

    ser.write(bytearray(GET))
    res = ser.read(9)
    res = bytearray(res)

    checkSum = 0xff & (~(res[1] + res[2] + res[3] + res[4] + res[5] + res[6] + res[7]) + 1)

    ser.close()

    if res[8] == checkSum:
        ppm = (res[2] << 8) | res[3]
        return ppm
    else:
        print("error! checkSum is " + str(checkSum))
        return -1

def sendPPM():
    global counter
    value = getPPM()
    url = 'http://runningServerAdress/api/nowppm/1/'
    apiCommand = "curl -X PUT " + url + " -d \"value=" + str(value) + "\"" + " -H \"Authorization: JWT " + token + "\""
    os.system(apiCommand)
    counter += 1
    if counter >= 60:
        url = 'http://runningServerAdress/api/ppmdata/'
        date = timezone.datetime.now()
        apiCommand = "curl -X POST " + url + " -d \"value=" + str(value) + "\" -d \"date=" + str(date) + "\"" + " -H \"Authorization: JWT " + token + "\""
        os.system(apiCommand)
        counter = 0

sendPPM()
schedule.every(10).seconds.do(sendPPM)

while True:
    schedule.run_pending()
    time.sleep(1)
