from flask import*
app=Flask(__name__) 
@app.route('/hai')
def name():
    return render_template('student.html')
@app.route('/sname', methods=["post"])    
def valu():
    a=request.form["stname"]
    return "STUDNET NAME:  "+a
    

if __name__=='__main__'   :
    app.run(debug=True) 
