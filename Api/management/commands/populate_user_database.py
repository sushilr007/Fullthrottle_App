from django.core.management.base import BaseCommand
from fullt_api.models import User, ActivityPeriod


class Command(BaseCommand):
    help = 'Run the loom buffer processor'

    def handle(self, *args, **kwargs):

        user_obj = User(User="Sushil", tz="Pune")
        user_obj.save()
        activityt_obj = ActivityPeriod(User, start_time="2020-1-25 12:10", end_time="2020-1-25 12:10")
        activityt_obj.save()