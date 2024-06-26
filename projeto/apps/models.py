from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

# quem tiver com essa ponta de cadastro das cafeterias pode elaborar o model abaixo, só tô colocando um pontapé pra conseguir fazer o model "Favorito"
class Cafe(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    email = models.EmailField(default="default@example.com")
    whatsapp = models.CharField(max_length=15, default='5500000000000')  # Inclua código do país e DDD

    def __str__(self):
        return self.nome #teste

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=15, default='5500000000000')  # Inclua código do país e DDD

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} - {self.cafe.nome}'
    
class Cadastrar_Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)  # Garante que cada cadastro tenha um User associado
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, validators=[RegexValidator(r'^\d{11}$', 'CPF deve ter 11 dígitos, somente números')])
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} ({self.user.username if self.user else 'Sem usuário'})"

    class Meta:
        app_label = 'apontacafe'
        verbose_name = "Cadastro"
        verbose_name_plural = "Cadastros" #teste
    