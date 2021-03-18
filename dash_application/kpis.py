import requests
import json



#k1_endpoint = "https://eydvdcrr2v9awbf-iboardadw.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi1/incvol/"

#k1_r = requests.get(k1_endpoint)
#k1_kpi_data = k1_r.json()["items"]


#ALTERNATIVE OFFLINE
k1_endpoint = "kpi_examples/kpi1.json"
with open(k1_endpoint) as json_file:
    k1_kpi_data = json.load(json_file)["items"]
    



k1_months = []
k1_incidences_numbers = []
k1_priorities = []

for dict in k1_kpi_data:
    k1_months.append(dict["month"])
    k1_incidences_numbers.append(dict["incidences_number"])
    k1_priorities.append(dict["priority"])

print(k1_months)
print(k1_incidences_numbers)
print(k1_priorities)




