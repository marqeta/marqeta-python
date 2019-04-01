from datetime import datetime, date
import json


class CronJobInfo(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def schedule(self):
        return self.json_response.get('schedule', None)

    @property
    def group(self):
        return self.json_response.get('group', None)

    @property
    def id(self):
        return self.json_response.get('id', None)

    @property
    def class_cron(self):
        return self.json_response.get('class', None)

    @property
    def is_running(self):
        return self.json_response.get('is_running', None)

    @property
    def last_run_duration_millis(self):
        return self.json_response.get('last_run_duration_millis', None)

    @property
    def next_run(self):
        if 'next_run' in self.json_response:
            return datetime.strptime(self.json_response['next_run'], '%Y-%m-%d').date()

    @property
    def last_run(self):
        if 'last_run' in self.json_response:
            return datetime.strptime(self.json_response['last_run'], '%Y-%m-%d').date()

    @property
    def timezone(self):
        return self.json_response.get('timezone', None)

    @property
    def start_time(self):
        if 'start_time' in self.json_response:
            return datetime.strptime(self.json_response['start_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
        return '<Marqeta.response_models.cron_job_info.CronJobInfo>'
