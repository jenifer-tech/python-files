from flask import*
app=Flask(__name__)
app.config["DEBUG"]=True

@app.route('/<int:name>')

def hello1(name):
    return render_template("hello.html",a=name)
if __name__=="__main__":   
    app.run()
