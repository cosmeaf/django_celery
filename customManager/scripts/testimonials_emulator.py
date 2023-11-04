import os
import django
import sys

# Adicione o caminho pai do seu projeto ao sys.path
sys.path.append('/home/superuser/projects/django_celery')

# Defina a variável de ambiente para as configurações do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Inicialize o Django
django.setup()

# O resto do seu código segue aqui...
from customManager.models.testimonial_model import Testimonial
from security.models import CustomUser
import random
import lorem
import faker

# Inicialize o gerador de dados fictícios
fake = faker.Faker()

def create_fake_testimonials(num_testimonials):
    for _ in range(num_testimonials):
        # Crie um usuário fictício
        user = CustomUser.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            password=fake.password(),
        )
        
        # Crie um testemunho fictício
        Testimonial.objects.create(
            user=user,
            rating=random.randint(1, 5),
            content=lorem.paragraph(),
            author_name=fake.name(),
            author_title=fake.job(),
            image='testimonials/testimonial-{}.png'.format(random.randint(1, 5))
        )

if __name__ == "__main__":
    num_testimonials_to_create = 10  # Defina o número de testemunhos fictícios que deseja criar
    create_fake_testimonials(num_testimonials_to_create)
