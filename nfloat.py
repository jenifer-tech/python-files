from flask import*
app=Flask(__name__)

@app.route('/no/<float:no1>')

def nfloat(no1):
    return "You are entered %f " %no1

if __name__=='__main__':
    app.run(debug=True)
