from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
import sqlalchemy



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Phase5'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://pxk5233:DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu'
    # db.init_app(app)
    # user = 'pxk5233'
    # pw = 'DatabasePraveen30'
    # host = 'az6F72ldbp1.az.uta.edu'
    # port = '1523'
    # db = 'pcse1p.data.uta.edu'
    # engine = sqlalchemy.create_engine('oracle+cx_oracle://' + user + ':' + pw + '@' + host + ':' + port + '/?service_name=' + db)
    

    # with conn as con:
    #     with open("Website/models/projectDBcreate.sql") as file:
    #         query = text(file.read())
    #         con.execute(query)
    # conn.execute("CREATE TABLE Fall22_S004_13_SERVICE(SSID INT PRIMARY KEY, S_TYPE VARCHAR(50) NOT NULL);")
    # print('Table created')
    from .views import views



    app.register_blueprint(views, url_prefix='/')

    return app    
