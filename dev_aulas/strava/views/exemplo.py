from django.urls import reverse_lazy
from strava.models.perfil import Pefil
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.serializers import serialize
from strava.models.perfil import Pefil
from django.views import View
from django.views.generic import DeleteView





def exemplo_list(request):
    exemplos = Pefil.objects.all()
    context = {'exemplos': exemplos,}
    return render(request,  'exemplo/list.html', context)

def exemplo_detail(request, pk):
    exemplo = Pefil.objects.get(id=pk)
    context = {'exemplo':exemplo,}
    return render(request, 'exemplo/read.html', context)

def delete(request, exemplo_id):
    exemplo = get_object_or_404(Pefil, pk=exemplo_id)
    print
    try: 
        if request.method == 'POST':
            v_pk_id = request.POST.get("exemplo_id", None)
            print(v_pk_id)
            if int(v_pk_id) == exemplo_id:
                exemplo.delete()
                return redirect('strava:exemplo_fuction_list')
        else:
            context = {'exemplo': exemplo}
            return render(request, 'exemplo/delete.html', context)
    except Exception as e:
        print(e)
        context = {}
        return render(request, 'exemplo/read.html', context)

class ExemploDetailView(View):
    @staticmethod
    def get(request, pk): 
        exemplo = Pefil.objects.get(id=pk)
        context = {'exemplo':exemplo,}
        return render(request, 'exemplo/read.html', context)


class ExemoloDeleteView(DeleteView):
    model = Pefil
    fields = '__all__'
    template_name = "exemplo/delete.html"
    sucess_url = reverse_lazy('strava:exemplo_fuction_list')