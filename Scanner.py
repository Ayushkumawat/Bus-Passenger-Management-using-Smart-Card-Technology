# Importing Labraries

import cv2
import pandas as pd
import openpyxl
from playsound import playsound
import time
from datetime import datetime

def quote(qot): # To Print The Process Executed
    try:
        print()
        print("|"*100)
        qon=(100-len(qot)-4)/2
        if qon.is_integer():print("|"*int(qon)+"  "+qot+"  "+"|"*int(qon))
        else:print("|"*(round(qon)+1)+"  "+qot+"  "+"|"*round(qon))
        print("|"*100)
    except:return

def scan(bus): # Scanning Function
    while True:
        try:
            _, img = cap.read()
            # detect and decode
            data, bbox, _ = detector.detectAndDecode(img)
            # check if there is a QRCode in the image
            if bbox is not None:
                # display the image with lines
                if data:
                    cod=list(bus['14-Digits Confidential ID'])
                    if cod.__contains__(data):
                        nam=list(bus["Name of Students"])
                        ind=cod.index(data)
                        per=nam[ind]
                        inn=list(bus["IN"])
                        out=list(bus["OUT"])
                        xlsx=openpyxl.load_workbook(pth)
                        sheet=xlsx.active                    
                        if int(hr)<12 and inn[ind]!="Y":
                            sheet['D'+str(ind+2)]="Y"
                            quote(per+" Has Boarded")
                            playsound('okay.mp3')
                        elif int(hr)>=12 and out[ind]!="Y":
                            sheet['E'+str(ind+2)]="Y"
                            quote(per+" Has Boarded")
                            playsound('okay.mp3')
                        else:
                            quote("This person has already boarded !")
                            playsound('access_denied.mp3')
                    else:
                        quote("Wrong QR code, please mind and check again !")
                        playsound('access_denied.mp3')
                    xlsx.save(pth)
                    bus=pd.read_excel(pth)
                    print()
            # display the result
            cv2.imshow("img", img)    
            if cv2.waitKey(1) == ord("q"):
                return
        except:
            quote("Wrong QR code, please mind and check again !")
            playsound('access_denied.mp3')

while True:
    hr,mi,se=datetime.now().strftime("%H:%M:%S").split(":")

    busn=input("Enter Bus Number : ").upper()
    if len(busn)>4:
        print("Invalid Bus Details !")
    else:
        # initalize the cam
        cap = cv2.VideoCapture(0)
        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()

        try:
            bn="Bus-" + busn
            pth=bn+".xlsx"
            bus=pd.read_excel(pth)
            print("SCANNING !")
            scan(bus)
            cap.release()
            cv2.destroyAllWindows()
        except:
            print("Bus number dosen't exists !")
            cap.release()
            cv2.destroyAllWindows()