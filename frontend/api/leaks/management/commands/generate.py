from django.core.management.base import BaseCommand
from ...models import Domain, DomainDataLeak, Email, EmailDataLeak, DataLeak
from .random_words import random_word


class Command(BaseCommand):
    help = 'Generating domains and emails'

    def handle(self, *args, **options):
        dataleaks = ["dataleak1", "dataleak_abc", "dataleak_123", "dataleak_gg12"]
        domains = ["example.com", "abc.com", "abc123.com", "abc.pt"]

        EmailDataLeak.objects.all().delete()
        DomainDataLeak.objects.all().delete()
        Email.objects.all().delete()
        Domain.objects.all().delete()
        DataLeak.objects.all().delete()

        for dataleak in dataleaks:
            print("DataLeak: %s" % dataleak)

            dataleak_row = DataLeak.objects.create(name=dataleak)

            for domain in domains:
                print("Domain: %s" % domain)

                for i in range(0, 100):

                    if Domain.objects.filter(domain=domain).count() == 0:
                        domain_row = Domain.objects.create(domain=domain)

                        if DomainDataLeak.objects.filter(domain=domain_row, data_leak=dataleak_row).count() == 0:
                            DomainDataLeak.objects.create(domain=domain_row, data_leak=dataleak_row)

                    else:
                        domain_row = Domain.objects.get(domain=domain)

                        if DomainDataLeak.objects.filter(domain=domain_row, data_leak=dataleak_row).count() == 0:
                            DomainDataLeak.objects.create(domain=domain_row, data_leak=dataleak_row)

                    email = random_word() + "@" + domain

                    if Email.objects.filter(email=email).count() == 0:
                        email_row = Email.objects.create(email=email)

                        if EmailDataLeak.objects.filter(email=email_row, data_leak=dataleak_row).count() == 0:
                            EmailDataLeak.objects.create(email=email_row, data_leak=dataleak_row)
                    else:
                        email_row = Email.objects.get(email=email)

                        if EmailDataLeak.objects.filter(email=email_row, data_leak=dataleak_row).count() == 0:
                            EmailDataLeak.objects.create(email=email_row, data_leak=dataleak_row)

                print("")

        print("Emails to use further:")

        print("")

        first_pk = Email.objects.first().pk

        for i in range(0, 10):
            print(Email.objects.get(pk=first_pk+i*50).email)
