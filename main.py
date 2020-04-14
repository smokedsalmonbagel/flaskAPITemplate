import json

from flask import Flask
from flask import request,redirect



app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def root():
    return 'Root endpoint' 

@app.route("/endpoint1", methods=['GET','POST'])
def endpoint1():   
    if request.args.get('name') is not None:  
        print('NAME: '+ request.args.get('name'))
        return 'hello ' + request.args.get('name')
        
    else:
        return 'hello unknown'

@app.route('/endpoint2/',defaults={"var": None})
@app.route("/endpoint2/<var>", methods=['GET','POST'])
def endpoint2(var=None):   
    if var is not None:  
        return 'var: ' + var
    else:
        return 'var: None'
        
        
if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True)

    
    
    
    
    