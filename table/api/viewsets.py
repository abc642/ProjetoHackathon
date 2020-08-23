from rest_framework.viewsets import ModelViewSet
from .serializers import ElementSerializer,ComercioSerializer,PersonSerializer
from table.models import Element,Comercio
from meiajuda.models import Person


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get','head','list']
    filter_fields = ('titulo','categoria','descricao','numero','cidade')

class ElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    http_method_names = ['get','head','list']
    filter_fields = ('element','symbol','atomicNumber','atomicMass','neutrons',
                       'protons','electrons','phase','radioactive','tp')

class ComercioViewSet(ModelViewSet):
    queryset = Comercio.objects.all()
    serializer_class = ComercioSerializer
    http_method_names = ['get','head','list']
    filter_fields = ('titulo','descricao','cidade','numero','tipo','imagem')



