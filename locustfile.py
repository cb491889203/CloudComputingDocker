from locust import HttpUser, task


class HelloWorldUser(HttpUser):

    @task
    def hello_world(self):
        pass