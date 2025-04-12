from flask import render_template_string,jsonify
def init_admin_routes(app):
    @app.route('/admin')
    def admin():
        return jsonify (
            {
                'admin':'admin class is here to help and control the'
                'all activity of the website'
            }
        )