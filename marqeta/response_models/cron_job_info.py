from datetime import datetime, date
import json

class CronJobInfo(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'schedule' : self.schedule,
           'group' : self.group,
           'id' : self.id,
           'class' : self.class,
           'is_running' : self.is_running,
           'last_run_duration_millis' : self.last_run_duration_millis,
           'next_run' : self.next_run,
           'last_run' : self.last_run,
           'timezone' : self.timezone,
           'start_time' : self.start_time,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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
                return datetime.strptime(self.json_response['next_run'], '%Y-%m-%d').date()

    @property
    def last_run(self):
        if 'last_run' in self.json_response:
                return datetime.strptime(self.json_response['last_run'], '%Y-%m-%d').date()

    @property
    def timezone(self):
        if 'timezone' in self.json_response:
            return self.json_response['timezone']

    @property
    def start_time(self):
        if 'start_time' in self.json_response:
                return datetime.strptime(self.json_response['start_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
         return '<Marqeta.response_models.cron_job_info.CronJobInfo>'