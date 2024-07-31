
from flask import Flask, Blueprint

# Flask 객체 인스턴스 생성
app = Flask(__name__)

def create_app():
    app = Flask(__name__)

@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'


if __name__=="__main__":
    app.run(debug=True)
