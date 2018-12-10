from flask import Blueprint,make_response,json,abort,Flask,jsonify
from flask_restful import Api
from .redflags.models import All_Incidents,One_Incident

version_1=Blueprint('api_v1',__name__,url_prefix='/api/v1')


api=Api(version_1)
api.add_resource(All_Incidents,'/flags/')
api.add_resource(One_Incident,'/flags/<id>')
