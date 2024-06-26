To start all the services run from within the microService directory 

`docker-compose up --build`

There are following components

RabbitMQ: For event drivien inter-service communication

api_gateway: RESR API Gateway. Sits between the browser and the micro services.

meterData service: A gRPC  service 

notification: It is runs of two seperate conainers
    1. It runs a listener of the event queue that pulls notification messages
    2. It runs a websocket server that manages connections and push the notification messages to the browser via websocket protocol

Redis: Used for the django channels used in the notification service

RabbitMQ: Acts as the async event/message queue


Test using postman:

Make a GET request at http://127.0.0.1:8000/api/MeterReadings
You should recieve a JSON  response
The API gateway parses the URL and finds the Django view
The Django view discovers the gRPC service and makes a request via the gRPC client. Recieves the response and sends it as a JSON response to Postman.

Make a POST request at http://127.0.0.1:8000/api/MeterReadings with payload {"start_date": "2020-08-01", "end_date": "2024-12-31", "meter_id": 11}
also open a browser tab with address http://localhost:8000/notifications/
1. In postman, you should recieve a JSON  response
2. The API gateway parses the URL and finds the Django view
3. The Django view discovers the gRPC service and makes a request via the gRPC client. 
4. The grpc service creates the data based on the request. The grpc service also sends a notifcation-message to the rabbitMQ.
5. Sends a response to the api-gateway. Api-gateway recieves the response and sends it as a JSON response to Postman.
6. The notification service's listener pulls the message from step 4 and forwards it to the websocket server via django-channels (Redis is required here. But it can be replaced by RabbbitMQ)
7. The notificatio service's websocket server pushes the message to the opened browser tab.

