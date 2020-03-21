import random
from io import BytesIO
from unittest import mock

from PIL import Image, ImageDraw, ImageFont
from django.core.files import File
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import BaseCommand
from faker import Faker
from django.conf import settings
from kww_app.models import CompanyType, Company, Technology, Role, Participant, Project, ProjectType, \
    ProjectParticipation, User


def text_on_img(text="Hello", size=12, upload_to=None):
    image_name = text + '.jpg'
    filename = settings.MEDIA_ROOT + '/' + settings.PROJECT_IMAGES + image_name
    print('filename= ' + filename)
    "Draw a text on an Image, saves it, show it"
    fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', size)
    # create image
    image = Image.new(
        mode="RGB",
        size=(int(size/2)*len(text), size+50), color="red")
    draw = ImageDraw.Draw(image)
    # draw text
    draw.text((10, 10), text, font=fnt, fill=(255, 255, 0))
    # save file
    #image_file = BytesIO()
    #image.save(image_file, 'PNG')  # or whatever format you prefer
    image.save(filename)
    return image_name


class Command(BaseCommand):
    help = 'add mock data during development process'

    def handle(self, *args, **options):
        self.fake = Faker()

        self.createsuperuser()

        self.create_companies()
        self.create_technologies()
        self.generate_participants()
        self.generate_projects()
        self.generate_participations()
        self.generate_issues()

    def createsuperuser(self):
        admin = User.objects.create_user(
            username='admin',
            password='admin',
            is_superuser=True,
            is_staff=True
        )

    def generate_issues(self):
        print('--- generate_issues ---')
        fake = self.fake
        participations = ProjectParticipation.objects.all()
        for par in participations:
            for i in range(random.randrange(1,5)):
                par.issues.create(
                    participation=par,
                    issue=fake.text(max_nb_chars=1024, ext_word_list=None),
                )

    def generate_participations(self):
        print('--- generate_participations ---')
        companies0 = list(Company.objects.filter(parent__isnull=True))
        companies1 = list(Company.objects.filter(parent__isnull=False))
        participants = list(Participant.objects.all())

        technologies = list(Technology.objects.all())

        def add_technology(participation):
            print('--- add_technology ---')
            tech = None
            par_techs = list(participation.technologies.all())
            while not tech and tech not in par_techs:
                tech = random.choice(technologies)
            participation.add_technology(tech)

        roles = list(Role.objects.all())

        def add_participation(prjs):
            print('--- add_participation ---')
            for prj in prjs:
                prj_participants = list(prj.participants.all())
                participant = None
                while not participant or participant in prj_participants:
                    participant = random.choice(participants)
                prj_companies = list(prj.companies.all())
                company = None
                while not company or company in prj_companies:
                    company = random.choice(companies0)
                company = random.choice(companies0)
                role = random.choice(roles)
                par_created = prj.add_participant(participant, role, company)
                if par_created:
                    for i in range(random.randrange(1,5)):
                        add_technology(par_created)

                comp_created = prj.add_company(company)

        prjs0 = list(Project.objects.filter(parent__isnull=True))
        add_participation(prjs0)
        prjs1 = list(Project.objects.filter(parent__isnull=False))
        add_participation(prjs1)

    def generate_projects(self):
        print('--- generate_projects ---')
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

        def create_project(parent=None, i=None):
            print('--- create_project ---')
            #content_path = settings.MEDIA_URL + settings.PROJECT_IMAGES

            name = text_on_img(text=str(i) + "***", size=100)
            content_path = settings.MEDIA_ROOT + '/' + settings.PROJECT_IMAGES + name
            uploaded_image = SimpleUploadedFile(
                    name=name,
                    content=open(content_path, 'rb').read(),
                    content_type='image/jpeg'
            )

            #file_mock = mock.MagicMock(spec=File, name='FileMock_' + str(i))
            name = fake.text(max_nb_chars=16, ext_word_list=None)
            #image_file = text_on_img(text=name)
            #image = Image.new('RGBA', size=(50, 50), color=(256, 0, 0))
            #image_file = BytesIO()
            #image.save(image_file, 'PNG')  # or whatever format you prefer
            #file = ImageFile(text_on_img(text="image_"+str(i), size=100))
            return Project.objects.create(
                name=name,
                projecttype=random.choice(prj_types),
                parent=parent,
                #image=text_on_img(text="image_"+str(i), size=100)
                image=uploaded_image
            )

        for i in range(0, 4):
            prj = create_project(i=i)
            prj0.append(prj)

        for i in range(5, 15):
            create_project(
                parent=random.choice(prj0),
                i=i
            )

    def generate_participants(self):
        print('--- generate_participants ---')
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
        print('--- create_technologies ---')
        fake = self.fake
        if Technology.objects.all().count() > 0:
            return

        def generate_tech(parents=None):
            print('--- generate_tech ---')
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

        tecs0 = generate_tech()
        tecs1 = generate_tech(tecs0)
        tecs2 = generate_tech(tecs1)

    def create_companies(self):
        print('--- create_companies ---')
        fake = self.fake
        if Company.objects.all().count() > 0:
            return
        companytypes = ['IT', 'Institute', 'University']
        for ct in companytypes:
            CompanyType.objects.create(name=ct)

        cts = list(CompanyType.objects.all())
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
