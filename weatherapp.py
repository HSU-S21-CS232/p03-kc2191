from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('Weather Feather')
root.geometry("600x100")

def zipLookup():

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=50&API_KEY=0E3E5AE2-C31C-4F23-AD8D-1AC132FEF3A7")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name'] 

        if category == "Good":
            air_qual_color = "Green"
        elif category == "Moderate":
            air_qual_color = "Yellow"
        elif category == "Unhealthy for Sensitive Groups":
            air_qual_color = "Orange"
        elif category == "Unhealthy":
            air_qual_color = "Red"
        elif category == "Very Unhealthy":
            air_qual_color = "Purple"
        elif category == "Hazardous":
            air_qual_color = "Maroon"

        root.configure(background=air_qual_color)

        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Times New Roman", 20), background=air_qual_color)
        myLabel.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "No weather for you today, baby"

zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text= "Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1)
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=92227&distance=25&API_KEY=0E3E5AE2-C31C-4F23-AD8D-1AC132FEF3A7


root.mainloop()



