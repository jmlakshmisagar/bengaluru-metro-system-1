import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import qrcode
from metro import *
from D_T_A import *

current_date_time = datetime.now()
current_date = current_date_time.date()

def show_qr_code():
    qr_img_window = tk.Toplevel()
    qr_img_window.title("QR Code")

    qr_code_img = Image.open("qr_code.png")
    qr_code_img_tk = ImageTk.PhotoImage(qr_code_img)

    qr_label = tk.Label(qr_img_window, image=qr_code_img_tk)
    qr_label.image = qr_code_img_tk  
    qr_label.pack()

def result():
    source = current_location_var.get()
    destination = destination_var.get()
    
    if source == destination:
        info_label.config(text="Source and Destination cannot be the same.", fg="red")
    elif source not in stations or destination not in stations:
        info_label.config(text="Source or destination not found.", fg="red")
        print("Source or destination not found.")
    else:
        source_index = -1
        for i, row in enumerate(l):
            if row[0][0] == source:
                source_index = i
                break

        destination_index = -1
        for i, row in enumerate(l[0]):
            if row[0] == destination:
                destination_index = i
                break
        
        if source_index == -1 or destination_index == -1:
            print("Source or destination not found.")
        else:
            distance = l[source_index][destination_index][0]
            time = l[source_index][destination_index][1]
            amount = l[source_index][destination_index][2]
            
            print("Source:" ,source)
            print("Destination:",destination)
            print("Distance:", distance)
            print("Time:", time)
            print("Amount:", amount)


        data = f"Source : {source}\n , Destination : {destination}\n , Distance : {distance}units\n , Time : {time}min\n , Amount : {amount}rupees\n ,Current Date : {current_date} "

        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img.save("qr_code.png")

        print("QR code generated successfully.")

        info_label.config(text=f"NO. of Stations to cross : {stops(source,destination)} \n Distance : {distance}\nEstimated time : {time} min\nEstimated amount : {amount} rupees \nCurrent Date : {current_date}", fg="black")

        show_qr_code()

def reset_selection():
    current_location_var.set("Select Current Location")
    destination_var.set("Select Destination")
    info_label.config(text=" Hello traveler ")

app = tk.Tk()
app.geometry("500x650")
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

stations = ['Attiguppe', 'Baiyappanahalli', 'Banashankari', 'Benniganahalli', 'Challaghatta', 'Chikkapette', 'City_Railway_station', 'Cubbon_Park', 'Dasarahalli', 'Deepanjali_Nagara', 'Doddakallasandra', 'Dr._BR._Ambedkar_Station_(Vidhana_Soudha)', 'Garudacharapalya', 'Goraguntepalya', 'Halasuru', 'Hoodi', 'Hopefarm_Channasandra', 'Indiranagara', 'Jalahalli', 'Jaya_Prakash_Nagara', 'Jayanagara', 'Jnanabharathi', 'Kadugodi_Tree_Park', 'Kengeri', 'Kengeri_Bus_Terminal', 'Konanakunte_Cross', 'Krishna_Rajendra_Market', 'Krishnarajapura_(K.R.Pura)', 'Kundalahalli', 'Kuvempu_Road', 'Lalbagh_Botanical_Garden', 'MG_Road', 'Magadi_Road', 'Mahalakshmi', 'Mysuru_Road', 'Nadaprabhu_Kempegowda_station_(Majestic)', 'Nagasandra', 'Nallurhalli', 'National_College', 'Pantharapalya_(Nayandahalli)', 'Pattanagere', 'Pattanduru_Agrahara', 'Peenya', 'Peenya_Industry', 'Rajajinagara', 'Rajarajeshwari_Nagar', 'Rashtreeya_Vidyalaya_Road', 'Sampige_Road', 'Sandal_Soap_Factory', 'Seetharamapalya', 'Silk_Institute', 'Singayyanapalya', 'Sir_M._Visveshwaraya_Station_(Central_College)', 'South_End_Circle', 'Sri_Balagangadharanatha_Swamiji_Station_(Hosahalli)', 'Sri_Sathya_Sai_Hospital', 'Srirampura', 'Swami_Vivekananda_Road', 'Talaghattapura', 'Trinity', 'Vajarahalli', 'Vijayanagara', 'Whitefield_(Kadugodi)', 'Yelachenahalli', 'Yeshwanthpura']

current_location_var = tk.StringVar()
current_location_var.set("Select Current Location")
destination_var = tk.StringVar()
destination_var.set("Select Destination")

source = ttk.Combobox(frame, textvariable=current_location_var, values=stations, font=('System', 12))
source.pack(pady=12, padx=15)

destination = ttk.Combobox(frame, textvariable=destination_var, values=stations, font=('System', 12))
destination.pack(pady=12, padx=115)

button = tk.Button(master=frame, text='Generate', command=result, bg='#2980b9', fg='white', font=('Helvetica', 12), bd=0, relief='flat')
button.pack(pady=12, padx=10)
button.configure(borderwidth=1, relief='solid')

reset_button = tk.Button(master=frame, text='Reset', command=reset_selection, bg='#2980b9', fg='white', font=('Helvetica', 12), bd=0, relief='flat')
reset_button.pack(pady=10, padx=10)
reset_button.configure(borderwidth=1, relief='solid')

info_label = tk.Label(frame, text=" Hello traveler ", fg='#34495e', font=('System', 12))
info_label.pack(pady=10)



app.mainloop()
