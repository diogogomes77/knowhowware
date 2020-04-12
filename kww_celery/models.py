from celery import shared_task
from django.db import models
import datetime
from datetime import date
import time
from django.db.models.signals import post_save
from django.dispatch import receiver


class PersonAge(models.Model):
    name = models.CharField(max_length=32)
    born = models.DateField()
    age = models.IntegerField(null=True, blank=True)

    def ____init__(self, name, born):
        try:
            # 1997/2/3
            datetime.datetime.strptime(born, '%Y/%m/%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY/MM/DD")
        self.name = name
        self.born = born


@shared_task
def calculate_age(id):
    print('started calculating age')
    person = PersonAge.objects.get(pk=id)
    print('personn= ' + str(person))
    today = date.today()
    birth_date = person.born
    age = today.year - birth_date.year - ((today.month, today.day) <(birth_date.month, birth_date.day))
    person.age = age
    time.sleep(30)
    person.save()
    print('finished calculating age')
    #return age


@receiver(post_save, sender=PersonAge)
def calculate_age_task(sender, instance, created, raw, using, update_fields, **kwargs):
    if created:
        print('post_save= calculate_age_task')
        person = instance
        print('person id= ' + str(person.id))
        calculate_age.delay(person.id)
