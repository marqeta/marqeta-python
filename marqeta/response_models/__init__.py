import re
from datetime import datetime, date

DATE_FORMATS = [
    "%Y-%m-%dT%H:%M:%S.%f%z",
    "%Y-%m-%d%T%H:%M:%S.%f%z",  # yyyy-MM-dd'T'HH:mm:ss.SSSZ
    "%Y-%m-%dT%H:%M:%S.%fZ",
    "%Y-%m-%d%T%H:%M:%S.%fZ",
    "%a, %d %b %Y %H:%M:%S %Z",  # yyyy-MM-dd'T'HH:mm:ss.SSS'Z'
    "%Y-%m-%dT%H:%M:%SZ",
    "yyyy-MM-ddThh:mm:ssZ",
    "%d %b %Y %H:%M:%S %f%z",  # dd MMM yyyy HH:mm:ss zzz
    "%d %b %Y %H:%M:%S %z",
]


def datetime_object(key, json_response):
    if key in json_response:
        match = re.match("\d{4}[-/]\d{2}[-/]\d{2}$", json_response[key])
        if match:
            return datetime.strptime(json_response[key], "%Y-%m-%d").date()
        else:
            for format in DATE_FORMATS:
                try:
                    return datetime.strptime(json_response[key], format)
                except ValueError:
                    pass
