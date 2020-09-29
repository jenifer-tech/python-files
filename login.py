from flask import*
app=Flask(__name__) 
@app.route('/')
def login():
    return render_template('login.html')
    
@app.route('/login', methods=["post","get"])    
def log():
    database={"jenifer":"123","merlin":"jeba"}
    a=request.form["usname"]
    b=request.form['pwd']
    if a not in database:
        return render_template("login.html",info="Invalid User")
    else:
        if database[a]!=b:
            return render_template("login.html",info="Invalid password")  
              
        else:
            return render_template("home1.html",name=a)   
            return redirect(url_for("login"))

if __name__=='__main__':
    app.run(debug=True)



