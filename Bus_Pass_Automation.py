# Importing Labraries
from tkinter import *
from tkinter import ttk
import pandas as pd
import os
import qrcode
import openpyxl
from PIL import Image,ImageTk,ImageDraw

win=Tk()
win.geometry("900x471")
win.minsize(900,471)

butn_pth=r"main_bg.png"
# set maximum window size value
win.maxsize(500, 400)
win.title("gui")

def options_page():
       
        filename5=PhotoImage(file=r"bg.png")
        background_lable15=Label(win,image=filename5)
        background_lable15.place(x=0,y=0)
        def back():
           
            options_page_b1.destroy()
            options_page_b2.destroy()
            options_page_b3.destroy()
            options_page_b4.destroy()
            options_page_b5.destroy()
            
            background_lable15.destroy()
            
        def fetch_QR():
            filename6=PhotoImage(file=butn_pth)
            background_lable16=Label(win,image=filename6)
            background_lable16.place(x=0,y=0)
            back()
            bus_No_entry2 = Entry(win,width = 35)
            bus_No_entry2.place(relx=0.55,rely=0.15+0.271,anchor="center")

            enrollement_entry3 = Entry(win,width = 35)
            enrollement_entry3.place(relx=0.55,rely=0.25+0.271,anchor="center")

            def back_to_options4():
                bus_No_entry2.destroy()
                
                fetch_QR_b1.destroy()
                fetch_QR_b2.destroy()
                fetch_QR_label1.destroy()
                fetch_QR_label2.destroy()
                enrollement_entry3.destroy()
                fetch_QR_label4.destroy()
                fetch_QR_label3.destroy()
                options_page()
            def qr_detail(): # To Fetch An Existing Person's QR
                        busn=bus_No_entry2.get().upper()
                        bn="Bus-" + busn
                        pth=bn+".xlsx"
                        if len(busn)>4 or len(busn)==0 or busn.isalpha() or busn.isnumeric() or os.path.exists(pth)==False:
                            fetch_QR_label4.config(text="Invalid bus")
                            fetch_QR_label4.config(fg="#ff0000")
                            return
                        bus=pd.read_excel(pth)
                        erp=list(bus["Enrollment number"])
                        cnf=list(bus["14-Digits Confidential ID"])
                        Enr=enrollement_entry3.get().upper()
                        if Enr.isalnum()==False or " " in Enr or (len(Enr)>14 and len(Enr)<7):
                             fetch_QR_label4.config(text="Enrollment Number Not valid !")
                             fetch_QR_label4.config(fg="#ff0000")
                             return
                        if erp.__contains__(Enr.upper()):
                            ind=erp.index(Enr)
                        else:
                            fetch_QR_label4.config(text="This enrollment does not exsist !")
                            fetch_QR_label4.config(fg="#ff0000")
                            return
                        img=qrcode.make(cnf[ind])
                        img.show()

                        fetch_QR_label4.config(text="QR Fetched Successfully")
                        fetch_QR_label4.config(fg="#00ff00")
                        bus_No_entry2.delete(0,END)
                        enrollement_entry3.delete(0,END)
                    
            fetch_QR_label3=Label(win,font=('Times New Roman',12,"bold"),text="Enrollment ID: ",borderwidth=0)
            fetch_QR_label3.place(relx=0.35,rely=0.25+0.271,anchor="center")

            fetch_QR_label4= Label(win,font=('helvetica',11,),text="",fg="#ff0000",borderwidth=0,border=0)
            fetch_QR_label4.place(relx=0.5,rely=0.32+0.3,anchor="center")
             
            fetch_QR_label1=Label(win,font=('Times New Roman',20,"bold"),text="Fetch QR",borderwidth=0)
            fetch_QR_label1.place(relx=0.5,rely=0.20,anchor="center")

            fetch_QR_label2=Label(win,font=('Times New Roman',12,"bold"),text="Bus No.: ",borderwidth=0)
            fetch_QR_label2.place(relx=0.36,rely=0.15+0.271,anchor="center")

            fetch_QR_b1=Button(win,text="Fetch QR",font=('Times New Roman',12,"bold"),width=12,bg="#f7f7f7",command=qr_detail)
            fetch_QR_b1.place(relx=0.7,rely=0.70,anchor="center")
                   
            fetch_QR_b2=Button(win,text="Back",font=('Times New Roman',12,"bold"),width=12,command=back_to_options4)
            fetch_QR_b2.place(relx=0.3,rely=0.70,anchor="center") 

            win.mainloop()
            
        def remove_bus():
            filename6=PhotoImage(file=butn_pth)
            background_lable16=Label(win,image=filename6)
            background_lable16.place(x=0,y=0)
            back()
            bus_No_entry1 = Entry(win,width = 35)
            bus_No_entry1.place(relx=0.55,rely=0.15+0.271,anchor="center")

            def back_to_options3():
                bus_No_entry1.destroy()
                
                remove_bus_b1.destroy()
                remove_bus_b2.destroy()
                remove_bus_label1.destroy()
                remove_bus_label2.destroy()
                remove_bus_label3.destroy()
                options_page()

            def remove_bus_details(): # To Remove An Existing Bus
                busn=bus_No_entry1.get().upper()
                try:
                    bn="Bus-"+busn
                    pth=bn+".xlsx"
                    os.remove(pth)
                    remove_bus_label3.config(text="FILE HAS BEEN REMOVED SUCESSFULLY")
                    remove_bus_label3.config(fg="#00ff00")
                    bus_No_entry1.delete(0,END)
                except:
                    remove_bus_label3.config(text="Details entered are invalid !")
                    remove_bus_label3.config(fg="#ff0000")   
                
            remove_bus_label3= Label(win,font=('helvetica',11,),text="",fg="#ff0000",borderwidth=0,border=0)
            remove_bus_label3.place(relx=0.5,rely=0.3+0.25,anchor="center")
            
            remove_bus_label1=Label(win,font=('Times New Roman',20,"bold"),text="Remove Bus",borderwidth=0)
            remove_bus_label1.place(relx=0.5,rely=0.20,anchor="center")

            remove_bus_label2=Label(win,font=('Times New Roman',12,"bold"),text="Bus No.: ",borderwidth=0)
            remove_bus_label2.place(relx=0.36,rely=0.15+0.271,anchor="center")

            remove_bus_b1=Button(win,text="Remove Bus",font=('Times New Roman',12,"bold"),width=12,command=remove_bus_details)
            remove_bus_b1.place(relx=0.7,rely=0.70,anchor="center")
                   
            remove_bus_b2=Button(win,text="Back",font=('Times New Roman',12,"bold"),width=12,command=back_to_options3)
            remove_bus_b2.place(relx=0.3,rely=0.70,anchor="center") 
            win.mainloop()
        def add_new_bus():
            filename6=PhotoImage(file=butn_pth)
            background_lable16=Label(win,image=filename6)
            background_lable16.place(x=0,y=0)
            back()
            bus_No_entry1 = Entry(win,width = 35)
            bus_No_entry1.place(relx=0.54,rely=0.15+0.271,anchor="center")

            def back_to_options2():
                bus_No_entry1.destroy()
                
                add_new_bus_b1.destroy()
                add_new_bus_b2.destroy()
                add_new_bus_label1.destroy()
                add_new_bus_label2.destroy()
                
                add_new_bus_label3.destroy()
                
                options_page()

            def add_bus_details():
                
                        busn=bus_No_entry1.get().upper()
                        bn="Bus-"+busn
                        pth=bn+".xlsx"
                        
                        if len(busn)>4 or len(busn)==0 or busn.isalpha() or busn.isnumeric() or os.path.exists(pth):
                            add_new_bus_label3.config(text="Invalid Bus Number !")
                            add_new_bus_label3.config(fg="#ff0000")
                            print()
                            return
                        
                        df = pd.DataFrame({"Name of Students":[],"Enrollment number":[],"14-Digits Confidential ID":[],"IN":[],"OUT":[]})
                        writer = pd.ExcelWriter(pth, engine='xlsxwriter')
                        df.to_excel(writer,index=False)
                        writer.close()
                        add_new_bus_label3.config(fg="#00ff00")
                        add_new_bus_label3.config(text="FILE HAS BEEN CREATED SUCESSFULLY")
                        bus_No_entry1.delete(0,END)
                   
            add_new_bus_label3= Label(win,font=('helvetica',11,),text="",fg="#ff0000",borderwidth=0,border=0)
            add_new_bus_label3.place(relx=0.5,rely=0.3+0.25,anchor="center")
            
            add_new_bus_label1=Label(win,font=('Times New Roman',20,"bold"),text="Add New Bus",borderwidth=0)
            add_new_bus_label1.place(relx=0.5,rely=0.20,anchor="center")

            add_new_bus_label2=Label(win,font=('Times New Roman',12,"bold"),text="Bus No.: ",borderwidth=0)
            add_new_bus_label2.place(relx=0.36,rely=0.15+0.271,anchor="center")
                   
            add_new_bus_b1=Button(win,text="Add Bus",font=('Times New Roman',12,"bold"),width=12,command=add_bus_details)
            add_new_bus_b1.place(relx=0.7,rely=0.70,anchor="center")
                   
            add_new_bus_b2=Button(win,text="Back",font=('Times New Roman',12,"bold"),width=12,command=back_to_options2)
            add_new_bus_b2.place(relx=0.3,rely=0.70,anchor="center") 
            win.mainloop()

        def remove_person():
            filename6=PhotoImage(file=butn_pth)
            background_lable16=Label(win,image=filename6)
            background_lable16.place(x=0,y=0)
            back()
            enrollement_entry1 = Entry(win,width = 35)
            enrollement_entry1.place(relx=0.58,rely=0.1+0.271,anchor="center")

            bus_entry1 = Entry(win,width = 35)
            bus_entry1.place(relx=0.58,rely=0.2+0.271,anchor="center")

            def back_to_options1():
                enrollement_entry1.destroy()
                
                remove_person_b1.destroy()
                remove_person_b2.destroy()
                remove_person_label1.destroy()
                remove_person_label2.destroy()
                remove_person_label3.destroy()
                bus_entry1.destroy()
                
                options_page()

            def remove_person_details():
                        busn=bus_entry1.get()
                        Enr=enrollement_entry1.get()
                    
                        bn="Bus-"+busn
                        pth=bn+".xlsx"
                        if Enr.isalnum()==False or " " in Enr or (len(Enr)>14 and len(Enr)<7):
                             remove_person_label4.config(text="Warning: This is not an enrollment number !")
                             remove_person_label4.config(fg="#ff0000")
                             return
                        else:
                            Enr=Enr.upper()
                        try:
                            bus=pd.read_excel(pth)
                        except:
                            remove_person_label4.config(text="Warning: this bus does not exist !")
                            remove_person_label4.config(fg="#ff0000")
                            return
                        
                        erp=list(bus["Enrollment number"])
                        Length=str(erp.index(str(Enr))+2)
                        xlsx = openpyxl.load_workbook(pth)     
                        sheet = xlsx.active                        
                        
                        remove_person_label4.config(text=list(bus["Name of Students"])[erp.index(str(Enr))]+"'s DETAILS HAS BEEN DELETED")
                        remove_person_label4.config(fg="#00ff00")
                        enrollement_entry1.delete(0,END)
                        bus_entry1.delete(0,END)

                        sheet['A'+Length]=""
                        sheet['B'+Length]=""
                        sheet['C'+Length]=""
                        xlsx.save(pth)

            remove_person_label4= Label(win,font=('helvetica',11,),text="",fg="#ff0000",borderwidth=0,border=0)
            remove_person_label4.place(relx=0.55,rely=0.3+0.3,anchor="center")
             
            remove_person_label1=Label(win,font=('Times New Roman',20,"bold"),text="Remove Person",borderwidth=0)
            remove_person_label1.place(relx=0.5,rely=0.20,anchor="center")

            remove_person_label2=Label(win,font=('Times New Roman',12,"bold"),text="Enrollment ID: ",borderwidth=0)
            remove_person_label2.place(relx=0.37,rely=0.1+0.271,anchor="center")

            remove_person_label3=Label(win,font=('Times New Roman',12,"bold"),text="BUS No.: ",borderwidth=0)
            remove_person_label3.place(relx=0.39,rely=0.2+0.271,anchor="center")

            remove_person_b1=Button(win,text="Remove",font=('Times New Roman',12,"bold"),width=12,command=remove_person_details)
            remove_person_b1.place(relx=0.7,rely=0.70,anchor="center")
                   
            remove_person_b2=Button(win,text="Back",font=('Times New Roman',12,"bold"),width=12,command=back_to_options1)
            remove_person_b2.place(relx=0.3,rely=0.70,anchor="center")
            
            win.mainloop()
            
        def add_person():
                   filename6=PhotoImage(file=butn_pth)
                   background_lable16=Label(win,image=filename6)
                   background_lable16.place(x=0,y=0)

                   back()                                                
                   name_entry = Entry(win,width = 35)
                   name_entry.place(relx=0.58,rely=0.1+0.271,anchor="center")

                   enrollement_entry = Entry(win,width = 35)
                   enrollement_entry.place(relx=0.58,rely=0.2+0.271,anchor="center")

                   bus_entry = Entry(win,width = 35)
                   bus_entry.place(relx=0.58,rely=0.3+0.271,anchor="center")
                   def back_to_options():
                       enrollement_entry.destroy()
                       name_entry.destroy()
                       add_person_page_b1.destroy()
                       add_person_page_b2.destroy()
                       add_person_page_label1.destroy()
                       add_person_page_label2.destroy()
                       add_person_page_label3.destroy()
                       name_entry.destroy()
                       bus_entry.destroy()
                       add_person_page_label4.destroy()
                       add_person_page_lable5.destroy()
                       options_page()
                    
                   def add_Person_details():     
                            busn=bus_entry.get()
                            
                            Name=name_entry.get()
                            Enr=enrollement_entry.get()
                            
                            print(len(busn))
                            if len(Name.strip().split())==1 or Name.replace(" ","").isalpha()==False:
                                add_person_page_lable5.config(text="Warning: This is not a valid full name, Please try again !")
                                add_person_page_lable5.config(fg="#ff0000")
                                return
                            if Enr.isalnum()==False or " " in Enr or (len(Enr)>14 and len(Enr)<7):
                                add_person_page_lable5.config(text="Warning: This is not an enrollment number !")
                                add_person_page_lable5.config(fg="#ff0000")
                                return

                            bn="Bus-"+busn
                            pth=bn+".xlsx"
                            
                            if " " in busn or busn.isalnum()==False or busn=="":
                                add_person_page_lable5.config(text="Warning: Wrong bus number")
                                add_person_page_lable5.config(fg="#ff0000")
                                return
                            try:
                                bus=pd.read_excel(pth)
                            except:
                                add_person_page_lable5.config(text="Warning: Bus does not exist!")
                                add_person_page_lable5.config(fg="#ff0000")
                                return
                            
                            erp=list(bus["Enrollment number"])
                            if erp.__contains__(Enr.upper()):
                                add_person_page_lable5.config(text="Warning: This enrollment number is already registered !")
                                add_person_page_lable5.config(fg="#ff0000")
                                return

                            Length=str(len(erp)+2)
                            xlsx=openpyxl.load_workbook(pth)
                            sheet=xlsx.active
                                
                            sheet['A'+Length]=Name.strip().title()
                            sheet['B'+Length]=Enr.upper()
                            
                            ID=Enr[::-1][:4]+Name.split(" ")[0][0]+Name.split(" ")[1][0]+Enr[2:5]
                            sheet['C'+Length]=ID
                            xlsx.save(pth)
                            
                            add_person_page_lable5.config(text=Name+"'s DETAILS HAS BEEN SAVED SUCCESSFULLY")
                            add_person_page_lable5.config(fg="#00ff00")
                            name_entry.delete(0,END)
                            enrollement_entry .delete(0,END)
                            bus_entry.delete(0,END)
                            
                   add_person_page_lable5=Label(win,font=('helvetica',11,),text="",fg="#ff0000",borderwidth=0,border=0)
                   add_person_page_lable5.place(relx=0.55,rely=0.3+0.35,anchor="center")
                   
                   add_person_page_label1=Label(win,font=('Times New Roman',20,"bold"),text="Add Person",borderwidth=0)
                   add_person_page_label1.place(relx=0.5,rely=0.20,anchor="center")

                   add_person_page_label2=Label(win,font=('Times New Roman',12,"bold"),text="Name: ",borderwidth=0)
                   add_person_page_label2.place(relx=0.40,rely=0.1+0.271,anchor="center")

                   add_person_page_label3=Label(win,font=('Times New Roman',12,"bold"),text="Enrollment ID: ",borderwidth=0)
                   add_person_page_label3.place(relx=0.37,rely=0.2+0.271,anchor="center")

                   add_person_page_label4=Label(win,font=('Times New Roman',12,"bold"),text="Bus Number: ",borderwidth=0)
                   add_person_page_label4.place(relx=0.37,rely=0.3+0.271,anchor="center")
                   
                   add_person_page_b1=Button(win,text="Add",font=('Times New Roman',12,"bold"),width=12,command=add_Person_details)
                   add_person_page_b1.place(relx=0.7,rely=0.75,anchor="center")
                   
                   add_person_page_b2=Button(win,text="Back",font=('Times New Roman',12,"bold"),width=12,command=back_to_options)
                   add_person_page_b2.place(relx=0.3,rely=0.75,anchor="center") 
                   win.mainloop()
        
        def Back_to_main_page():
            back()
        
        options_page_b1=Button(win,text="Add Person",font=('Times New Roman',13,"bold"),width=11,bg="#f7f7f7",command=add_person)
        options_page_b1.place(relx=0.13,rely=0.55,anchor="center")

        options_page_b2=Button(win,text="Add Bus",font=('Times New Roman',13,"bold"),width=11,bg="#f7f7f7",command=add_new_bus)
        options_page_b2.place(relx=0.31,rely=0.55,anchor="center")

        options_page_b3=Button(win,text="Remove Bus",font=('Times New Roman',13,"bold"),width=11,bg="#f7f7f7",command=remove_bus)
        options_page_b3.place(relx=0.51,rely=0.55,anchor="center")

        options_page_b4=Button(win,text="Delete Person",font=('Times New Roman',13,"bold"),width=11,bg="#f7f7f7",command=remove_person)
        options_page_b4.place(relx=0.69,rely=0.55,anchor="center")

        options_page_b5=Button(win,text="Fetch QR",font=('Times New Roman',13,"bold"),width=11,bg="#f7f7f7",command=fetch_QR)
        options_page_b5.place(relx=0.87,rely=0.55,anchor="center")

        win.mainloop()

options_page()