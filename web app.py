from flask import Flask
app=Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return "welcome home python !"
if __name__=='__main__':
    app.run('localhost',5050)
