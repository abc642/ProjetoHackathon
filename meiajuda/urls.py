from django.urls import path
from .views import signup_view,activate,activation_sent_view
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from .views import sou_mei



urlpatterns = [
    path('soumei/',sou_mei,name='soumei'),
    path('singup/',signup_view,name='singup'),
    path('sent/',activation_sent_view,name='activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/',activate,name='activate'),
    path('list/',persons_list,name='person_list'),
    path('new/',persons_new,name='person_new'),
    path('update/<int:id>/',persons_update,name='person_update'),
    path('delete/<int:id>/',persons_delete,name='person_delete'),

]