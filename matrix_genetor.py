import random

# List of stations
stations = ['Nagasandra', 'Dasarahalli', 'Jalahalli', 'Peenya_Industry', 'Peenya', 'Goraguntepalya', 'Yeshwanthpura', 
            'Sandal_Soap_Factory', 'Mahalakshmi', 'Rajajinagara', 'Kuvempu_Road', 'Srirampura', 'Sampige_Road', 
            'Nadaprabhu_Kempegowda_station_(Majestic)', 'Chikkapette', 'Krishna_Rajendra_Market', 'National_College', 
            'Lalbagh_Botanical_Garden', 'South_End_Circle', 'Jayanagara', 'Rashtreeya_Vidyalaya_Road', 'Banashankari', 
            'Jaya_Prakash_Nagara', 'Yelachenahalli', 'Konanakunte_Cross', 'Doddakallasandra', 'Vajarahalli', 
            'Talaghattapura', 'Silk_Institute', 'Whitefield_(Kadugodi)', 'Hopefarm_Channasandra', 'Kadugodi_Tree_Park', 
            'Pattanduru_Agrahara', 'Sri_Sathya_Sai_Hospital', 'Nallurhalli', 'Kundalahalli', 'Seetharamapalya', 'Hoodi', 
            'Garudacharapalya', 'Singayyanapalya', 'Krishnarajapura_(K.R.Pura)', 'Benniganahalli', 'Baiyappanahalli', 
            'Swami_Vivekananda_Road', 'Indiranagara', 'Halasuru', 'Trinity', 'MG_Road', 'Cubbon_Park', 
            'Dr._BR._Ambedkar_Station_(Vidhana_Soudha)', 'Sir_M._Visveshwaraya_Station_(Central_College)', 
            'Nadaprabhu_Kempegowda_station_(Majestic)', 'City_Railway_station', 'Magadi_Road', 
            'Sri_Balagangadharanatha_Swamiji_Station_(Hosahalli)', 'Vijayanagara', 'Attiguppe', 'Deepanjali_Nagara', 
            'Mysuru_Road', 'Pantharapalya_(Nayandahalli)', 'Rajarajeshwari_Nagar', 'Jnanabharathi', 'Pattanagere', 
            'Kengeri_Bus_Terminal', 'Kengeri', 'Challaghatta']

# Function to generate the matrix
matrix=[[[0,0,0]]]
for i in range(len(stations)):
    matrix[0].append([stations[i],0,0])
for i in range(1,len(stations)+1):
    for j in range(len(stations)+1):
        if j==0:
            matrix.append([[stations[i-1],0,0]])
        elif i==j:
            matrix[i].append([0,0,0])
        else:
            x=random.randint(1, 40)
            y=random.randint(1, 40)
            z=random.randint(1, 40)
            matrix[i].append([x,y,z])
# print(matrix/)
for i in range(len(matrix)):
    print(matrix[i],",\n")

    