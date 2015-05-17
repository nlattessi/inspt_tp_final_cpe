from django_faker import Faker
# this Populator is only a function thats return a django_faker.populator.Populator instance
# correctly initialized with a faker.generator.Generator instance, configured as above
populator = Faker.getPopulator()

from app.models import Estado, Vendedor
populator.addEntity(Estado,5)
populator.addEntity(Vendedor,10)

insertedPks = populator.execute()