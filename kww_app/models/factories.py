import factory

from kww_app.models import Company, CompanyType, Participant


class CompanyTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CompanyType

    name = factory.Faker('random_elements', elements=['IT', 'Institute', 'University'])


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker('company')
    companytype = factory.SubFactory(CompanyTypeFactory)


class ParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Participant



