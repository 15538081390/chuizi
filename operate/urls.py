from django.conf.urls import url

from operate import views, tests
from operate import views

urlpatterns =[
    url(r"^login/$", views.login, name="login"),
<<<<<<< HEAD

=======
    url(r"^login/register/$", views.register, name = 'register'),
>>>>>>> b6529df94fe4278282f9aea10c2e6a179248d16c
    url(r"^smartisan/$",views.smartisan,name="smartisan"),

    url(r"^money/(\d+)/$",views.money,name="money"),
    url(r"^payment/$",views.payment,name="payment"),

]

