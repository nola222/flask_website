# -*- coding: utf-8 -*- 
# @Time : 2021/4/24 19:22 
# @Author : Nola
# @File : app
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    title = 'Home'
    paragraphs = [
        'Section 1',
        'Section 2',
        'Section 3',
    ]
    return render_template('index.html', title=title, data=paragraphs)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
