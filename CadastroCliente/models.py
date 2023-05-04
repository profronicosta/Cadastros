from django.db import models

# Create your models here.
class Profissao(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Profissões"

class Interesse(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    ESTADO_CIVIL = [
        ('SOL','Solteiro'),
        ('CAS','Casado'),
        ('DIV','Divorciado'),
        ('VIU','Viúvo')
    ]
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=120, unique=True)
    endereco = models.CharField(max_length=250, null=True, verbose_name="Endereço")
    nro = models.IntegerField(null=True)
    bairro = models.CharField(max_length=50, null=True)
    cidade = models.CharField(max_length=50, null=True)
    cep = models.CharField(max_length=9, null=True)
    matricula = models.IntegerField(verbose_name="Matrícula")
    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(verbose_name="Usuário Ativo?")
    estado_civil = models.CharField(max_length=3, choices=ESTADO_CIVIL, null=True)
    profissao = models.ForeignKey(Profissao, 
                                  on_delete=models.SET_NULL, null=True, verbose_name="Profissão")
    interesses = models.ManyToManyField(Interesse)

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    ddd = models.CharField(max_length=2)
    numero = models.CharField(max_length=10)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.ddd}) {self.numero}"