from flask import*
app=Flask(__name__)
@app.route('/')
def admin1():
    return  "Hello Admin"
@app.route('/guest1/<gname>')
def guest1(gname):
    return "You are %s" %gname
@app.route('/user1/<uname>')    
def user1(uname):
    if uname=='admin':
        return redirect(for_url("admin"))
    else:
        return redirect(for_url("guest",gname=uname))    
if __name__=='__main__':
    app.run(debug=True)        



