import datetime
from email.message import EmailMessage
import imghdr
import pandas as pd
import pywhatkit
import smtplib


# define a function for sending email
def sendEmail(receiver_email, name, msg):
    # Get sender's details
    sender_email = "spbhagwat01@gmail.com"
    sender_password = "znlwtodkhizioveu"

    # creating an object of EmailMessage class
    mail = EmailMessage()

    # Defining email subject, sender email, receiver email & email body
    mail['Subject'] = "Happy birthday!"
    mail['From'] = sender_email
    mail['To'] = receiver_email
    mail.set_content(msg)

    # Send an image as attachment
    with open("bday.jpeg", 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    mail.add_attachment(image_data, maintype='image',
                        subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # Login to SMTP server
        server.login(sender_email, sender_password)

        # Sending email using send_message method by passing EmailMessage object
        server.send_message(mail)

        # Disconnect server
        server.quit()

    print("Email sent to " + str(name) +
          " wishing them with message: " + str(msg))


#  define a function for sending whatsapp message
def whatsapp_msg(name, phone, msg):
    # Set time to send msg i.e 1 min later than current time
    hr = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute) + 1

    pywhatkit.sendwhatmsg(phone, msg, hr, min)
    # WhatsApp will open and after 15 Seconds  & message will be Delivered!

    print("Messsage sent to " + str(name) +
          " wish them with message: " + str(msg))


if __name__ == "__main__":
    dataframe = pd.read_excel("birthday_list.xlsx")


    # today's date
    today = datetime.datetime.now().strftime("%d-%m")

    # current year
    yearNow = datetime.datetime.now().strftime("%Y")

    for index, item in dataframe.iterrows():

        # stripping the birthdays in excel sheet as : DD-MM
        bday = item['Date_of_Birth'].strftime("%d-%m")

        name = item['Name']
        phone = '+91'+str(item['Mobile_no'])
        email = item['Email']

        # Message to be sent
        msg = "Wish you many many happy returns of the day " + name+ "! \nShravani Bhagwat"
        if (today == bday) and yearNow not in str(item['year']):

            # calling the sendEmail function
            sendEmail(email, name, msg)
            # calling the whatsapp_msg function
            whatsapp_msg(name, phone, msg)