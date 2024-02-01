from django.urls import path
from . import views

urlpatterns = [
    path("basic",views.hello_world_basic,name="basic_hello_world"),
    path("static",views.static_hello_world,name="static"),
    path('paramater',views.hello_world_paramaters,name="hw_paramaters"),
    
    #example of a url paramater, note the type which can be changed
    path('named/<str:names>',views.hello_world_url_paramaters,name="hw_url_params")
]
