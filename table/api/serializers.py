from rest_framework.serializers import ModelSerializer
from table.models import Element,Comercio
from meiajuda.models import Person

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('titulo','categoria','descricao','imagem','numero','cep','cidade')

class ElementSerializer(ModelSerializer):
    class Meta:
        model = Element
        fields = ('element','symbol','atomicNumber',
                  'atomicMass','neutrons','protons',
                  'electrons','phase','radioactive','tp')

class ComercioSerializer(ModelSerializer):
    class Meta:
        model = Comercio
        fields = ('titulo','descricao','cidade','numero','imagem','tipo')



