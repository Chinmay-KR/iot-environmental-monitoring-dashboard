import pandas as pd
import random
import time
from datetime import datetime

file = "live_sensor_data.csv"

# create file with headers if it doesn't exist
try:
    pd.read_csv(file)
except:
    df = pd.DataFrame(columns=["timestamp","temperature","humidity","smoke"])
    df.to_csv(file,index=False)

while True:

    timestamp = datetime.now()

    temperature = random.uniform(26, 32)
    humidity = random.uniform(55, 70)
    smoke = random.randint(100, 140)

    new_data = pd.DataFrame({
        "timestamp":[timestamp],
        "temperature":[temperature],
        "humidity":[humidity],
        "smoke":[smoke]
    })

    new_data.to_csv(file, mode='a', header=False, index=False)

    print("New Sensor Data:", new_data)

    time.sleep(5)