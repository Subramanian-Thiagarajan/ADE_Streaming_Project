from iot_hub_connector import sendToIotHub
import asyncio, json, datetime, random, time

if __name__ == "__main__":
    connectionString = "HostName=iothub-bus-speed-tracking.azure-devices.net;DeviceId=bus2;SharedAccessKey=okzPD99fXf6BAdidTNBvX/uJZgdvct0JbAIoTG88Di4="
    while True:
        speed = random.randint(110, 130)
        longitude = random.randint(-180, 180)
        latitude = random.randint(-90,90)
        data={
            "bus_id":"BI456",
            "longitude": longitude,
            "latitude": latitude,
            "speed": speed,
            "timestamp": str(datetime.datetime.now())
        }
        asyncio.run(sendToIotHub(connectionString=connectionString,data=json.dumps(data)))
        time.sleep(60)