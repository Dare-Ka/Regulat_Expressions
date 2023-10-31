from pprint import pprint
import csv
import re

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
new_list = []
pprint(contacts_list)

keys = contacts_list[0]
values = contacts_list[1:]
contacts_dict = []
for num, vals in enumerate(values):
    contacts_dict.append({})
    for key, val in zip(keys, vals):
        contacts_dict[num].update({key: val})

pprint(contacts_dict)
pprint(len(contacts_dict))

def fix_names():
    for name in contacts_dict:
        split_ = name['lastname'].split(' ')
        if len(split_) > 1:
            name['lastname'] = split_[0]
            name['firstname'] = split_[1]
        if len(split_) > 2:
            name['surname'] = split_[2]

        split_ = name['firstname'].split(' ')
        if len(split_) > 1:
            name['firstname'] = split_[0]
            name['surname'] = split_[1]
    return


def fix_phones():
    phone_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?')
    phone_substitution = r'+7(\2)\3-\4-\5\6\7\8'
    for name in contacts_dict:
        name['phone'] = phone_pattern.sub(phone_substitution, name['phone'])
    return
fix_names()
fix_phones()
pprint(contacts_dict)
