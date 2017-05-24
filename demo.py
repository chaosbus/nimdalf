from flask import Flask
from flask import render_template_string, render_template
from flask import redirect, url_for
from app import create_app


# app = Flask(__name__)


# @app.route('/asdf')
# def hello_wonrld():
#     return 'Hello World!'


if __name__ == '__main__':
    app = create_app()

    @app.route('/redirect')
    def f1():
        return redirect('http://www.baidu.com')

    @app.route('/')
    def f2():
        print 'hahah'
        print url_for('api.index', _external=True)
        ss = '''<li><a href="{{ url_for('api.index') }}">API.</a></li>
        <li><a href="{{ url_for('admin.index') }}">Admin.</a></li>'''
        return render_template_string(ss)

    app.run(port=30000)
