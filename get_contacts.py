# importing the requests library 
import requests 
import time

# api-endpoint 
URL = "http://smartmedicinecup.herokuapp.com/api/get_contact/"

# JSON FORMAT
# {
# 	id_copo: 1,
# 	partition: 1,
# 	moment: "2018-12-30 hh:mm",
# 	event: "tomou|não tomou|cadastrou|removeu",
# 	alarm_info: {
# 		start: {
# 			hour: 10,	
# 			minute: 10,
# 		}
# 		period: {
# 			hour: 10,
# 			minute: 10,
# 		},
# 		duration: 5, ---> dias
# 	},
# }
def get_contacts():
    # extracting data in json format 
    r = requests.get(url = URL)
    data = r.json()
    print(data)
    return data
    
if __name__ == '__main__':
    get_contacts()
