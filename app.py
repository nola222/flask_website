# -*- coding: utf-8 -*- 
# @Time : 2021/4/24 19:22 
# @Author : Nola
# @File : app
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Flask APP'
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
