import pandas as pd
from flask import Flask, render_template
from flask_restful import Api, Resource
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

sheet_id="1Okfg6syPwad4AMoplykawUytVMGouD_1kkKo-d0k8gM"
df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

#converting data to dictionary objects 
records=df.to_dict(orient='records')

#instantiate new Flask Application Object
app=Flask(__name__)
# initialize API object for flask application
api=Api(app)

#Routes - pages
@app.route('/')
def index():
    return render_template('index.html')


#API Requests 
class All(Resource):
    def get(self):
        return records 
    

class Name(Resource):
    def get(self,value):
            return [obj for obj in records if obj['const']==(value)]

class N_iter(Resource):
    def get(self,value):
            return [obj for obj in records if obj['n_iter']==(value)]
        
class Deg_C(Resource):
    def get(self,value):
            return [obj for obj in records if obj['deg_c']==(value)]

#Register API Resources
api.add_resource(All,'/api/')
api.add_resource(Name,'/api/const/<int:value>')
api.add_resource(N_iter,'/api/n_iter/<int:value>')
api.add_resource(Deg_C,'/api/deg_c/<int:value>')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5001,debug=True)
    