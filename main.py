import json

def employees_rewrite(key):
    with open("employees.json", "r") as fh:
        file_json = json.load(fh)
    file_data = file_json['employees']
    for i in range(len(file_data)):
        keys_list = list(file_data[i].keys())
        for k in keys_list:
            file_data[i][k.upper()] = file_data[i].pop(k)
    key = key.upper()
    keys_list = list(file_data[0].keys())
    try:
        j = 0
        for p in keys_list:
            if key == p:
                j += 1
                if isinstance(file_data[1][key], int):
                    file_data_sorted = sorted(file_data, key=lambda user: user[key], reverse=True)
                else:
                    file_data_sorted = sorted(file_data, key=lambda user: user[key])
        if j == 0:
            raise ValueError
    except Exception as error:
        return print(error.__class__.__name__,"('Bad key for sorting')")
    with open(f"employees_{key}_sorted.json", "w") as json_file:
        json.dump(file_data_sorted, json_file, indent=4)

employees_rewrite('departmen')


