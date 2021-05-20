import time
import os
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
from app import get_response_time, get_urls

class CustomCollector(object):
    def __init__(self):
      pass

    def collect(self):
      g = GaugeMetricFamily("simple_http_response", "Tiempo de Respuesta", labels=['url'])
      for url in get_urls():
        g.add_metric([url],get_response_time(url)) 
      yield g

if __name__ == '__main__':
    start_http_server(5530)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)

