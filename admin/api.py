from flask import jsonify
def init_api_routes(app):
    @app.route('/api')
    def api():
        return 'api is here';


    @app.route('/api/v1/admin/login', methods=['POST'])
    def admin_login():
        return jsonify({
            'status':200,
            'massage':'log in successfully on the admin dashboard'
        })