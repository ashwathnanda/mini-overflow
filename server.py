'''
An Rest-Application using Flask's Restful library . Call the service using the IP provided to get the project required.
'''

#importing necessary libraries
from flask import Flask,jsonify
from flask_restful import Api, Resource, reqparse
import pandas as pd
from flashtext import KeywordProcessor
import json
from moesifwsgi import MoesifMiddleware

moesif_settings = {
    'APPLICATION_ID': 'eyJhcHAiOiIxNTA6MjU3IiwidmVyIjoiMi4wIiwib3JnIjoiNDU2OjEzMiIsImlhdCI6MTU1NDc2ODAwMH0.O3rVkWX-yP-kr05hv2s_ezvncL2PJ8dsxWJ0ZMB8pHw'
}



app = Flask(__name__)
api = Api(app)
app.wsgi_app = MoesifMiddleware(app.wsgi_app, moesif_settings)


parser = reqparse.RequestParser()

key_processor = KeywordProcessor()
data = pd.read_csv('dataset/data_tag.csv')
l = list(data['Tag'])
my_list2 = []
for i,m in enumerate(l):
   my_list2.extend(m.split(','))
	
#adding the tags onto the processor
key_processor.add_keywords_from_list(my_list2)

class Fetch_code(Resource):
   def get(self, code):

      code.lower()
      ans = key_processor.extract_keywords(code)
      ans.sort()
      ans = ','.join(ans)
      for i,item in enumerate(l):
         if(ans == item):
            return jsonify(requirement=code,data_link=data['Snippet'][i],status=200)
      return jsonify(requirement=code,data_link='Requirement not found' , status=404)

#POST request with 'req' as the argument  
   def post(self):
      parser.add_argument('req',type=str)
      args = parser.parse_args()
      code = args['req']
      if code is None:
         return jsonify(requirement='No requirement found',data_link='None',status=404)
      else:
         code.lower()
         ans = key_processor.extract_keywords(code)
         ans.sort()
         ans = ','.join(ans)
         for i,item in enumerate(l):
            if(ans == item):
               return jsonify(requirement=code,data_link=data['Snippet'][i], status=200)
         return jsonify(requirement=code,data_link='Requirement not found' , status=404)
      
api.add_resource(Fetch_code, "/<string:code>" , '/')
app.run(port = 8080,host='0.0.0.0',debug=True) 