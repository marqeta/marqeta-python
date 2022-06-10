from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class FileProcessingResponse(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):
        if "created_time" in self.json_response:
            return datetime_object("created_time", self.json_response)

    @property
    def last_modified_time(self):
        if "last_modified_time" in self.json_response:
            return datetime_object("last_modified_time", self.json_response)

    @property
    def token(self):
        return self.json_response.get("token", None)

    @property
    def file_process_type(self):
        return self.json_response.get("file_process_type", None)

    @property
    def source_file(self):
        return self.json_response.get("source_file", None)

    @property
    def archive_file(self):
        return self.json_response.get("archive_file", None)

    @property
    def file_process_status(self):
        return self.json_response.get("file_process_status", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.file_processing_response.FileProcessingResponse>"
            + self.__str__()
        )
