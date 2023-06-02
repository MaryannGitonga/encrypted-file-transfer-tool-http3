from concurrent import futures
import grpc, time, os, logging
from file_transfer_pb2_grpc import FileTransferServiceServicer, add_FileTransferServiceServicer_to_server
from file_transfer_pb2 import FileTransferResponse
from encrypt_decrypt import Cipher

class FileTransferServicer(FileTransferServiceServicer):
    def SendFile(self, request, context):
        fileName = Cipher.decrypt(request.fileName).decode()
        fileSize = Cipher.decrypt(request.fileSize).decode()

        print('Received file:', fileName)

        start_time = time.time()

        # Open the file and write the data received from the client
        new_file_name = os.path.splitext(fileName)[0] + "_sent" + os.path.splitext(fileName)[1]
        with open(new_file_name, 'wb') as file:
            data = request.fileContents
            file.write(Cipher.decrypt(data))

        end_time = time.time()
        return FileTransferResponse(message=f"Time taken: {end_time - start_time}, File saved: {new_file_name}")
    

def serve() -> None:
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  add_FileTransferServiceServicer_to_server(
      FileTransferServicer(), server)
  server.add_insecure_port('[::]:50000')
  server.start()
  server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()