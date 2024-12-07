from django.db import models

class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    preco = models.FloatField(null=False)
    quantidade = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.codigo}, {self.nome}, {self.preco}' \
                f'{self.quantidade}'

    def __repr__(self):
        return f'{self.codigo}, {self.nome}, {self.preco}' \
                f'{self.quantidade}'
    pass