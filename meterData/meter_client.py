import grpc
import meter_pb2
import meter_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = meter_pb2_grpc.MeterServiceStub(channel)
        request = meter_pb2.ReadingRequest(
            start_date="2024-01-01", end_date="2024-01-31", meter_id=123
        )
        response = stub.GetReadings(request)
        for reading in response.readings:
            print(
                f"Value: {reading.value}, Created At: {reading.created_at}, Source: {reading.source}"
            )


if __name__ == "__main__":
    run()
