from datetime import datetime

class CronJobInfo(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def schedule(self):
        if 'schedule' in self.json_response:
            return self.json_response['schedule']

    @property
    def group(self):
        if 'group' in self.json_response:
            return self.json_response['group']

    @property
    def id(self):
        if 'id' in self.json_response:
            return self.json_response['id']

    @property
    def class(self):
        if 'class' in self.json_response:
            return self.json_response['class']

    @property
    def is_running(self):
        if 'is_running' in self.json_response:
            return self.json_response['is_running']

    @property
    def last_run_duration_millis(self):
        if 'last_run_duration_millis' in self.json_response:
            return self.json_response['last_run_duration_millis']

    @property
    def next_run(self):
        if 'next_run' in self.json_response:
            return datetime.strptime(self.json_response['next_run'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_run(self):
        if 'last_run' in self.json_response:
            return datetime.strptime(self.json_response['last_run'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def timezone(self):
        if 'timezone' in self.json_response:
            return self.json_response['timezone']

    @property
    def start_time(self):
        if 'start_time' in self.json_response:
            return datetime.strptime(self.json_response['start_time'], '%Y-%m-%dT%H:%M:%SZ')

