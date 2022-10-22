from flask import Flask, jsonify, request
from model.Person import Person, PersonSchema


app = Flask(__name__)

people = [
  Person (1, 'Maria', 15, 'Brasilia'),
  Person (2, 'Joao', 85, 'Sao Paulo'),
  Person (3, 'Jose', 23, 'Recife'),
]

@app.route('/person')
def get_produtos():
    schema = PersonSchema(many=True)
    result = schema.dump(people)
    return jsonify(result)

@app.route('/person/<int:person_id>', methods = ['GET'])
def get_produto(person_id):
    schema = PersonSchema(many=True)
    result = schema.dump(people)
    for person in result:
      if(person['person_id'] == person_id):
        return person
    return("Not Found")