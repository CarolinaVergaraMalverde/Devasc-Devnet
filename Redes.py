import urllib.parse 
import requests

while True:
    main_api = "https://www.mapquestapi.com/directions/v2/route?" 
    orig = input("Origen (Ciudad de origen o Pais): ")
    if orig == "S" or orig == "salida": 
        break  
    dest = input("Destino (Ciudad de destino o Pais): ")
    if dest == "S" or dest == "salida": 
        break  
    key = "MlXqQ9nqoPBKtCSS75QijE3rGNSEe9M4"  
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest, "unit": "k"}) 
    json_data = requests.get(url).json() 

    print("URL: " + url) 
    json_status = json_data["info"]["statuscode"] 

    if json_status == 0:     
        print("API Status: " + str(json_status) + " = Llamada a ruta correcta.\n")
        print("=============================================")         
        print("Dirección de origen: " + orig + " Hacia: " + dest)         
        print("Kilómetros: " + str("{:.1f}".format(json_data["route"]["distance"]))) 
        print("Duración del viaje: " + json_data["route"]["formattedTime"])         
       
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " (" + str("{:.1f}".format(each["distance"])) + " km)")	 
    print("=====================================================\n")
    
