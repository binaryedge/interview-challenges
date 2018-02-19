from django.core.management.base import BaseCommand
from ...models import Domain, DomainDataLeak, Email, EmailDataLeak, DataLeak
from .random_words import random_word
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Generating domains and emails'

    def handle(self, *args, **options):
        dataleaks = ["dataleak1", "dataleak_abc", "dataleak_123", "dataleak_gg12"]
        domains = ["example.com", "abc.com", "abc123.com", "abc.pt"]

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
                        email_row = Email.objects.create(email=email, domain=domain_row)

                        if EmailDataLeak.objects.filter(email=email_row, data_leak=dataleak_row).count() == 0:
                            EmailDataLeak.objects.create(email=email_row, data_leak=dataleak_row)
                    else:
                        email_row = Email.objects.get(email=email)

                        if EmailDataLeak.objects.filter(email=email_row, data_leak=dataleak_row).count() == 0:
                            EmailDataLeak.objects.create(email=email_row, data_leak=dataleak_row)

                print("")

        domain = "example.com"
        emails = ["example1@example.com", "example2@example.com", "example3@example.com", "example4@example.com",
                  "example5@example.com"]

        for dataleak in dataleaks:
            dataleak_row = DataLeak.objects.get(name=dataleak)

            if Domain.objects.filter(domain=domain).count() == 0:
                domain_row = Domain.objects.create(domain=domain)

                if DomainDataLeak.objects.filter(domain=domain_row, data_leak=dataleak_row).count() == 0:
                    DomainDataLeak.objects.create(domain=domain_row, data_leak=dataleak_row)

            else:
                domain_row = Domain.objects.get(domain=domain)

                if DomainDataLeak.objects.filter(domain=domain_row, data_leak=dataleak_row).count() == 0:
                    DomainDataLeak.objects.create(domain=domain_row, data_leak=dataleak_row)

            for email in emails:
                if Email.objects.filter(email=email).count() == 0:
                    email_row = Email.objects.create(email=email, domain=domain_row)

                    if EmailDataLeak.objects.filter(email=email_row, data_leak=dataleak_row).count() == 0:
                        EmailDataLeak.objects.create(email=email_row, data_leak=dataleak_row)
                else:
                    email_row = Email.objects.get(email=email)

                    if EmailDataLeak.objects.filter(email=email_row, data_leak=dataleak_row).count() == 0:
                        EmailDataLeak.objects.create(email=email_row, data_leak=dataleak_row)

        print("Emails to use further:")

        print("")

        first_pk = Email.objects.first().pk

        for i in range(0, 10):
            print(Email.objects.get(pk=first_pk+i*50).email)

        if User.objects.filter(username="teste").count() == 0:
            User.objects.create_user(username="teste", email="email@email.com", password="reverse")
