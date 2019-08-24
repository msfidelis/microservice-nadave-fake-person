from flask import Flask, jsonify
from faker import Faker
from faker.providers import profile, automotive, ssn
import json

fields_to_search = 'username,blood_group,address,company,job,mail,sex,name,residence,mail'

app = Flask(__name__)

VERSION = "v1"

@app.route('/faker',  methods=['GET'])
def fake():
  fake = Faker('pt_BR')
  fake.add_provider(profile)
  fake.add_provider(automotive)
  fake.add_provider(ssn)

  basic = fake.profile(fields=fields_to_search, sex=None)
  person_json = json.dumps(basic, sort_keys=False)


  result = {
    'name': basic['name'],
    'job': basic['job'],
    'blood_group': basic['blood_group'],
    'sex': basic['sex'],
    'address': basic['address'],
    'residence': basic['residence'],
    'company': basic['company'],
    'license_plate': fake.license_plate(),
    'cpf': fake.cpf(),
    'rg': fake.rg()
  }

  return jsonify(result)


@app.route('/faker/male',  methods=['GET'])
def male_fake():
  fake = Faker('pt_BR')
  fake.add_provider(profile)
  fake.add_provider(automotive)
  fake.add_provider(ssn)

  basic = fake.profile(fields=fields_to_search, sex='M')
  person_json = json.dumps(basic, sort_keys=False)


  result = {
    'name': basic['name'],
    'job': basic['job'],
    'blood_group': basic['blood_group'],
    'sex': basic['sex'],
    'address': basic['address'],
    'residence': basic['residence'],
    'company': basic['company'],
    'license_plate': fake.license_plate(),
    'cpf': fake.cpf(),
    'rg': fake.rg()
  }

  return jsonify(result)


@app.route('/faker/female',  methods=['GET'])
def female_fake():
  fake = Faker('pt_BR')
  fake.add_provider(profile)
  fake.add_provider(automotive)
  fake.add_provider(ssn)

  basic = fake.profile(fields=fields_to_search, sex="F")
  person_json = json.dumps(basic, sort_keys=False)


  result = {
    'name': basic['name'],
    'job': basic['job'],
    'blood_group': basic['blood_group'],
    'sex': basic['sex'],
    'address': basic['address'],
    'residence': basic['residence'],
    'company': basic['company'],
    'license_plate': fake.license_plate(),
    'cpf': fake.cpf(),
    'rg': fake.rg()
  }

  return jsonify(result)

@app.route('/healthcheck',  methods=['GET'])
def healthcheck():
  result = {
    "status": 200,
    "version": VERSION
  }

  return jsonify(result)


if __name__ == "__main__":
  app.run(host='0.0.0.0')