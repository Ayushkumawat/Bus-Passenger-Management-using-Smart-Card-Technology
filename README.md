# Bus Passenger Management using Smart Card Technology

# Problem-Domain:
Over the last few decades, there has been an increase in the use of public transport like social travel (ST). Also many student use the bus pass for their regular traveling. The traditional system of bus pass system is fully depends upon paper means every student carry the paper pass. Means this system has use huge amount of paper. Rather than traditional system, there is invent in this and people create online bus pass system but it is very complex to maintain the users online.

# Proposed Solution:
To overcome this problem QR based student bus pass system get in use.

The System works in two modules:

1. Bus_Pass_Automation.py:
It is a GUI based programme which will be used to provide QR code to students/consumers, its interactive user-interface (UI) will ease the making of excel-sheets for the buses and managing the students, means the use of paper is reduce. This system functionality is fully offline so we does not need internet to operate it, and also no need to carry buss-pass. In this system simply student should fill up the form and pay money. Admin get all the information of student like Name, Enrollment number and respective Bus number. Admin store all this information in database by creating unique id for student and QR code. Admin send the mail to the consumer or student. This module will be installed in university and would be controlled by bus management authorities.

![image](https://user-images.githubusercontent.com/76219349/216086790-afd490dd-6c4a-4fec-ae3f-8641c6e13a38.png)

![image](https://user-images.githubusercontent.com/76219349/216087650-1f8b647f-c032-4ab5-9bd5-aca7e6e229f1.png)

![image](https://user-images.githubusercontent.com/76219349/216091126-350acf8c-b302-49ff-9db7-3477003c38aa.png)

2. Scanner.py
This module will need a camera and a small display as requirements to scan and display the QR code and make the process easy. Model will be deployed in every college-bus this may initially include some costing for the product but it will reduce the labour cost of checking the passes manually which is a slow process and also reduce university loss because of students travelling without a valid bus-pass, model will contain the respective excel-sheet of the bus and check for the person using its QR, every person have their own Qr which can only be used 1 time in morning and 1 time in evening so that it can't be used by any other kid, this also provides the security that the student is boarding the same bus to go home. The system plays audio "Okay" if the QR code scanned is valid and "Access-denied" if the QR is not valid, this makes the model more user interactive and easy to identify intruder.

![image](https://user-images.githubusercontent.com/76219349/216098178-7f8cbfa7-3e0d-438e-b73f-542cf094d1a0.png)

# Libraries Involved:

1. tkinter: Used for GUI purpose, Install using - " pip install tk "

2. pandas: Managing and accessing students data-base, Install using : " pip install pandas "

3. os: To save and verify the excel-file in local storage, (pre-installed)

4. qrcode: To generate QR codes, Install using : " pip install qrcode "

5. openpyxl: For creating and editing excel-sheets, Install using : " pip install openpyxl "

6. PIL: For using images in the UI which makes it more interactive to the user, Install using : "pip install pillow "

7. cv2: Used in Scanner for capturing QR codes, Install using : " pip install opencv-python "

8. playsound: Used in Scanner for playing audio files, Install using : " pip install playsound "
