from django import forms

class CadastroForm(forms.Form):
    codigo = forms.CharField(required=False, widget=forms.HiddenInput())
    nome = forms.CharField(label="Nome", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    preco = forms.FloatField(label="Preço", widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantidade = forms.IntegerField(label="Quantidade", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # 🚩 Lembre-se de mudar o NumberInput para TextInput caso haja algum erro
    pass