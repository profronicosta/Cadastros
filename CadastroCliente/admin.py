from django.contrib import admin
from CadastroCliente.models import Cliente, Profissao, Telefone, Interesse

# Register your models here.
#Classe para exibir Telefones no cad. de cliente
class Telefones(admin.StackedInline):
    model = Telefone
    # extra = 0
    
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cidade', 'profissao']
    list_display_links = ['id', 'nome']
    list_filter = ['bairro', 'cidade', 'ativo']
    search_fields = ['nome']
    inlines = [Telefones]
    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Profissao)
admin.site.register(Telefone)
admin.site.register(Interesse)