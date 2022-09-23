from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Index.")

@csrf_exempt
@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = auth.authenticate(username=username, email=username, password=password)
    if user is not None:
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponse()

    return HttpResponse("Login Error", status=400)

@login_required(login_url='/login')
def caminhos(request):
    return HttpResponse()

@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return HttpResponse()

@api_view(['POST'])
def signup(request):
    try:
        username = request.data['username']
        password = request.data['password']

        user = User.objects.create_user(username=username, email=username, password=password)
        user.save()

        return HttpResponse()
    except Exception as e:
        return HttpResponse(e, status=400)

def confirm_payment(request):
    return HttpResponse()
