from django.db import models
from django.contrib.auth.models import User


class Department(models.TextChoices):
    PROD = 'P', 'Produção'
    HUMANOS = 'RH', 'Recursos Humanos'
    QUALIDADE = 'Q', 'Qualidade'
    LOGISTICA = 'L', 'Logistica'
    MANUTENCAO = 'M', 'Manutenção'


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    department = models.CharField(
        max_length=3,
        choices=Department.choices,
        default=Department.PROD
    )
    image = models.ImageField(upload_to='func' ,default='random.jpg')
    contact = models.CharField(max_length=150, blank=True, null=True)
    nationality = models.CharField(max_length=150, default='portuguesa')
    address = models.CharField(max_length=150, blank=True, null=True)
    

    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.department}'

class Client(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='clients/', default='random.jpg')

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='users/', null=True, default='transferir.jpg')


    def __str__(self):
        return self.user.username

