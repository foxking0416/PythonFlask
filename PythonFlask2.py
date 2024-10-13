from flask import Flask
app = Flask(__name__)
@app.route("/")
@app.route('/data/appInfo/id/<int:id>', methods=['GET'])

def queryDataMessageById(id):
    print("type(id) : ", type(id))
    return 'int => {}'.format(id)

if __name__ == '__main__':
    app.run()

#訪問 : http://127.0.0.1:5000/data/appInfo/id/5