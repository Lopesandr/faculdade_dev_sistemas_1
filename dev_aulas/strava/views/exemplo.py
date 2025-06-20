from django.urls import reverse_lazy
from strava.forms.exemplo import ExemploForm
from strava.models.perfil import Pefil
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.serializers import serialize
from strava.models.perfil import Pefil
from django.views import View
from django.views.generic import DeleteView
from  django.contrib.auth.decorators import permission_required, login_required
from  django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

@login_required
@permission_required("strava.view_exemplo", raise_exception=True)


def create(request):
    if request.method == 'POST':
        form =  ExemploForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('strava:exemplo_fuction_list')
    else: 
        form = ExemploForm()
        context = {
            'form': form
        }

        return render(request, 'exemplo/create.html', context)



@login_required
@permission_required("strava.view_exemplo", raise_exception=True)
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

class ExemploDetailView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'strava.view_exemplo'
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


