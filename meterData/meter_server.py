from concurrent import futures
import grpc
import meter_pb2
import meter_pb2_grpc
from datetime import datetime

from notification_client import notify_data_creation


class MeterServiceServicer(meter_pb2_grpc.MeterServiceServicer):
    def GetReadings(self, request, context):
        # Dummy data for demonstration
        readings = [
            meter_pb2.Reading(
                value=100, created_at="2024-01-01T12:00:00Z", source="sensor1"
            ),
            meter_pb2.Reading(
                value=200, created_at="2024-01-02T12:00:00Z", source="sensor2"
            ),
            meter_pb2.Reading(
                value=150, created_at="2024-01-03T12:00:00Z", source="sensor3"
            ),
        ]

        print(request.start_date, request.end_date, request.meter_id)

        # Normally, you would filter and process data based on request parameters
        response = meter_pb2.ReadingResponse(readings=readings)
        return response

    def CreateReadings(self, request, context):
        s = f"{request.start_date}, {request.end_date}, {request.meter_id}"
        print(f"-----created meter data with: {s}")
        notify_data_creation(message=f"created meter with {s}")
        return meter_pb2.ReadingCreateResponse(id=100)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meter_pb2_grpc.add_MeterServiceServicer_to_server(MeterServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
