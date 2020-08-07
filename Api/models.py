from django.db import models


class User(models.Model):
    """
        Class representing articles
    """
    id = models.AutoField(primary_key=True)
    User = models.CharField(max_length=50)
    tz = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'


class ActivityPeriod(models.Model):
    """
    Models to check user activity
    """
    user_activity = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        db_table = 'activity_period'