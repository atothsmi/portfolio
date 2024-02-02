import os 
import json 

#DEBUG:
# print(os.getcwd())
# print(os.listdir('pages\\thoughts\\'))

dir_path = 'pages\\thoughts\\'

years = os.listdir(dir_path)

thoughts_dict = {}

for year in years:
    thoughts_dict[year] = {}
    for date in os.listdir(dir_path + year + '\\'):
        with open(dir_path + year + '\\' + date, 'r') as f:
            data = f.readlines()
            if len(data) >= 2:
                thoughts_dict[year][date] = {'title': data[0].strip(),'date': data[1].strip(),'content': data[2:]}

# DEBUG:
# for year in thoughts_dict:
#     print(year)
#     print(thoughts_dict[year])
#     print()
            
# json_string = json.dumps(thoughts_dict, indent=3)
# print(json_string)
# array = [{i: thoughts_dict[i]} for i in thoughts_dict]

            
with open('js\\thoughts.json', 'w') as outfile:
    json.dump(thoughts_dict, outfile)
            
