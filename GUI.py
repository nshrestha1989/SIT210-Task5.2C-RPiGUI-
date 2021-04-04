from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##hardware
ledGreen=LED(14)
ledBlue=LED(15)
ledRed=LED(18)

##GUI DEFINITIONS##
win=Tk()
win.title("Led Toggler")

myFont=tkinter.font.Font(family='Helvetica',size=12,weight="bold")

##EVENT FUNCTION##
def ledToggleGreen():
	if ledGreen.is_lit:
	    ledGreen.off()
	    ledButton["text"]="Turn Green Led on"
	
	else:
	   ledGreen.on()
	   ledButton["text"]="Turn Green Led off"
def ledToggleBlue():	   
	if ledBlue.is_lit:
	    ledBlue.off()
	    ledButton["text"]="Turn Blue Led on"
	
	else:
	   ledBlue.on()
	   ledButton["text"]="Turn blue Led off"

def ledToggleRed():	   
	if ledRed.is_lit:
	    ledRed.off()
	    ledButton["text"]="Turn Red Led on"
	
	else:
	   ledRed.on()
	   ledButton["text"]="Turn blue Led off" 


def close():
    RPi.GPIO.cleanup()
    win.destroy()
##WIDGETS###
ledButton=Button(win,text='Turn Green LED on',font=myFont,command=ledToggleGreen,bg='bisque2',height=1,width=24)

ledButton.grid(row=0,column=1)

ledButton=Button(win,text='Turn Blue LED on',font=myFont,command=ledToggleBlue,bg='bisque2',height=1,width=24)

ledButton.grid(row=1,column=1)

ledButton=Button(win,text='Turn Red LED on',font=myFont,command=ledToggleRed,bg='bisque2',height=1,width=24)

ledButton.grid(row=2,column=1)

exitButton=Button(win,text='Exit',font=myFont,command=close,bg='red',height=1,width=6)
exitButton.grid(row=3,column=1)

win.protocol("WM_DELETE_WINDOW",close)#exit clean

win.mainloop() #loop forever


