"""app URL Configuration

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
from django.urls import path
from leaks.views import DomainDataLeaksViewSet, EmailDataLeaksViewSet
from rest_framework_jwt.views import ObtainJSONWebToken, verify_jwt_token, refresh_jwt_token
from app.jwt import EmailJSONWebTokenSerializer


urlpatterns = [
    path(r'api/auth/login/', ObtainJSONWebToken.as_view(serializer_class=EmailJSONWebTokenSerializer)),
    path(r'api/auth/refresh/', refresh_jwt_token),
    path(r'api/auth/validate/', verify_jwt_token),

    # urls
    path('api/v1/email/dataleaks/', EmailDataLeaksViewSet.as_view({"get": "get"})),
    path('api/v1/domain/dataleaks/', DomainDataLeaksViewSet.as_view({"get": "get"}))
]
