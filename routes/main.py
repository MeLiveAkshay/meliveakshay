from flask import render_template,jsonify
def init_main_routes(app):
    @app.route('/')
    def hello():
        return render_template('index.html')
    
    @app.route('/contact')
    def contact():
        return jsonify({
            'Status':'Contact Page is here'
        })

    @app.route('/portfolio')
    def portfolio():
        return 'Portfolio'

    @app.route('/career')
    def career():
        return 'career page is live here'