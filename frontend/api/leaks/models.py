from django.db import models


class Email(models.Model):
    email = models.TextField(blank=False, unique=True)


class Domain(models.Model):
    domain = models.TextField(blank=False, unique=True)


class EmailDataLeak(models.Model):
    data_leak = models.ForeignKey("DataLeak", null=True, on_delete=models.SET_NULL)
    email = models.ForeignKey("Email", null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ("data_leak", "email")


class DomainDataLeak(models.Model):
    data_leak = models.ForeignKey("DataLeak", null=True, on_delete=models.SET_NULL)
    domain = models.ForeignKey("Domain", null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ("data_leak", "domain")


class DataLeak(models.Model):
    name = models.TextField(blank=False, unique=True)
