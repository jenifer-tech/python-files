from flask import*
app=Flask(__name__)

@app.route('/fact/<int:n>')

def fact(n):
   
    factorial = 1
    if n<0:
        return "enter positive value"
    elif n==0:
        return "factorial of 0 is 1"
    else: 
        for i in range(1,n+1):
            factorial=factorial*i
        return "The factorial of",n, "is",factorial
    

if __name__=='__main__':
    app.run(debug=True)