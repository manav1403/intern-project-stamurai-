from django.db import models
from django.db.models.signals import pre_save, post_delete

class task(models.Model):
    title = models.CharField(max_length=40)
    P_choices =(
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low')
    )
    date=models.DateField()
    priority = models.CharField(max_length=20,choices=P_choices)
    discription = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    


class updates(models.Model):
    task= models.CharField(max_length=40)
    u_choices=(
        ('Add','Add'),
        ('Remove','Remove'),
        ('Update','Update')
    )
    type=models.CharField(max_length=10,choices=u_choices)


    def __str__(self):
        return (self.type+' => '+self.task)


def task_pre_save_receiver(sender, instance, *args, **kwargs):
    type="Add"
    if task.objects.filter(id=instance.id).exists():
        type="Update"
    obj=updates(task=instance.title,type=type)
    obj.save()

def task_post_delete_receiver(sender, instance, *args, **kwargs):
    type="Remove"
    obj=updates(task=instance.title,type=type)
    obj.save()


pre_save.connect(task_pre_save_receiver, sender=task)
post_delete.connect(task_post_delete_receiver, sender=task)