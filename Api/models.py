from django.db import models

# Create your models here.
class User(models.Model):
    """
        Class representing articles
    """
    unique_id = models.CharField(max_length=20,primary_key=True)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'


class ActivityPeriod(models.Model):
    """
    Models to check user activity
    """
    user_activity = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    start_time = models.DateTimeField('%m/%d/%Y %H:%M')
    end_time = models.DateTimeField('%m/%d/%Y %H:%M')

    class Meta:
        db_table = 'activity_period'