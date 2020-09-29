from flask import*
app=Flask(__name__)

@app.route('/even/<int:n>')

def odd_even(n):
    if n%2==0:
        return "You are entered {}   is even no".format(n)
    else:
        return "You are entered {}   is odd no".format(n)    

if __name__=='__main__':
    app.run(debug=True)