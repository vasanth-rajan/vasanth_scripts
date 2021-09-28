import json

r'''
json keywords:
dumps - convert json string to dict 
loads - convert dict to json 
load - loading a json file 
dump - writing the dictionary to a file
'''

json_obj = '{"id":1, "name": "Emily", "language": ["C++", "Python"]}'

## converts json to dictionary
json_dict = json.loads(json_obj)
print("JSON_dict content: {}".format(json_dict))
print("JSON_dictionary dataType: {}".format(type(json_dict)))

## convert dict to JSon 
json_obj_conv = json.dumps(json_dict)
print("Converted JSON_obj content: {}".format(json_obj_conv))
print("Converted JSON_obj dataType: {}".format(type(json_obj_conv)))

## JSON File name 
jsonFile = "json_output.json"

## write a dict to JSON file 
with open(jsonFile, "w") as f0:
    json.dump(json_dict, f0)


## Read json file and convert as dict 
with open(jsonFile) as f1:
    json_read = json.load(f1)
print("JSON file content: {}".format(json_read))
print("JSON_dictionary dataType: {}".format(type(json_read)))
