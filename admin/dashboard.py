def init_dashboard_routes(app):
    @app.route('/dashboard')
    def dashboard():
        return 'dashboard showing live here'