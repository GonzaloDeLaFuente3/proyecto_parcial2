from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from apps.vianda.models import Vianda


class ViandaForm(forms.ModelForm):
    cantidad_vianda = forms.IntegerField(min_value=1)


    # estado = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = Vianda

        fields = '__all__'

        widgets = {
            'fecha_inicio': DateInput(format='%Y-%m-%d', attrs={'type':'date'}),



        }

    # from datetime import datetime
    #
    # print(datetime.today().strftime('%Y-%m-%d'))
    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data['fecha_inicio'].strftime('%Y-%m-%d')
        fecha_hoy= datetime.today().strftime('%Y-%m-%d')
        print(fecha_inicio)
        print(fecha_hoy)


        if fecha_inicio <= fecha_hoy:

            raise ValidationError('la fecha de la vianda tiene que mayor a la fecha actual')
        return fecha_inicio