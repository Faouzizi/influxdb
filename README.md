# influxdb

I. Installs on mac
    1. Install influxdb 
      brew install influxdb 
    2. Install CLI 
      brew install influxdb-cli
      
II. Launch Influxdb 
  - influxd
  - Go to another terminal and execute 'influx ping' the result should be 'OK'
  - You can create users access by using influxdb UI : http://localhost:8086/ 
  - Or by the CLI using following command

III. If you forget the admin password you can reset it by deleting : rm -rf ~/.influxdbv2
