class Friend:
    def __init__(self):
        self.job = "None"

    def get_job(self):
        return self.job
    
    def set_job(self, job):
        self.job = job
    
Alice = Friend()
Bob = Friend()

Alice.set_job("Carpenter")
Bob.set_job("Builder")

print(Bob.job, Alice.job)