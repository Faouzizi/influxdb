
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
