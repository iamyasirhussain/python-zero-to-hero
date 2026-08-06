from datetime import datetime
import random

def make_deploy_id(app_name):
    time = datetime.now().strftime("%Y%m%d")
    number = random.randint(1000, 9999)

    return f"{app_name}-{time}-{number}"

print(make_deploy_id("payments-api"))
print(make_deploy_id("auth-service"))
