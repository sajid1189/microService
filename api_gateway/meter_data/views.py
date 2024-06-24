from django.shortcuts import render
import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

logger = logging.getLogger(__name__)


from django.shortcuts import render

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
        start_date = self.request.data.get("start_date", "2022-01-01")
        end_date = self.request.data.get("end_date", "2022-01-31")
        meter_id = int(self.request.GET.get("meter_id", 0))
        with grpc.insecure_channel(self.grpc_address) as channel:
            stub = meter_pb2_grpc.MeterServiceStub(channel)
            grpc_request = meter_pb2.ReadingRequest(
                start_date=start_date, end_date=end_date, meter_id=meter_id
            )
            grpc_response = stub.CreateReadings(grpc_request)

            # Convert the gRPC response to JSON

        return JsonResponse({"readings": grpc_response.id}, status=201)


def notifications_view(request):
    return render(request, "notifications.html")