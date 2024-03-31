green_line_stations = [14,'Nagasandra', 'Dasarahalli', 'Jalahalli', 'Peenya_Industry', 'Peenya', 'Goraguntepalya', 'Yeshwanthpura', 'Sandal_Soap_Factory', 'Mahalakshmi', 'Rajajinagara', 'Kuvempu_Road', 'Srirampura', 'Sampige_Road', 'Nadaprabhu_Kempegowda_station_(Majestic)', 'Chikkapette', 'Krishna_Rajendra_Market', 'National_College', 'Lalbagh_Botanical_Garden', 'South_End_Circle', 'Jayanagara', 'Rashtreeya_Vidyalaya_Road', 'Banashankari', 'Jaya_Prakash_Nagara', 'Yelachenahalli', 'Konanakunte_Cross', 'Doddakallasandra', 'Vajarahalli', 'Talaghattapura', 'Silk_Institute']
purple_line_stations = [23,'Whitefield_(Kadugodi)', 'Hopefarm_Channasandra', 'Kadugodi_Tree_Park', 'Pattanduru_Agrahara', 'Sri_Sathya_Sai_Hospital', 'Nallurhalli', 'Kundalahalli', 'Seetharamapalya', 'Hoodi', 'Garudacharapalya', 'Singayyanapalya', 'Krishnarajapura_(K.R.Pura)', 'Benniganahalli', 'Baiyappanahalli', 'Swami_Vivekananda_Road', 'Indiranagara', 'Halasuru', 'Trinity', 'MG_Road', 'Cubbon_Park', 'Dr._BR._Ambedkar_Station_(Vidhana_Soudha)', 'Sir_M._Visveshwaraya_Station_(Central_College)', 'Nadaprabhu_Kempegowda_station_(Majestic)', 'City_Railway_station', 'Magadi_Road', 'Sri_Balagangadharanatha_Swamiji_Station_(Hosahalli)', 'Vijayanagara', 'Attiguppe', 'Deepanjali_Nagara', 'Mysuru_Road', 'Pantharapalya_(Nayandahalli)', 'Rajarajeshwari_Nagar', 'Jnanabharathi', 'Pattanagere', 'Kengeri_Bus_Terminal', 'Kengeri', 'Challaghatta']

def distance(source,destination):
    if source in green_line_stations and destination in green_line_stations:
        return abs(green_line_stations.index(source)-green_line_stations.index(destination))
      
    elif source in purple_line_stations and destination in purple_line_stations:
        return abs(purple_line_stations.index(source)-purple_line_stations.index(destination))
  
    elif source in purple_line_stations and destination in green_line_stations:
        p=abs(purple_line_stations.index(source)-purple_line_stations[0])
        g=abs(green_line_stations.index(destination)-green_line_stations[0])
        return p+g
   
    elif source in green_line_stations and destination in purple_line_stations:
        g=abs(green_line_stations.index(source)-green_line_stations[0])
        p=abs(purple_line_stations.index(destination)-purple_line_stations[0])
        return g+p
        
    else:
        print("Invalid Station Name")

final=distance("Pattanagere","Whitefield_(Kadugodi)")
print("distance : ",final," units")
tim=final*10
print("Estimated time : ",tim," minutes")
print("Estimated amount : ",round(tim/3,2),"Rupess")