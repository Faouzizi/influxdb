from influxdb import InfluxDBClient
import pandas as pd


class influxdb_connexion:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def show_databases(self):
        client = InfluxDBClient(host=self.host, port=self.port)
        return client.get_list_database()
    
    def show_tables(self, db):
        client = InfluxDBClient(host=self.host, port=self.port)
        client.switch_database(db)
        return client.get_list_measurements()
    
    def select_query(self, db, query_str):
        client = InfluxDBClient(host=self.host, port=self.port)
        client.switch_database(db)
        results = client.query(query_str)
        raws = results.raw['series'][0]
        colonnes = raws['columns']
        df = pd.DataFrame(raws['values'], columns=colonnes)
        return df
        


if __name__ == '__main__':
  client = influxdb_connexion(host='host', port='port')
  client.show_databases()
  client.show_tables('db')
  results = client.select_query('db','SELECT * FROM table limit 10;')

