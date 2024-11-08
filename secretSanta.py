import random
import csv
import smtplib
from email.mime.text import MIMEText
import args

random.seed()

#creates the name-email dictionary
def getNames():

    print("gettings assignments...")
    
    names = {}

    with open("names.csv") as f:

        reader = csv.reader(f)
        
        for row in reader:
            if len(row) != 2:
                print("ensure that your names.csv file is formatted properly")
                return None
            else:
                name,email = row[0],row[1]
                names[name] = email

        return names

#create the assignments dictionary
def getAssignments(n):
    if not n:
        return None
    p = list(n.keys())
    random.shuffle(p)

    assignments = {}

    for i in range(len(p)):
        current_participant = p[i]
        next_index = (i + 1) % len(p)
        assigned_participant = p[next_index]

        # Ensure a person is not assigned themselves
        while assigned_participant == current_participant:
            next_index = (next_index + 1) % len(p)
            assigned_participant = p[next_index]

        # Assign the participant to their Secret Santa
        assignments[current_participant] = n[assigned_participant]

        #write the assignments to a file just in case
        with open ("assLog.txt",'w') as al:
            for key,value in assignments.items() :
                al.write(f"{key}: {find_key_by_value(n,value)}\n")

    return assignments

#there's probably a better data structure to use for this but this is only version 1 
def find_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None

def send_secret_santa_emails(assignments, sender_email, sender_password, smtp_server, smtp_port,name_email_dict):
    for participant, assigned_person in assignments.items():
        
        # Email content
        subject = args.subject

        email_body = args.body.format(
            giver=name_email_dict[participant],
            receiver = find_key_by_value(name_email_dict,assigned_person),
            Santa = args.Santa
        )

        # Prepare the email
        msg = MIMEText(args.body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = name_email_dict[participant]
        msg.attach(MIMEText(email_body, "plain"))

        # Send the email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, [name_email_dict[participant]], msg.as_string())
            print(f"Email sent to {participant} successfully!")
        except Exception as e:
            print(f"Error sending email to {participant}: {e}")

def main():

    nameEmail = getNames()

    #pardon my profanity
    Ass = getAssignments(nameEmail)

    send_secret_santa_emails(Ass,args.user,args.gmail_pass,args.host,args.port,nameEmail)

if __name__ == "__main__" :
    main()
