from concurrent import futures
import grpc
import meter_pb2
import meter_pb2_grpc
from datetime import datetime
from django.conf import settings


from notification_client import notify_data_creation
from google.protobuf.json_format import MessageToDict

from django.db import IntegrityError

class MeterServiceServicer(meter_pb2_grpc.MeterServiceServicer):
    def GetReadings(self, request, context):
        import django
        import os
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.orm.settings")
        django.setup()
        from orm.meter_data.serializers import MeterReadingSerializer
        from orm.meter_data.models import Data
        Data.objects.count()
        # Dummy data for demonstration
        print(f"total meter readings {Data.objects.count()}")
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
        import django
        import os
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.orm.settings")
        django.setup()
        from orm.meter_data.serializers import MeterReadingSerializer
        from orm.meter_data.models import Data
        request_dict = MessageToDict(request, preserving_proto_field_name=True)
        print(f"request payload {request_dict}")
        instance = None
        serializer = MeterReadingSerializer(data=request_dict)
        if serializer.is_valid():
            print(f"serializer is invalid")
            # Create the object if data is valid
            try:
                instance = serializer.save()
            except IntegrityError as e:
                print(f"integrity error: {e}")
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, f"{e}")
            except Exception as e:
                print(f"Unknown error: {e}")
                context.abort(grpc.StatusCode.UNKNOWN, f"{e}")
        else:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, f"invalid request payload: {serializer.errors}")

        if instance:
            notify_data_creation("created")
            return meter_pb2.ReadingCreateResponse(id=instance.id if instance else -1)

def serve():


    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meter_pb2_grpc.add_MeterServiceServicer_to_server(MeterServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
