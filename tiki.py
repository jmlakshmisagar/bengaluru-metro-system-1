import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

def result():
    current_location = current_location_var.get()
    destination = destination_var.get()
    
    if current_location == destination:
        info_label.config(text="Source and Destination cannot be the same.", fg="red")
    else:
        info_label.config(text=f"From : {current_location}\nTo: {destination}", fg="black")

app = tk.Tk()
app.geometry("500x550")
app.title("Metro System")
app.config(bg='#808080')

img = Image.open("metrologo.png")
img = img.resize((150, 120))
tk_img = ImageTk.PhotoImage(img)

label = tk.Label(app, text="Namma Metro", bg='#808080', fg='white', font=('Helvetica', 25))
label.pack(pady=20)

frame = tk.Frame(master=app, bg='#34495e')
frame.pack(pady=20, padx=40, fill='both', expand=True)

image_label = tk.Label(master=frame, image=tk_img, bg='#34495e')
image_label.pack(pady=15, padx=10)

# Dropdown menu options
green_line_stations = [
    "Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpura",
    "Sandal Soap Factory", "Mahalakshmi", "Rajajinagara", "Kuvempu Road", "Srirampura", "Sampige Road",
    "Nadaprabhu Kempegowda station (Majestic)", "Chikkapette", "Krishna Rajendra Market", "National College",
    "Lalbagh Botanical Garden", "South End Circle", "Jayanagara", "Rashtreeya Vidyalaya Road", "Banashankari",
    "Jaya Prakash Nagara", "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra", "Vajarahalli", "Talaghattapura",
    "Silk Institute", "Whitefield (Kadugodi)", "Hopefarm Channasandra", "Kadugodi Tree Park", "Pattanduru Agrahara",
    "Sri Sathya Sai Hospital", "Nallurhalli", "Kundalahalli", "Seetharamapalya", "Hoodi", "Garudacharapalya",
    "Singayyanapalya", "Krishnarajapura (K.R.Pura)", "Benniganahalli", "Baiyappanahalli", "Swami Vivekananda Road",
    "Indiranagara", "Halasuru", "Trinity", "MG Road", "Cubbon Park", "Dr. BR. Ambedkar Station (Vidhana Soudha)",
    "Sir M. Visveshwaraya Station (Central College)", "Nadaprabhu Kempegowda station (Majestic)", "City Railway station",
    "Magadi Road", "Sri Balagangadharanatha Swamiji Station (Hosahalli)", "Vijayanagara", "Attiguppe",
    "Deepanjali Nagara", "Mysuru Road", "Pantharapalya (Nayandahalli)", "Rajarajeshwari Nagar", "Jnanabharathi",
    "Pattanagere", "Kengeri Bus Terminal", "Kengeri", "Challaghatta"
]

purpal_line_stations = green_line_stations  # For demonstration, you can modify this as needed

# Define the variables
current_location_var = tk.StringVar()
current_location_var.set("Select Current Location")
destination_var = tk.StringVar()
destination_var.set("Select Destination")

current_location_combobox = ttk.Combobox(frame, textvariable=current_location_var, values=green_line_stations, font=('System', 12))
current_location_combobox.pack(pady=12, padx=10)

destination_combobox = ttk.Combobox(frame, textvariable=destination_var, values=purpal_line_stations, font=('System', 12))
destination_combobox.pack(pady=12, padx=10)

button = tk.Button(master=frame, text='Calculate', command=result, bg='#2980b9', fg='white', font=('Helvetica', 12), bd=0, relief='flat')
button.pack(pady=12, padx=10)

# Set rounded border
button.configure(borderwidth=1, relief='solid')

# Label to display result message
info_label = tk.Label(frame, text="", fg='#34495e', font=('System', 12))  # Set foreground color to match background
info_label.pack(pady=10)


app.mainloop()
