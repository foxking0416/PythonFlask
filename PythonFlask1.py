from flask import Flask
app = Flask(__name__)
@app.route("/")
@app.route('/data/appInfo/<name>', methods=['GET'])

def queryDataMessageByName(name):
    print("type(name) : ", type(name))
    return 'String => {}'.format(name)

if __name__ == '__main__':
    app.run()

#訪問 : http://127.0.0.1:5000/data/appInfo/FlaskSE