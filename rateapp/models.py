from django.db import models
import datetime

# Create your models here.
class Rate(models.Model):
    ident = models.CharField(max_length=3)
    rate = models.IntegerField()
    time_point = models.DateTimeField(db_index=True)

    # def comparing(request):
    #     rates_a = Rate.objects.filter(ident=request[0])
    #     rate_a = [element for element in rates_a if element.time_point - request[2] >= datetime.timedelta(0)]
    #     a = max(rate_a, key=lambda i : i.time_point).rate
    #     rates_b = Rate.objects.filter(ident=request[1])
    #     rate_b = [element for element in rates_b if element.time_point - request[2] >= datetime.timedelta(0)]
    #     b = max(rate_b, key=lambda i : i.time_point).rate
    #     return a/b