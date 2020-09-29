from flask import*
app=Flask(__name__)

@app.route('/ad/<float:no1>/<int:no2>')

def addd(no1,no2):
    x=no1+no2
    return "You are entered {}  and {} is {}".format(no1,no2,x)
    

if __name__=='__main__':
    app.run(debug=True)