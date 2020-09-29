from flask import*
app=Flask(__name__)
app.config["DEBUG"]=True

@app.route('/hello')

def first():
    return render_template("home.html")

@app.route('/second',methods=["post"])

def second():
    name=request.form["uname"]
    return "Username is" +name

if __name__=="__main__":   
    app.run()
