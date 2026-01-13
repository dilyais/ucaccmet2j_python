import json

with open('precipitation.json') as file:
    line = json.load(file)

stations = []
ppt_m_s = {}

for i in line:
    if i['station'] not in stations:
        stations.append(i['station'])

for n in stations:
    ppt_m_s[n] = {}

for i in line:
    station = i['station']
    month = i['date'][:7]
    if month not in ppt_m_s[station]:
        ppt_m_s[station][month] = []
    ppt_m_s[station][month].append(i['value'])

ppt_total_per_month = {}
for station, months_dict in ppt_m_s.items():
    ppt_total_per_month[station] = {}
    for month, values in months_dict.items():
        ppt_total_per_month[station][month] = sum(values)

with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(ppt_total_per_month, f, indent=4, ensure_ascii=False)

print("Monthly totals saved to results.json")
