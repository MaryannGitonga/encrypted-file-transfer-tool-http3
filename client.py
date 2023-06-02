from __future__ import print_function
import logging, os, grpc
from file_transfer_pb2 import FileTransferRequest
from file_transfer_pb2_grpc import FileTransferServiceStub
from encrypt_decrypt import Cipher

def transfer_file(stub: FileTransferServiceStub) -> None:
    file_name = 'test_file.txt'
    with open(file_name, 'rb') as file:
        data = file.read()

    fileTransferReq = FileTransferRequest(
        fileName=Cipher.encrypt(file_name.encode()),
        fileSize=Cipher.encrypt(str(os.path.getsize(file_name)).encode()),
        fileContents=Cipher.encrypt(data)
    )
    file_response = stub.SendFile(fileTransferReq)
    # file_future_response = stub.SendFile.future(fileTransferReq)

    print(f'Server Response: {file_response.message}')
    return

def run() -> None:
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50000') as channel:
        stub = FileTransferServiceStub(channel)
        print("-------------- File Transfer --------------")
        transfer_file(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()