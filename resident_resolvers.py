import json
import ipdb

def resident_with_id(_, info, _id):
    with open('./data/residents.json') as file:
        data = json.load(file)
        for resident in data['residents']:
            if resident['id'] == _id:
                return resident

def get_residents(_, info):
    with open('./data/residents.json') as file:
        data = json.load(file)
        return data['residents']

def resolve_residents_in_building(building, info):
    with open('./data/residents.json') as file:
        data = json.load(file)
        residents = [
            resident
            for resident
            in data['residents']
            if resident['building']
            == building['id']
        ]
        return residents

def resolve_resident_family(resident, info):
    family_residents = []
    family = resident['family']
    with open('./data/residents.json') as file:
        data = json.load(file)
        for member in family:
            for resident in data['residents']:
                if resident['id'] == member:
                    family_residents.append(resident)
    return family_residents

def update_resident_name(_, info, _id, _name):
    with open('./data/residents.json') as file:
        data = json.load(file)
        for resident in data['residents']:
            if len(data['residents']) < int(_id):
                return { 'success': False }
            if resident['id'] == _id:
                resident['name'] = _name
                return { 'success': True, "resident": resident }

def update_resident_age(_, info, _id, _age):
    with open('./data/residents.json') as file:
        data = json.load(file)
        for resident in data['residents']:
            if len(data['residents']) < int(_id):
                return { "success": False }
            if resident['id'] == _id:
                resident['age'] = _age
                return { "success": True, "resident": resident }



# return
