# Azure Streaming Project

## Problem: 
Private intercity buses cross speeds of 120kmph+ often leading to accidents and less safety of passengers and other vehicles.

## Solution
- This project involves tracking of speeds of buses including the location and sends email notifications with a fine to the bus owners when the speed limit exceeds 125kmph.
- This will ensure that buses follow safer speeds and ensure safety of passengers and other vehicles

## Implementation

![image](https://github.com/Subramanian-Thiagarajan/ADE_Streaming_Project/assets/96657323/959e9019-e66e-46f9-befc-7e7ac4999307)

### 1. Python Code simulation of IoT devices attached to bus
- Code written in python to simulate the IoT devices attached to the buses which will send telemetry data including speed and location.
- This code will send data in json format to Azure Iot Hub. Code attached in the repo.

### 2. Create IoT Hub and add the devices to it.
- Add 3 devices to IoT Hub and add the primary connection string to the python code.
  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Streaming_Project/assets/96657323/8f14d519-9c92-44f0-b225-aee29cad1ee6)

### 3. Create ADLS Gen 2 and Service Bus Queue
- Create ADLS Gen 2 to store the raw data. Folders are created for each bus automatically by giving partition path condition in stream analytics job.
  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Streaming_Project/assets/96657323/53f1cb24-ed78-45f8-a7b4-95cff2579f18)

- Create Service Bus Queue to enqueue the required details for the email notification crossing 125kmph

### 3. Create Azure Stream analytics job
- Add IoT Hub as input.
- ADLS Gen 2 and Service Bus as output.
  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Streaming_Project/assets/96657323/06ac4973-f0bc-464e-aad2-be884a13af35)


### 4. Create a Logic App to send email when a message is received in the queue.
- Create Logic App and add the component as follows
  ![image](https://github.com/Subramanian-Thiagarajan/ADE_Streaming_Project/assets/96657323/64f4ac4d-eeec-4236-b027-4035fa1a960b)

### 5. Output of Email received
![image](https://github.com/Subramanian-Thiagarajan/ADE_Streaming_Project/assets/96657323/74d7f9ae-d6f1-4741-9a93-aab85cc26a10)
