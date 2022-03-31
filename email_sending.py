# A program that automate sending of emails using python 
import smtplib
contact_name = []
contact_email = []
def get_contacts(file_value):
    with open(file_value, "r") as contact_val:
     reci_contact = contact_val.read().split("\n")
    for i in range(0, len(reci_contact)):
            first_name = reci_contact[i].split()[0][0].upper() + reci_contact[i].split()[0][1:]
            last_name = reci_contact[i].split()[1][0].upper() + reci_contact[i].split()[1][1:]
            email = reci_contact[i].split()[2]
            full_name = f"{first_name} {last_name}"
            contact_name.append(full_name)
            contact_email.append(email)
            name_email_file = dict(zip(contact_name, contact_email))
    return name_email_file
# file_value = get_contacts("user_contact.txt")
# print(file_value)
server_email = 'smtp.gmail.com'
port = 465
def smpt_details(name_email_file, sender_email,sender_password):
    with smtplib.SMTP(server_email, port) as server:
        
        
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, contact_email, msg)
        server.ehlo()
        server.starttls()
        server.ehlo()
        for contact_name, contact_email in name_email_file.items():
            msg  = f"" '''  Dear {contact_name}, 
                            There will be a general meeting of all members of staff.
                            Date: 12th April
                            Time : 12 noon
                            Venue: Multipurpose Hall
                            Thanks,
                            Yours sincerly,
                            Mr Beop '''
sender_email = input('enter email: ')
sender_password = input("enter password: ")
file_details = get_contacts("user_contact.txt")
smtp_msg = smpt_details(file_details, sender_email, sender_password)

