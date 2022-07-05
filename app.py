from flask import Flask,jsonify,request
app = Flask(__name__)

contacts = [
    {
        'id':1,
        'name':'John',
        'number':'9182002023',
        'done':False
    },
    {
        'id':2,
        'name':'David',
        'number':'9187795812',
        'done':False
    }
]
@app.route('/add-task',methods = ['POST'])
def addTask():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide data in correct format'
        })
    newTask = {
        'id':contacts[-1]['id']+1,
        'name':request.json['name'],
        'number':request.json['number'],
        'done':False
    }
    contacts.append(newTask)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })
@app.route('/get-task')
def getTask():
    return jsonify({
        'status':'success',
        'data': contacts

    })
  

if(__name__=='__main__'):
    app.run(debug = True)
    