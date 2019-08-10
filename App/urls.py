from django.conf.urls import url

from App import views

urlpatterns =[

    url(r"^index/$",views.index,name="index"),
    url(r"^second/(\d+)/$",views.second,name="second"),
    url(r"^server/$",views.server,name="server"),
    url(r"^server2/$",views.server2,name="server2"),
    url(r"^server3/$",views.server3,name="server3")

]