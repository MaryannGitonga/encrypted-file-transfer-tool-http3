from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileTransferRequest(_message.Message):
    __slots__ = ["fileContents", "fileName", "fileSize"]
    FILECONTENTS_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILESIZE_FIELD_NUMBER: _ClassVar[int]
    fileContents: bytes
    fileName: bytes
    fileSize: bytes
    def __init__(self, fileName: _Optional[bytes] = ..., fileSize: _Optional[bytes] = ..., fileContents: _Optional[bytes] = ...) -> None: ...

class FileTransferResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
