
from influxdb import InfluxDBClient


json_file = []
tags = client_source.select_query('db_cible', 'show TAG KEYS from "%s";' % table)[1]
tags_type = client_source.select_query('db_cible', 'show field TAG KEYS from "%s";' % table)[1]

fields_type = {}




for j in range(len(data)):
  line = data.iloc[j]
  line['host'] = 'linxo'
  tags_dict, fields_dict = {}, {}
  for i in range(len(tags)):
    tags_dict[tags[i]] = line[tags[i]]
    del line[tags[i]]
  colonnes = list(set(data.columns) - set(tags))
  for col in colonnes:
    fields_dict[col] = line[col]
  current_time = '2019-06-01T00:00:00Z'
  dict_2_push = {
    "measurement": '%s' % table,
    "tags": tags_dict,
    "fields": fields_dict,
    "time": current_time
  }
  json_file.append(dict_2_push)
  
client = InfluxDBClient(host=host, port=port)
client.write_points('db_cible', json_file)




# pip install influxdb-client

from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "token"
org = "organization name"
bucket = "bucket name"

# Option 1
with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
  write_api = client.write_api(write_options=SYNCHRONOUS)
  data = "mem,host=host1 used_percent=23.43234543"
  write_api.write(bucket, org, data)
  
# Option 2
with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
  write_api = client.write_api(write_options=SYNCHRONOUS)
  point = Point("mem") \
    .tag("host", "host1") \
    .field("used_percent", 23.43234543) \
    .time(datetime.utcnow(), WritePrecision.NS)
  write_api.write(bucket, org, point)
  
# Option 3
with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
  write_api = client.write_api(write_options=SYNCHRONOUS)
  sequence = ["mem,host=host1 used_percent=23.43234543",
            "mem,host=host1 available_percent=15.856523"]
  write_api.write(bucket, org, sequence)

  
  
query = 'from(bucket: "test") |> range(start: -1h)'
tables = client.query_api().query(query, org=org)
for table in tables:
    for record in table.records:
        print(record)

client.close()
  
  
  

  
