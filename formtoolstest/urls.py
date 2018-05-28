"""formtoolstest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url

from .forms import NumberOfTicketsForm, PeopleForm, OtherForm
from .views import BookingWizard

named_forms = (
    ('step1', NumberOfTicketsForm),
    ('step2', PeopleForm),
)

contact_wizard = BookingWizard.as_view(
    named_forms, url_name='booking_step', done_step_name='other')

urlpatterns = [
    # path('booking/', BookingWizard.as_view()),
    url(r'^booking/(?P<step>.+)/$', contact_wizard, name='booking_step'),
    path('admin/', admin.site.urls),
]
