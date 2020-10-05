from flask import*
app=Flask(__name__)

@app.route('/age/<int:n>')


def age(n):
    if n>=18:
        return "You are elligible for vote"
    else:
        return "You are  notelligible for vote"    

if __name__=='__main__':
    app.run(debug=True)









