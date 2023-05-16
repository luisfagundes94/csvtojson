import csv
import json

input_csv_file = "input.csv"
output_json_file = "output.json"

attributes = ["categoria", "quantidade", "nome", "imagem", "preço", "site", "status"]

with open(input_csv_file, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader)  # Skipping header if it's present, otherwise remove this line
    
    data = []
    for row in csv_reader:
        entry = {attr: value for attr, value in zip(attributes, row)}
        data.append(entry)

with open(output_json_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
