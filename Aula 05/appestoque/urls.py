from django.urls import path
from .import views

app_name='appestoque'

urlpatterns = [
    path('', views.home, name="home"),
    path('Cadastro/', views.cadastro, name="cadastro"),
    path('Lista/', views.lista, name="lista"),
    path('Busca/', views.busca, name="busca"),
    path('Cadastrar/', views.cadastrar, name="cadastrar"),
    path('Excluir/<int:codigo>', views.excluir, name="excluir"),
    path('Alterar/<int:codigo>', views.alterar, name="alterar"),
    path('Busca/enviar_post/', views.pesquisar, name="pesquisar")
]