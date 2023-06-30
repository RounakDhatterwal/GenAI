def extract_keys(dictionary, keys):
    dict = {}
    for key in keys:
        if key in dictionary:
            dict[key] = dictionary[key]
    return dict

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

new_dict = extract_keys(sample_dict, keys)

print(new_dict)
