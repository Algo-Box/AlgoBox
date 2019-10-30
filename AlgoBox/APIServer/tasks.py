from django_cron import CronJobBase, Schedule
from APIServer.CListAPI import saveModel

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'APIServer.my_cron_job'

    def do(self):
    	saveModel()