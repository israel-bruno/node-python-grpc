from concurrent import futures
import logging

import grpc
from proto.recognition_pb2 import Request, Response
from proto.recognition_pb2_grpc import RecognizerServicer, add_RecognizerServicer_to_server
from recognizer import recognizeFace


class Recognizer(RecognizerServicer):
    def SendMessage(self, request: Request, context):
        result = recognizeFace(request.name, request.image)
        return Response(message=result)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_RecognizerServicer_to_server(Recognizer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
