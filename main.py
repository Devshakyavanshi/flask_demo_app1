from flask import Flask
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    return ('HELLO THIS IS DEMO FLASK APP')

if __name__=='__main__':
    app.run(debug=True)
