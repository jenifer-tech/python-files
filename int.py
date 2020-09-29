from flask import*
app=Flask(__name__)

@app.route('/blog/<int:ID>',methods=['GET'])

def show_blog(ID):
    return 'Blog no %d ' %ID 

 
if __name__=='__main__':
    app.run(debug=True)