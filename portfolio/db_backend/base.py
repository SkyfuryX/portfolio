from django.db.backends.postgresql.base import DatabaseWrapper as PostgresWrapper
import boto3, time
from psycopg2 import OperationalError
from dotenv import dotenv_values

config = dotenv_values('./.env')

class DatabaseWrapper(PostgresWrapper):        
    
    def get_connection_params(self):
        conn_params = super().get_connection_params()
        auth_token = boto3.client('rds', region_name=config['REGION']).generate_db_auth_token(
            DBHostname=conn_params['host'], 
            Port=int(conn_params['port']), 
            DBUsername=conn_params['user'], 
            Region=config['REGION'])
        conn_params['password'] = auth_token     
        return conn_params
    
    def get_new_connection(self, conn_params):
        retries = 0
        while retries < 3:
            try:
                conn_params = self.get_connection_params()
                connection = super().get_new_connection(conn_params)
                return connection
            except OperationalError as e:
                retries +=1
                if retries >= 3:
                    raise e
                time.sleep(5)
            except Exception as e:
                raise e         
            
                
        
        