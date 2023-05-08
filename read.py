import influxdb_client, os, time
from influxdb_client import InfluxDBClient, QueryApi

def init_client():
    token = "gPtM-AAoqNMaeqHO-2w8XnhoL0vdLkPTlk-LRk8ZWwlhVTqwZW6YlfUOgjd6oyQbD_ZFca1WSjVoPCqD-agm5w=="
    org = "my-org"
    url = "http://35.240.148.191:8086"
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    return client 

def read_data(client):
    print("Reading")
    query = 'from(bucket: "my-bucket")\
        |> range(start: -1h)\
        |> filter(fn: (r) =>\
            r._measurement == "energy_consumption" and\
            r._field == "power_usage_watts" and\
            r.device_type == "light" or r._device == "co2"\
            )'
    query_api = client.query_api()
    result = query_api.query(query=query)
    for table in result:
        for row in table:
            print(row)

client = init_client()
start_time = time.time()
result = read_data(client)
elapsed_time = time.time() - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")