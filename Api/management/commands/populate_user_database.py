from django.core.management.base import BaseCommand
from Api.models import User, ActivityPeriod


class Command(BaseCommand):
    help = 'Run the loom buffer processor'
#kwargs
    def handle(self, *args, **options):

        user_obj = User.objects.create(unique_id="W012A3CDE",real_name="Sushil Raverkar", tz="Pune")
        user_obj = User.objects.create(unique_id="W012A3CDE",real_name="Sushil Raverkar", tz="Pune")
        user_obj.save()
        activityt_obj = ActivityPeriod.objects.create(user_activity=user_obj, start_time="2020-1-25 12:10", end_time="2020-1-25 12:10")
        activityt_obj = ActivityPeriod.objects.create(user_activity=user_obj, start_time="2020-1-25 12:10", end_time="2020-1-25 12:10")
        activityt_obj.save()