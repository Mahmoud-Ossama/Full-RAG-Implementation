from enum import Enum 

class ResponseSignal(Enum):
    SUCCESS = "Done!"
    FILE_NOT_SUPPORTED = "file not supported"
    FILE_TOO_LARGE = "file exceeded max size 10MB"
    PROCESSING_FAILED = "failed to chunk the file"
    PROCESSING_SUCCESS = "file chunked successfully"