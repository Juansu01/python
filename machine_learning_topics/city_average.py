import csv

previous_city = None
city_count = 0
city_dict = {}
name_list = []
with open('citytemp.csv', newline='') as file:
    content = csv.reader(file)
    for row in content:
        if previous_city:
            if previous_city != row[0]:
                name_list.append(row[0])
                city_dict[row[0]] = {}
                city_dict[row[0]]["temps"] = [f"{row[1]}, {row[2]}"]
                city_dict[row[0]]['format'] = row[2]
                city_count += 1
                previous_city = row[0]
                continue
            city_dict[row[0]]["temps"].append(f"{row[1]}, {row[2]}")
        else:
            city_dict[row[0]] = {}
            city_dict[row[0]]['temps'] = [f"{row[1]}, {row[2]}"]
            city_dict[row[0]]['format'] = row[2]
            city_count += 1
            previous_city = row[0]
            name_list.append(row[0])
    for city in name_list:
        temps = city_dict[city]['temps']
        far_temps = []
        for temp in temps:
            if temp[-1:] == 'C':
                to_far = (int(temp[:2]) * 9/5) + 32
                far_temps.append(to_far)
            else:
                far_temps.append(int(temp[:2]))
        avg = sum(far_temps) / len(far_temps)
        print(f"{city} average temp is : {str(avg)[:5]}")
    print(f"TOTAL CITIES:{city_count}")
