from locust import HttpUser, task
import time

class LoadGenerator(HttpUser):

    host = "http://172.21.0.1:8090"

    @task
    def call_benchmarkapp(self):
        response = self.client.get("/primecheck")
        print('{}, user {} call benchmarkapp, url: {} , result: {}'.format(time.strftime('%H:%M:%S'), self, response.url, response.text))
