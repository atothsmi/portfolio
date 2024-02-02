import os 
import json 

#DEBUG:
# print(os.getcwd())
# print(os.listdir('pages\\thoughts\\'))

# Get data from txt files and format nicely
dir_path = 'pages\\thoughts\\'

years = os.listdir(dir_path)

thoughts_dict = {}

for year in years:
    thoughts_dict[year] = {}
    for date in os.listdir(dir_path + year + '\\'):
        with open(dir_path + year + '\\' + date, 'r') as f:
            data = f.readlines()
            if len(data) >= 2:
                thoughts_dict[year][date] = {'title': data[0].strip(),'date': data[1].strip(),'content': "".join(data[2:])}

# DEBUG:
# for year in thoughts_dict:
#     print(year)
#     print(thoughts_dict[year])
#     print()

# Write dictonary to json file    
with open('js\\thoughts.json', 'w') as outfile:
    json.dump(thoughts_dict, outfile)
            
data = None
thoughtsHTML = []
prepend = '<div class="padding-2 max-width-100"><div class="portfolio-item center"><div class="portfolio-desc width-100">'
postpend = '</div></div></div>'
with open('js\\thoughts.json', 'r') as infile:
    years = json.load(infile)
    for year in years:
        print(year)
        for date in years[year]:
            print(date)
            content = prepend
            content += f'<h2 class="margin-0">{years[year][date]["title"]}</h2>'
            content += f'<p class="margin-0">{years[year][date]["date"]}</p>'
            content += f'<p>{years[year][date]["content"]}</p>'
            content += postpend
            thoughtsHTML.append(content)

with open('js\\thoughtsHTML.json', 'w') as outfile:
    json.dump(thoughtsHTML, outfile)
