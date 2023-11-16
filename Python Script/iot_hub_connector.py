from azure.iot.device.aio import IoTHubDeviceClient

import random
import datetime
import time
import json
import asyncio

async def sendToIotHub(connectionString,data):
    try:
        # Create an instance of the IoT Hub Client class
        device_client = IoTHubDeviceClient.create_from_connection_string(connectionString)

        # Connect the device client
        await device_client.connect()

        #Send the message
        await device_client.send_message(data)
        print("Message sent to IoT Hub:", data)

        # Shutdown the client
        await device_client.shutdown()
        
    
    except Exception as e:
        print("Error:", str(e))