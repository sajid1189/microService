from django.shortcuts import render
import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

logger = logging.getLogger(__name__)


from django.shortcuts import render
from rest_framework.exceptions import ValidationError
# Create your views here.
from django.http import JsonResponse
import grpc
from django.views.decorators.csrf import csrf_exempt

from meter_data.grpc_clients import meter_pb2, meter_pb2_grpc


class MeterReadingsViewSet(APIView):
    """Endpoint for meter readings."""

    grpc_address = "grpc-service:50051"

    def get(self, request):
        # Extract parameters from the request
        start_date = self.request.GET.get("start_date", "2022-01-01")
        end_date = self.request.GET.get("end_date", "2022-01-31")
        meter_id = int(self.request.GET.get("meter_id", 0))

        # Call the gRPC service

        with grpc.insecure_channel(self.grpc_address) as channel:
            stub = meter_pb2_grpc.MeterServiceStub(channel)
            grpc_request = meter_pb2.ReadingRequest(
                start_date=start_date, end_date=end_date, meter_id=meter_id
            )
            grpc_response = stub.GetReadings(grpc_request)

        # Convert the gRPC response to JSON
        readings = [
            {
                "value": reading.value,
                "created_at": reading.created_at,
                "source": reading.source,
            }
            for reading in grpc_response.readings
        ]

        return JsonResponse({"readings": readings}, status=200)

    def post(self, request, *args, **kwargs):
        d = self.request.data
        errors = []
        reading_pb = meter_pb2.MeterDataPayload()
        try:
            reading_pb.meter_serial = d["meter_serial"]
        except Exception as e:
            errors.append(str(e))

        try:
            reading_pb.timestamp = d["timestamp"]
        except Exception as e:
            errors.append(str(e))

        try:
            reading_pb.channel = int(d["channel"])
        except Exception as e:
            errors.append(str(e))

        try:
            reading_pb.value = float(d["value"])
        except Exception as e:
            errors.append(str(e))

        try:
            reading_pb.source = d["source"]
        except Exception as e:
            errors.append(str(e))

        try:
            reading_pb.reading_reason = d["reading_reason"]
        except Exception as e:
            errors.append(str(e))
        if errors:
            raise ValidationError(errors)
        response_error = None
        status_code = 201
        with grpc.insecure_channel(self.grpc_address) as channel:
            stub = meter_pb2_grpc.MeterServiceStub(channel)
            try:
                response = stub.CreateReadings(reading_pb)
                print(f"received response {response}")
                # Process the response
            except grpc.RpcError as e:
                if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                    status_code, response_error = 400, f"Invalid argument error: {e.details()}"
                elif e.code() == grpc.StatusCode.INTERNAL:
                    status_code, response_error = 500, f"Internal server error: {e.details()}"
                elif e.code() == grpc.StatusCode.UNKNOWN:
                    status_code, response_error = 500, f"Unknown error: {e.details()}"
                else:
                    status_code, response_error = 500, f"An error occurred: {e.code()}: {e.details()}"
            except Exception as e:
                status_code, response_error = 500, f"An unknown error occurred"
            # Convert the gRPC response to JSON
        if response_error:
            return JsonResponse({"error": response_error}, status=status_code)
        return JsonResponse({"readings": 1}, status=status_code)


def notifications_view(request):
    return render(request, "notifications.html")