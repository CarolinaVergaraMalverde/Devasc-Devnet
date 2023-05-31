import urllib.parse 
import requests

while True:
    main_api = "https://www.mapquestapi.com/directions/v2/route?" 
    origen = input("Origen (Ciudad de origen, Pais): ")
    if origen == "S" or origen == "salida": 
        break  
    dest = input("Destino (Ciudad de destino, Pais): ")
    if dest == "S" or dest == "salida": 
        break  
    key = "MlXqQ9nqoPBKtCSS75QijE3rGNSEe9M4"  
    url = main_api + urllib.parse.urlencode({"key": key, "from": origen, "to": dest, "unit": "k"}) 
    json_data = requests.get(url).json() 

    print("URL: " + url) 
    json_status = json_data["info"]["statuscode"] 

    if json_status == 0:     
        print("API Status: " + str(json_status) + " = Llamada a ruta correcta.\n")
        print("=============================================")         
        print("Dirección de origen: " + origen + " Hacia: " + destino)         
        print("Kilómetros: " + str("{:.1f}".format(json_data["route"]["distance"]))) 
        print("Duración del viaje: " + json_data["route"]["formattedTime"])         
       
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " (" + str("{:.1f}".format(each["distance"])) + " km)")	 
    print("=====================================================\n")
    
