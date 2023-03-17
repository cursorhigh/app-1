from django.db import models

class Person(models.Model):
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    onscore = models.IntegerField(default=0)
    ofscore = models.IntegerField(default=0)
    tscore = models.IntegerField(default=0)

    def save(self, update_rank=True, *args, **kwargs):
        super().save(*args, **kwargs)
        if update_rank and not getattr(self, '_updating_ranks', False):
            self._updating_ranks = True
            update_ranks()
            del self._updating_ranks

def update_ranks():
    # Get all persons ordered by total score
    persons = Person.objects.order_by('-tscore')

    # Update the rank of each person
    for rank, person in enumerate(persons, start=1):
        person.rank = rank
        person.save(update_fields=['rank'], update_rank=False)
