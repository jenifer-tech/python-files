from flask import*
app=Flask(__name__)

@app.route('/admin/<admi>')

def hello_admin(admi):
    return 'Hello %s You are Admin' %admi

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Helo %s as guest " %guest     
@app.route('/user/<name>')    
def hello_user(name):
    if name=='jeni':
        return redirect(url_for('hello_admin',admi=name))
    else:
        return redirect(url_for('hello_guest',guest=name) )    

if __name__=='__main__':
    app.run(debug=True)
             



