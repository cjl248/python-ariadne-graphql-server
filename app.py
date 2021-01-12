import importlib

from ariadne import graphql_sync, make_executable_schema, load_schema_from_path
from ariadne import ObjectType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify

import resident_resolvers as rr
import building_resolver as br


app = Flask(__name__)

type_defs = load_schema_from_path('schema.graphql')

query = QueryType()
building = ObjectType('Building')
resident = ObjectType('Resident')

query.set_field('buildings', br.get_buildings)
query.set_field('building_with_id', br.building_with_id)

query.set_field('residents', rr.get_residents)
query.set_field('resident_with_id', rr.resident_with_id)

building.set_field('residents', rr.resolve_residents_in_building)

resident.set_field('building', br.resolve_resident_building)

schema = make_executable_schema(type_defs, [query, building, resident])


@app.route('/graphql', methods = ['GET'])
def playground():
    return PLAYGROUND_HTML, 200

@app.route('/graphql', methods = ['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value = None,
        debug = app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
