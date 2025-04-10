def init_main_routes(app):
    @app.route('/')
    def hello():
        return 'Hello World!'
    