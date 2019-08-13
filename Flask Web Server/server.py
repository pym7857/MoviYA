from flask import Flask, render_template, request
import numpy as np
import datetime

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
      return render_template('index.html')
    if request.method == 'POST':
        avg_temp = float(request.form['avg_temp'])    # 서버로부터 받아옴
        min_temp = float(request.form['min_temp'])
        max_temp = float(request.form['max_temp'])
        rain_fall = float(request.form['rain_fall'])

    price = 0   # price 변수 생성

    data = ((avg_temp, min_temp, max_temp, rain_fall),)
    arr = np.array(data, dtype=np.float32)

    x_data = arr[0: 4]

    price = x_data[0]
    return render_template('index.html', price=price)   # 서버로 price 변수값 보냄

if __name__ == '__main__':
    app.run(debug=True)