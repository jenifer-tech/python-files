from flask import*
app=Flask(__name__)
app.config["DEBUG"]=True

@app.route('/',methods=['GET'])

def hello1():
    return "Hai!  this is my first flask program.   "
if __name__=="__main__":   
    app.run()
