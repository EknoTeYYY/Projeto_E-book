from django.db import models
from django.contrib.auth.models import User

class Livros(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.IntegerField()
    descicao = models.TextField(blank=True)
    imagem = models.ImageField()
    nota = models.IntegerField(default=0)
    quantidade_avaliacoes = models.IntegerField(default=0)
    quantidade_estrelas = models.FloatField(default=0)
    porcentagem = models.FloatField(default=0)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = ('Livros')

class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livros,on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = ('Carrinho')
    
class Vote(models.Model):
    livro =models.ForeignKey(Livros, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)