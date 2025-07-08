import pymysql

def get_db_connection():
    try:
        connection = pymysql.connect(
            host='mysql-controle-ru-controle-ru.k.aivencloud.com', 
            port=19833,
            user='avnadmin',            
            password='AVNS_lLQ9cx9O1nNeqxgOQ64',          
            db='defaultdb',     
            cursorclass=pymysql.cursors.DictCursor,
            connect_timeout=30 
        )
        return connection
    except Exception as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        raise e
