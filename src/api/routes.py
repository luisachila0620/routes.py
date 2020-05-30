"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db
from api.utils import generate_sitemap
#from models import Person

api = Blueprint('api', __name__)
import random


@api.route('/excuse', methods=['GET'])
def handle_hello():
    excuse = 'The dog eat my homework when I finished'
    who = ['the dog','my granma','his turtle','my bird']
    what = ['eat','pissed','crushed','broked']
    when = ['before the class','right in time','when I finished','during my lunch','while I was praying']
    excuse = who[random.randint(0,len(who)-1)]+" "+what[random.randint(0,len(what)-1)]+" "+when[random.randint(0,len(when)-1)]



    response_body = {
        "msg": "world"
    }

    return jsonify(excuse), 200