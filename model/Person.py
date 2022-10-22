from marshmallow import Schema, fields

class Person():
  def __init__(self, person_id, name, age, city):
    self.person_id = person_id
    self.name = name
    self.age = age
    self.city = city

  def __repr__(self):
    return '<Person(name={self.name!r})>'.format(self=self)


class PersonSchema(Schema):
  person_id = fields.Number()
  name = fields.Str()
  age = fields.Number()
  city = fields.Str()