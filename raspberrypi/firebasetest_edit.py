from firebase import firebase
import single_line_edit
import signal
from datetime import datetime
import time

firebase=firebase.FirebaseApplication('https://vahmac-43546.firebaseio.com/', None)

msg=""
a=0
b=0
c=0
d=0
rd=0
ht=0
newts=0
prevts=0
alert=""

while True:
    result=firebase.get('Commands','FromAndroid')
    if(msg!=result):
        print result
        msg=result
        reply=single_line_edit.find_function(result)
        firebase.put('/Commands','FromPi',reply)
    #warn user only once for ten minutes 
    if(rd==1):
        if((int(datetime.now().strftime('%H'))-a)*60+(int(datetime.now().strftime('%M'))-b)>=10):
            alert,rd=single_line_edit.rain_detection()
            a=int(datetime.now().strftime('%H'))
            b=int(datetime.now().strftime('%M'))
    else:
        alert,rd=single_line_edit.rain_detection()
        a=int(datetime.now().strftime('%H'))
        b=int(datetime.now().strftime('%M'))

    if(ht==1):
        if((int(datetime.now().strftime('%H'))-c)*60+(int(datetime.now().strftime('%M'))-d)>=10):
            alert,ht=single_line_edit.high_temperature()
            c=int(datetime.now().strftime('%H'))
            d=int(datetime.now().strftime('%M'))
    else:
        alert, ht=single_line_edit.high_temperature()
        a=int(datetime.now().strftime('%H'))
        b=int(datetime.now().strftime('%M'))

    if(len(alert)>1):
        firebase.put('/Commands','AlertPi',alert)

    alert, newts=single_line_edit.tank_status()
    print newts
    if(newts>0 and prevts!=newts):
            single_line_edit.send_message(alert)
            firebase.put('/Commands','AlertPi',alert)
    prevts=newts



