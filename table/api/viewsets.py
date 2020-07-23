from rest_framework.viewsets import ModelViewSet
from .serializers import ElementSerializer
from table.models import Element

class ElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    http_method_names = ['get','head','list']

    def get_queryset(self):

        element = self.request.query_params.get('element',None)
        symbol = self.request.query_params.get('symbol',None)
        atomicNumber = self.request.query_params.get('atomicNumber',None)
        atomicMass = self.request.query_params.get('atomicMass',None)
        neutrons = self.request.query_params.get('neutrons',None)
        protons = self.request.query_params.get('protons',None)
        electrons = self.request.query_params.get('electrons',None)
        phase = self.request.query_params.get('phase',None)
        radioactive = self.request.query_params.get('radioactive',None)
        tp = self.request.query_params.get('tp',None)
        queryset = Element.objects.all()

        if element:
           queryset = queryset.filter(element=element)

        if symbol:
           queryset = queryset.filter(symbol=symbol)

        if atomicMass:
            queryset = queryset.filter(atomicMass=atomicMass)

        if atomicNumber:
            queryset = queryset.filter(atomicNumber=atomicNumber)

        if neutrons:
            queryset = queryset.filter(neutrons=neutrons)

        if protons:
            queryset = queryset.filter(protons=protons)

        if electrons:
            queryset = queryset.filter(electrons=electrons)

        if phase:
            queryset = queryset.filter(phase=phase)

        if radioactive:
            queryset = queryset.filter(radioactive=radioactive)

        if tp:
            queryset = queryset.filter(tp=tp)

        return queryset



