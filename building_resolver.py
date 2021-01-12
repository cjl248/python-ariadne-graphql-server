import json

def resolve_resident_building(resident, info):
    with open('./data/buildings.json') as file:
        data = json.load(file)
        resident_building = None
        for building in data['buildings']:
             if building['id'] == resident['building']:
                 resident_building = building
        return resident_building

def building_with_id(_, info, _id):
    with open('./data/buildings.json') as file:
        data = json.load(file)
        for building in data['buildings']:
            if building['id'] == _id:
                return building

def get_buildings(_, info):
    with open('./data/buildings.json') as file:
        data = json.load(file)
        return data['buildings']
