'''
import json
with open ("demo.json",'w') as file:
    data = [
        {'id':'1','name':'nikhil'},
        {'id':'2','name':'saaketh'},
        {'id':'3','name':'sapnil'},
        {'id':'4','name':'shanmuka'},
        ]
    json.dump(data,file,indent=4)
    print("data saved")
'''
import json
with open('demo.json',"r") as file:
    data = json.load(file)
data.append({'id':'5','name':'abhi'})
with open('demo.json',"w") as file:  #we donot have append so we read and we write in json
    json.dump(data,file,indent=4)
