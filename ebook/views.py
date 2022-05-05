from django.http import request
from django.shortcuts import render, redirect,get_object_or_404
from .models import Livros, Carrinho, Vote
from django.contrib.auth.decorators import login_required

def index(request):
    livros = Livros.objects.all()
    melhores_livros = Livros.objects.all().order_by("-porcentagem")[0:6]
    return render(request, 'paginas/tela.html', {'livros': livros, 'melhores_livros':melhores_livros})

@login_required(redirect_field_name='login')
def produto(request, id):

    livro = get_object_or_404(Livros, id=id)
    if request.method == 'POST' and "btn-form1" in request.POST:
        fb = request.POST.get('fb')
        avaliacao = Vote.objects.all().filter(user = request.user, livro = livro )
        if len(avaliacao) == 0:
            livro.quantidade_avaliacoes += 1
            livro.nota += int(fb)
            livro.quantidade_estrelas = livro.nota / livro.quantidade_avaliacoes
            livro.porcentagem = (livro.quantidade_estrelas * 100) / 5 
            livro.porcentagem = round(livro.porcentagem)
            livro.save()

            avaliacao = Vote.objects.create(user = request.user, livro = livro)
            avaliacao.save()

            return render(request, 'paginas/produto.html', {'livro':livro})
        else:
            return render(request, 'paginas/produto.html', {'livro':livro})
    
    elif request.method == 'POST' and "btn-form2" in request.POST:
        quant = request.POST.get('quantidade')
        livro = Carrinho.objects.all().filter(user=request.user, livro__id=id)
        if len(livro) == 0:
            total = 0
            total += int(quant)
            book=Livros.objects.get(id=id)
            livro = Carrinho.objects.create(user=request.user, livro=book, quantidade = quant, total=total)
            livro.save()
        else:
            livro[0].quantidade += int(quant)
            livro[0].save()
        return redirect('carrinho')
    else:
        return render (request, 'paginas/produto.html',{'livro':livro})


@login_required(redirect_field_name='login')    
def carrinho(request):
    carrinho = Carrinho.objects.all().filter(user=request.user)
    kart=[]
    for product in carrinho:
        dic={'usuario':product.user,'livro':product.livro,'quantidade':product.quantidade,'total':product.quantidade*product.livro.valor}
        kart.append(dic)
       
    return render(request, 'paginas/carrinho.html',{'kart':kart})

def deletar(request,id):
    remove = Carrinho.objects.all().filter(user=request.user,livro__id=id)
    remove.delete()
    return redirect('carrinho')
