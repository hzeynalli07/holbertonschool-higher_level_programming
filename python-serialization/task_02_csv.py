#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """CSV məlumatlarını oxuyur və data.json faylına JSON kimi yazır."""
    try:
        data = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # DictReader hər sətri sütun başlıqlarına uyğun lüğətə çevirir
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
