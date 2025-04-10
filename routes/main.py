
from flask import render_template
def init_main_routes(app):
    @app.route('/')
    def hello():
        return render_template('index.html')
    