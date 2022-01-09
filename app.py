# File encoding: UTF-8

from flask import Flask

from component.html_factory import Base

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ins_base = Base()
    return ins_base.get_html()


if __name__ == '__main__':
    app.run(debug=True, port=5000)

