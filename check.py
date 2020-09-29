from flask import*
app=Flask(__name__)

@app.route('/no/<float:no1>/<int:no2>')

def nfloat(no1,no2):
    return "You are entered {}  and {}".format(no1,no2)

if __name__=='__main__':
    app.run(debug=True)
