from app1.models.views import app2
from app1.models.tables import Migration



if __name__ == "__main__":
    db_conn = Migration()
    db_conn.drop_tables()
    db_conn.create_tables()  
    app2.run(debug=True, port=8080)