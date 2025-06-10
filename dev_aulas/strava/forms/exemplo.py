from strava.forms.base_form import BaseForm
from strava.models.perfil import Pefil


class ExemploForm(BaseForm):
    class Meta:
        model = Pefil
        fields = "__all__"