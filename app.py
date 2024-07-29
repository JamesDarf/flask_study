
#app.py
from flask import Flask, render_template, request

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
    # return render_template('index.html', user="modori205", data={'level':60, 'point': 360, 'exp':45000})
    if request.method == "POST": # 전송 방식이 POST일 경우
        # user=request.form['user'] # 전달받은 name이 user인 데이터
        print(request.form.get('user'))
        user = request.form.get('user')
        data = {'level': 60, 'point': 360, 'exp': 45000}
        return render_template('index.html', user=user, data=data)
    elif request.method == "GET" : # 전송 방식이 GET일 경우
        user = "modori205"
        data = {'level': 60, 'point': 360, 'exp': 45000}
        return render_template('index.html', user=user, data=data)

if __name__=="__main__":
    app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    # app.run(host="127.0.0.1", port="5000", debug=True)
