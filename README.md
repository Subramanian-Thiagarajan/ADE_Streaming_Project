# ADE_Streaming_Project

1. Store Incoming data in IoT Hub or Event Hub
2. Connect Stream Analytics Job to the Event Hub to analyse the incoming data.
3. Push the filtered data to Service Bus topic. And store all the data for further processing partitioned by Bus ID and date
4. Trigger Logic App when a record is pushed to Service Bus Topic.


Input: JSON data with a specific format
Output: Trigger an email to Company

![image](https://github.com/Subramanian-Thiagarajan/ADE_Streaming_Project/assets/96657323/c265d257-0411-48b5-afc0-9b89010e8643)
