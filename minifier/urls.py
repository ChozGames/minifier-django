from django.urls import path
from . import views

urlpatterns = [
    path('convert', views.convert, name="convert"),
    path('redirectcode', views.redirectcode, name="redirectcode"), 
    # path('articles/<str:tag>', views.list_articles_by_tag), 
    # path('articles/<int:year>/<int:month>', views.list_articles), 
    # path('google', views.google), 
    # path('date', views.date_actuelle),
    # path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    # path('article/<int:id>', views.lire, name='lire'),
    # path('article/<slug:slug>', views.lire, name='lire'),
    # path('contact/', views.contact, name='contact'),
    # path('new/contact/', views.nouveau_contact, name="newcontact"),
    # path('voir/contact/', views.voir_contacts, name="voircontact"),
]


