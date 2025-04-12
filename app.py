#import 
from flask import Flask
from routes.main import init_main_routes
from admin.admin import init_admin_routes
from admin.api import init_api_routes
from admin.dashboard import init_dashboard_routes
#inisalization
app = Flask(__name__)
init_main_routes(app)
init_admin_routes(app)
init_api_routes(app)
init_dashboard_routes(app)

#main function
if __name__ == '__main__':
    app.run(debug=True, port=8000,host='0.0.0.0')
