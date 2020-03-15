import random

from django.core.management import BaseCommand
from faker import Faker

from kww_app.models import CompanyType, Company, Technology, Role, Participant, Project, ProjectType


class Command(BaseCommand):
    help = 'add mock data during development process'

    def handle(self, *args, **options):
        self.fake = Faker()
        self.create_companies()
        self.create_technologies()
        self.generate_participants()

    def generate_projects(self):
        if Project.objects.all().count() > 0:
            return
        fake = self.fake
        project_type_names = ['Telco', 'R&I', 'Web', 'Desktop']
        prj_types = []
        for name in project_type_names:
            prj_type = ProjectType.objects.create(
                name=name
            )
            prj_types.append(prj_type)

        prj0 = []
        companies = list(Company.objects.all())
        for i in range(10):
            prj = Project.objects.create(
                name=fake.text(max_nb_chars=16, ext_word_list=None),
            )

    def generate_participants(self):
        fake = self.fake

        if Participant.objects.all().count() > 0:
            return
        role_names = ['dev', 'tester', 'manager',]
        roles = []
        for name in role_names:
            role = Role.objects.create(
                name=name
            )
            roles.append(role)

        for i in range(5):
            profile = fake.profile()
            Participant.objects.create(
                username=profile['username'],
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=profile['mail']
            )

    def create_technologies(self):
        fake = self.fake
        if Technology.objects.all().count() > 0:
            return

        def generate(parents=None):
            tecs = []
            for i in range(5):
                parent = None
                if parents:
                    parent = random.choice(parents)
                tec = Technology.objects.create(
                    name=fake.text(max_nb_chars=16, ext_word_list=None),
                    parent=parent
                )
                tecs.append(tec)
                return tecs

        tecs0 = generate()
        tecs1 = generate(tecs0)
        tecs2 = generate(tecs1)

    def create_companies(self):
        fake = self.fake
        if Company.objects.all().count() > 0:
            return
        companytypes = ['IT', 'Institute', 'University']
        for ct in companytypes:
            CompanyType.objects.create(name=ct)

        cts = list(CompanyType.objects.all())
        # first level companies
        for i in range(5):
            Company.objects.create(
                name=fake.company(),
                companytype=random.choice(cts)
            )
        companies0 = list(Company.objects.all())
        for i in range(10):
            Company.objects.create(
                name=fake.company(),
                companytype=random.choice(cts),
                parent=random.choice(companies0)
            )

        companies1 = list(Company.objects.filter(parent__isnull=False))
        for i in range(5):
            Company.objects.create(
                name=fake.company(),
                companytype=random.choice(cts),
                parent=random.choice(companies1)
            )
