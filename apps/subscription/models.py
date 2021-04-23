from django.db import models
from apps.user.models import User

# Create your models here.


# Subject Data Model
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# SubjectUsers is a bridge between subject and user
class SubjectUsers(models.Model):
    project = models.ForeignKey(
        Subject,
        db_index=True,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    user = models.ForeignKey(
        User,
        db_index=True,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def __str__(self):
        return ''

    # fixes a pluralization issue and forces project and user to be unique together
    class Meta:
        unique_together = (
            ('project', 'user'),
        )
        verbose_name_plural = 'Project Users'


class Subscription(models.Model):

    # Constants for sub status
    SUBSCRIBED = 'subscribe'
    UNSUBSCRIBED = 'unsubscribed'

    # Creates a list of lists for subscription
    SUBSCRIPTION_STATUS = (
        (SUBSCRIBED, 'Subscribe'),
        (UNSUBSCRIBED, 'Unsubscribed')
    )

    # Subject the subscription is attached to
    subject = models.ForeignKey(
        Subject,
        db_index=True,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    # The user that is subscribed
    subbed_user = models.ForeignKey(
        User,
        db_index=True,
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )



