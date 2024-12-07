from django.shortcuts import render, loader
from django.http import HttpResponse
from .forms import CadastroForm
from .models import Produto
import json

HOME_PAGE = 'pages/home.html'
CADASTRO_PAGE = 'pages/cadastro.html'
LISTA_PAGE = 'pages/lista.html'
BUSCA_PAGE = 'pages/busca.html'

def home(request):
    template = loader.get_template(HOME_PAGE)
    return HttpResponse(template.render())
    pass

def cadastro(request):
    form = CadastroForm()
    return render(request, CADASTRO_PAGE, {'form': form})
    pass

def lista(request):
    produtos = Produto.objects.all()
    return render(request, LISTA_PAGE, {
        'produtos': produtos
    })
    pass

def busca(request):
    return render(request, BUSCA_PAGE)
    pass

def cadastrar(request):
    try:
        if request.method == "POST":
            form = CadastroForm(request.POST)
            if form.is_valid():
                produto = Produto()
                produto.nome = form.cleaned_data['nome']
                produto.preco = form.cleaned_data['preco']
                produto.quantidade = form.cleaned_data['quantidade']
                if len(form.cleaned_data['codigo']) > 0:
                    produto.codigo = int(form.cleaned_data['codigo'])
                    msg = 'Produto atualizado com sucesso!'
                else:
                    msg = 'Produto cadastrado com sucesso!'
                produto.save()
            else:
                msg = form.errors
            return render(request, CADASTRO_PAGE, {
                'form': CadastroForm(),
                'msg': msg
            })
        else:
            raise Exception('MethodEnvioError, Use post para formulários')
    except Exception as e:
        msg = e.args
        return render(request, CADASTRO_PAGE, {
            'form': CadastroForm(),
            'msg': msg
        })
    pass

def excluir(request, codigo):
    try:
        produto = Produto.objects.get(pk=codigo)
        result = produto.delete()
        if result[0] > 0:
            msg = "Produto deletado com sucesso!"
        else:
            msg = "Nenhum produto foi encontrado."

        return render(request, LISTA_PAGE, {
            'produtos': Produto.objects.all(),
            'msg': msg
        })
    except Exception as e:
        msg = e.args
        return render(request, LISTA_PAGE, {
            'produtos': Produto.objects.all(),
            'msg': msg
        })
    pass

def alterar(request, codigo):
    try:
        produto = Produto.objects.get(pk=codigo)
        form = CadastroForm(initial={
            'codigo': produto.codigo,
            'nome': produto.nome,
            'preco': produto.preco,
            'quantidade': produto.quantidade
        })
        return render(request, CADASTRO_PAGE, {
            'form': form
        })
    except Exception as e:
        msg = e.args
        return render(request, LISTA_PAGE, {'produtos': Produto.objects.all(), 'msg': msg})
    pass

def pesquisar(request):
    try:
        if request.method == "POST":
            nome = request.POST['nome']
            # efetuar a busca
            # LIKE %nome%
            produtos = Produto.objects.filter(nome__icontains=nome)
            response = {}
            for indice, produto in enumerate(produtos):
                p = {}
                p['codigo'] = produto.codigo
                p['nome'] = produto.nome
                p['preco'] = produto.preco
                p['quantidade'] = produto.quantidade
                response[indice] = p
                response['t'] = len(produtos)
                return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            raise Exception("MethodEnvioError, use POST para formulários.")
    except Exception as ex:
        msg = ex.args
        return HttpResponse(json.dumps({'msg': msg}), content_type="application/json")
    pass