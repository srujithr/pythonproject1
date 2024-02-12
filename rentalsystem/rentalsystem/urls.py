"""
URL configuration for carrental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rentalapps import views
from django.conf import settings
from django.urls import reverse

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\ main index page urls start  \\\\\\\\\\\\\\\\\\\\\\
    path('',views.index,name="indexs"),
    path('about',views.about, name='about'),
    path('car',views.car, name='car'),
    path('service',views.service, name='service'),
    path('contact',views.contact, name='contact'),
    path('user_register',views.user_register, name='user_register'),
    path('user_login',views.user_login, name='user_login'),
    path('company_register',views.company_register, name='company_register'),

# \\\\\\\\\\\\\\\\\ main index page urls end \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\ company page urls start \\\\\\\\\\\\\\\\\\\\\\

    path('add_car',views.add_car, name='add_car'),
    path('cmpnyindex',views.cmpnyindex, name='cmpnyindex'),
    path('user_page',views.user_page, name='user_page'),
    path('edit_car/<int:id>',views.edit_car, name="edit_car"),
    path('update_company',views.update_company, name='update_company'),
    path('view_car',views.view_car, name="view_car"),
    path('car_request/<int:id>',views.car_request, name='car_request'),
    path('view_requests',views.view_requests, name='view_requests'),
    path('delete/<int:id>',views.delete, name="delete"),

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\ company page urls end \\\\\\\\\\\\\\\\\\\\\\ 



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\ user page urls start \\\\\\\\\\\\\\\\\\\\\\ 
    path('user_requests',views.user_requests,name="user_requests"),

    path('userindex',views.userindex, name="userindex"),

    path('cars',views.cars, name='cars'),

    
    path('view_users',views.view_users, name='view_users'),
    path('car_search',views.car_search, name='car_search'),
    path('profile',views.profile, name="profile"),
    path('car_request/<int:id>',views.car_request,name='car_request'),

    path('statusrequest/<int:id>',views.statusrequest, name="statusrequest"),
    # path('view_car',views.view_car, name="view_car"),
    path('edit_profile/<int:id>',views.edit_profile, name="edit_profile"),
    # path('usercarlist',views.usercarlist,name='usercarlist'),
    path('cart/<int:id>',views.cart, name="cart"),
    # path('payments/<int:id>',views.payments, name='payments'),


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\ user page urls end \\\\\\\\\\\\\\\\\\\\\\ 

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\  logout urls end \\\\\\\\\\\\\\\\\\\\\\ 

path('userlogout',views.userlogout, name='userlogout'),
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\ logout end \\\\\\\\\\\\\\\\\\\\\\ 


path('update_status/<int:id>',views.update_status, name='update_status'),
path('history',views.history,name='history'),

path('review_add/<int:id>',views.review_add,name="review_add"),

path('userhistory',views.userhistory,name='userhistory'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)