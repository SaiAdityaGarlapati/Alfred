import time
import RPi.GPIO as gpio
import string
import smtplib
import Adafruit_DHT
from twilio.rest import Client
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
account_sid="ACdd50eb2196ea24e697f92d902c7cee44"
auth_token="c2d8c3086a158096d70bbe79618a6d96"


gpio.setwarnings (False)
gpio.setmode(gpio.BCM)
#set pins
gpio.setup(17,gpio.OUT) #B1.L
gpio.setup(27,gpio.OUT) #B1.F
gpio.setup(22,gpio.OUT) #B1.TV
gpio.setup(5,gpio.OUT)  #B2.L
gpio.setup(6,gpio.OUT)  #B2.F
gpio.setup(13,gpio.OUT) #B2.TV
gpio.setup(16,gpio.OUT) #B3.L
gpio.setup(20,gpio.OUT) #B3.F
gpio.setup(21,gpio.OUT) #B3.TV
global humidity1, temperature1, humidity2, temperature2, humidity3, temperature3

# Software SPI configuration for MCP3008:
CLK  = 25
MISO = 8
MOSI = 7
CS   = 12
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def LightON(user,msg):
    if(user.find('all')!=-1 or user.find('everything')!=-1 or ((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1))):
        gpio.output(17, gpio.HIGH)
        gpio.output(5, gpio.HIGH)
        gpio.output(16, gpio.HIGH)
        reply='All the light\'s have been tuned ON'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1)):
        gpio.output(17, gpio.HIGH)
        gpio.output(5, gpio.HIGH)
        reply='Light\'s have been turned ON in room one and two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1)):
        gpio.output(5, gpio.HIGH)
        gpio.output(16, gpio.HIGH)
        reply= 'Light\'s has been turned ON in room two and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('third')!=-1 or user.find('three')!=-1) and (user.find('one')!=-1 or user.find('first')!=-1)):
        gpio.output(16, gpio.HIGH)
        gpio.output(17, gpio.HIGH)
        reply='Light\'s have been turned ON in room one and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('one')!=-1 or user.find('first')!=-1):
        gpio.output(17, gpio.HIGH)
        reply='Light has been turned ON in room one'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1):
        gpio.output(5, gpio.HIGH)
        reply= 'Light has been turned ON in room two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('third')!=-1 or user.find('three')!=-1):
        gpio.output(16, gpio.HIGH)
        reply='Light has been turned ON in room three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    else:
        msg= 'Sorry Master, I did\'nt get that. Can you please specify the room?'
    return msg

def LightOFF(user,msg):
    if(user.find('all')!=-1 or user.find('everything')!=-1 or ((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1))):
        gpio.output(17, gpio.LOW)
        gpio.output(5, gpio.LOW)
        gpio.output(16, gpio.LOW)
        reply='All the light\'s have been tuned OFF'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1)):
        gpio.output(17, gpio.LOW)
        gpio.output(5, gpio.LOW)
        reply='Light\'s have been turned OFF in room one and two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1)):
        gpio.output(5, gpio.LOW)
        gpio.output(16, gpio.LOW)
        reply= 'Light\'s has been turned OFF in room two and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('third')!=-1 or user.find('three')!=-1) and (user.find('one')!=-1 or user.find('first')!=-1)):
        gpio.output(16, gpio.LOW)
        gpio.output(17, gpio.LOW)
        reply='Light\'s have been turned OFF in room one and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('one')!=-1 or user.find('first')!=-1):
        gpio.output(17, gpio.LOW)
        reply='Light has been turned OFF in room one'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1):
        gpio.output(5, gpio.LOW)
        reply= 'Light has been turned OFF in room two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('third')!=-1 or user.find('three')!=-1):
        gpio.output(16, gpio.LOW)
        reply='Light has been turned OFF in room three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    else:
        msg= 'Sorry Master, I did\'nt get that. Can you please specify the room?'
    return msg


def FanON(user,msg):
    if(user.find('all')!=-1 or user.find('everything')!=-1 or ((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1))):
        gpio.output(27, gpio.HIGH)
        gpio.output(6, gpio.HIGH)
        gpio.output(20, gpio.HIGH)
        reply='All the fan\'s have been tuned ON'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1)):
        gpio.output(27, gpio.HIGH)
        gpio.output(6, gpio.HIGH)
        reply='Fan\'s have been turned ON in room one and two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1)):
        gpio.output(6, gpio.HIGH)
        gpio.output(20, gpio.HIGH)
        reply= 'Fan\'s has been turned ON in room two and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1)):
        gpio.output(27, gpio.HIGH)
        gpio.output(20, gpio.HIGH)
        reply= 'Fan\'s has been turned ON in room one and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('one')!=-1 or user.find('first')!=-1):
        gpio.output(27, gpio.HIGH)
        reply='Fan has been turned ON in room one'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1):
        gpio.output(6, gpio.HIGH)
        reply= 'Fan has been turned ON in room two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('third')!=-1 or user.find('three')!=-1):
        gpio.output(20, gpio.HIGH)
        reply='Fan has been turned ON in room three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    else:
        msg= 'Sorry Master, I did\'nt get that. Can you please specify the room?'
    return msg

def FanOFF(user,msg):
    if(user.find('all')!=-1 or user.find('everything')!=-1 or ((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1))):
        gpio.output(27, gpio.LOW)
        gpio.output(6, gpio.LOW)
        gpio.output(20, gpio.LOW)
        reply='All the fan\'s have been tuned OFF'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1)):
        gpio.output(27, gpio.LOW)
        gpio.output(6, gpio.LOW)
        reply='Fan\'s have been turned OFF in room one and two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1)):
        gpio.output(6, gpio.LOW)
        gpio.output(20, gpio.LOW)
        reply= 'Fan\'s has been turned OFF in room two and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('third')!=-1 or user.find('three')!=-1) and (user.find('one')!=-1 or user.find('first')!=-1)):
        gpio.output(27, gpio.LOW)
        gpio.output(20, gpio.LOW)
        reply='Fan\'s have been turned OFF in room one and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('one')!=-1 or user.find('first')!=-1):
        
        gpio.output(27, gpio.LOW)
        reply='Fan has been turned OFF in room one'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1):
        gpio.output(6, gpio.LOW)
        reply= 'Fan has been turned OFF in room two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('third')!=-1 or user.find('three')!=-1):
        gpio.output(20, gpio.LOW)
        reply='Fan has been turned OFF in room three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    else:
        msg= 'Sorry Master, I did\'nt get that. Can you please specify the room?'
    return msg


def TVON(user,msg):
    if(user.find('all')!=-1 or user.find('everything')!=-1 or ((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1))):
        gpio.output(22, gpio.HIGH)
        gpio.output(13, gpio.HIGH)
        gpio.output(21, gpio.HIGH)
        reply='All the TV\'s have been tuned ON'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1)):
        gpio.output(22, gpio.HIGH)
        gpio.output(13, gpio.HIGH)
        reply='TV\'s have been turned ON in room one and two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1)):
        gpio.output(13, gpio.HIGH)
        gpio.output(21, gpio.HIGH)
        reply= 'TV\'s has been turned ON in room two and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1)):
        gpio.output(22, gpio.HIGH)
        gpio.output(21, gpio.HIGH)
        reply= 'TV\'s has been turned ON in room two and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('one')!=-1 or user.find('first')!=-1):
        gpio.output(22, gpio.HIGH)
        reply='TV has been turned ON in room one'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    
    elif(user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1):
        gpio.output(13, gpio.HIGH)
        reply= 'TV has been turned ON in room two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('third')!=-1 or user.find('three')!=-1):
        gpio.output(21, gpio.HIGH)
        reply='TV has been turned ON in room three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    else:
        msg= 'Sorry Master, I did\'nt get that. Can you please specify the room?'
    return msg

def TVOFF(user,msg):
    if(user.find('all')!=-1 or user.find('everything')!=-1 or ((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1))):
        gpio.output(22, gpio.LOW)
        gpio.output(13, gpio.LOW)
        gpio.output(21, gpio.LOW)
        reply='All the TV\'s have been tuned OFF'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('one')!=-1 or user.find('first')!=-1) and (user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1)):
        gpio.output(22, gpio.LOW)
        gpio.output(13, gpio.LOW)
        reply='TV\'s have been turned OFF in room one and two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1) and (user.find('third')!=-1 or user.find('three')!=-1)):
        gpio.output(13, gpio.LOW)
        gpio.output(21, gpio.LOW)
        reply= 'TV\'s has been turned OFF in room two and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif((user.find('third')!=-1 or user.find('three')!=-1) and (user.find('one')!=-1 or user.find('first')!=-1)):
        gpio.output(22, gpio.LOW)
        gpio.output(21, gpio.LOW)
        reply='TV\'s have been turned OFF in room one and three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('one')!=-1 or user.find('first')!=-1):
        gpio.output(22, gpio.LOW)
        reply='TV has been turned OFF in room one'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    
    elif(user.find('two')!=-1 or user.find('secound')!=-1 or user.find('second')!=-1):
        gpio.output(13, gpio.LOW)
        reply= 'TV has been turned OFF in room two'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    elif(user.find('third')!=-1 or user.find('three')!=-1):
        gpio.output(21, gpio.LOW)
        reply='TV has been turned OFF in room three'
        if(len(msg)>1):
            msg=msg+', '+reply
        else:
            msg=reply
    else:
        msg= 'Sorry Master, I did\'nt get that. Can you please specify the room?'
    return msg

def ON(user,reply):
    x=0
    if(user.find('light')!=-1 or user.find('lights')!=-1):
        reply=LightON(user,reply)
        x=1
    if(user.find('fan')!=-1 or user.find('fans')!=-1):
        reply=FanON(user,reply)
        x=1
    if(user.find('television')!=-1 or user.find('TV')!=-1 or user.find('televisions')!=-1):
        reply=TVON(user,reply)
        x=1
    if(x!=1):
        if(user.find('everything')!=-1 or user.find('all')!=-1):
            reply=LightON(user,reply)
            reply=FanON(user,reply)
            reply=TVON(user,reply)
        else:
            reply="Sorry Master, couldnt find the device you are looking for"
    return reply

def OFF(user,reply):
    x=0
    if(user.find('light')!=-1 or user.find('lights')!=-1):
        reply=LightOFF(user,reply)
        x=1
    if(user.find('fan')!=-1 or user.find('fans')!=-1):
        reply=FanOFF(user,reply)
        x=1
    if(user.find('television')!=-1 or user.find('TV')!=-1 or user.find('televisions')!=-1):
        reply=TVOFF(user,reply)
        x=1
    if(x==0):
        if(user.find('everything')!=-1 or user.find('all')!=-1):
            reply=LightOFF(user,reply)
            reply=FanOFF(user,reply)
            reply=TVOFF(user,reply)
        else:
            reply="Sorry Master, couldnt find the device you are looking for"
    
    return reply

def temperature(user): 
    if(user.find('one')!=-1):
        humidity1, temperature1 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 18)
        if humidity1 is not None and temperature1 is not None:
            reply= ('Temperature in room one is {0:0.1f}*C'.format(temperature1))
        else:
            reply= ('Failed to get reading in room one. Try again!')
    if(user.find('two')!=-1):
        humidity2, temperature2 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
        if humidity2 is not None and temperature2 is not None:
            reply= ('Temperature in room two is {0:0.1f}*C'.format(temperature2))
        else:
            reply= ('Failed to get reading in room two. Try again!')
    if(user.find('three')!=-1):
        humidity3, temperature3 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 19)
        if humidity3 is not None and temperature3 is not None:
            reply= ('Temperature in room three is {0:0.1f}*C'.format(temperature3))
        else:
            reply= ('Failed to get reading in room three. Try again!')
    return reply


def send_message(text):
    client= Client(account_sid, auth_token)
    client.messages.create(to='+918800568420', from_=+15097743039, body=text)


def high_temperature():
    ht=1
    text=""
    humidity1, temperature1 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 18)
    humidity2, temperature2 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    humidity3, temperature3 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 19)
    if(temperature1>wt and temperature2>wt and temperature3>wt):
        text= "high temperatures are detected in all the rooms"
        send_message(text)
    elif(temperature1>wt and temperature2>wt):
        text= "high temperatures are detected in room one and two"
        send_message(text)
    elif(temperature2>wt and temperature3>wt):
        text= "high temperatures are detected in room two and three"
        send_message(text)
    elif(temperature3>wt and temperature1>wt):
        text= "high temperatures are detected in room one and three"
        send_message(text)
    elif(temperature1>wt):
        text= "high temperature is detected in room one"
        send_message(text)
    elif(temperature2>wt):
        text= "high temperature is detected in room two"
        send_message(text)
    elif(temperature3>wt):
        text= "high temperature is detected in room three"
        send_message(text)
    else:
        ht=0 #ht toggled to zero when no high temperatures are detected
    return text, ht
    

def rain_detection():
    text=""
    rd=1
    rl=mcp.read_adc(0)
    if(rl>250 and rl<900):
        text= "light rainfall detected on terrace"
    elif (rl<=250):
        text= "Heavy rainfall detected on terrace"
    else:
        rd=0 #rd is toggled to zero when no rain is detected
    if(rd==1):
        send_message(text)
    return text, rd

def water_tank_alert(PrevStatus):
    text=""
    text,NewStatus=tank_status()
    if(NewStatus>0):
        if(PrevStatus!=NewStatus):
            send_message(text)
    return text, NewStatus

def tank_status():
    top=mcp.read_adc(6)
    bottom=mcp.read_adc(7)
    ts=-1
    reply="unnable to get watertank status"
    if((bottom>30) and (top>30)):
        ts=1
        reply= "water tank is full"
    elif((bottom>30) and (top<=30)):
        ts=0
        reply= "water tank is neither full not empty"
    else:
        ts=2
        reply= "water tank is empty"
    return reply, ts


def find_function(user):
    user=user+" "
    reply= ""
    if(user.find('on ')!=-1):
        reply=ON(user,reply)
    elif(user.find('off')!=-1):
        reply=OFF(user,reply)
    elif(user.find('temperature')!=-1):
        reply= temperature(user)
    elif(user.find('tank')!=1):
        reply,ts=tank_status()
    else:
        reply= 'Sorry Master, I did\'nt get that'
    return reply


#Main Body
#initialisation of gpio pins
gpio.output(17, gpio.LOW)
gpio.output(27, gpio.LOW)
gpio.output(22, gpio.LOW)
gpio.output(5, gpio.LOW)
gpio.output(6, gpio.LOW)
gpio.output(13, gpio.LOW)
gpio.output(16, gpio.LOW)
gpio.output(20, gpio.LOW)
gpio.output(21, gpio.LOW)
global wt  #warning temperature is set as 45 degree celsius
wt=45
#temperature1=46
#temperature2=40
#temperature3=50



