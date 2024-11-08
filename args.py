user = "your_email_here@gmail.com" #sender's email
host = "smtp.gmail.com"
port = 587 #For TLS
gmail_pass = "pass word goes here" 


#ascii Santa, feel free to put whatever you want here, or take it out entirely
Santa = "   *        *        *        __o    *       *\n*      *       *        *    /_| _     *\n   K  *     K      *        O'_)/ \  *    *\n  <')____  <')____    __*   V   \  ) __  *\n   \ ___ )--\ ___ )--( (    (___|__)/ /*     *\n *  |   |    |   |  * \ \____| |___/ /  *\n    |*  |    |   |     \____________/       *"

subject = "Secret Santa Assignment"

body = """
Hello {giver}!
You are assigned to buy a gift for: {receiver}

Please limit your gift to $50 or less.

Merry Christmas!

Love,
J0b, Retired Web-scraper
{Santa}
This message was sent automatically. You can reply if you really want to, but no one is checking this inbox.
"""