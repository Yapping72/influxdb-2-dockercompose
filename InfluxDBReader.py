import time 
import sys 
from influxdb_client import InfluxDBClient, QueryApi, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

INFLUXDB_TOKEN = "gPtM-AAoqNMaeqHO-2w8XnhoL0vdLkPTlk-LRk8ZWwlhVTqwZW6YlfUOgjd6oyQbD_ZFca1WSjVoPCqD-agm5w=="
INFLUXDB_ORG = "my-org"
URL = "http://35.240.148.191:8086"

class InfluxDBReader:
    def __init__(self):
        # Instantiates InfluxDB client, uses the Sensor (Testing) Bucket by default
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.bucket_name = "Sensors (Testing)"
    
    