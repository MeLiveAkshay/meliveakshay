def init_dashboard_routes(app):
    @app.route('/dashboard', methods=['GET'])
    def dashboard():
        return 'dashboard showing live here'