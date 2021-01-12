import json

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
    print(building)
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
