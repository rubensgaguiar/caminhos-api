import stripe

from datetime import datetime

from core.models import Payment, Session, CustomerDetails, CustomerAddress

stripe.api_key = "sk_test_51HqiHpFm7x7XSTxAXGegtstsdrB3MJKlfwrfxGdZN8AfLJTdSm5QyHqbOQr3IO40uPenLpNG70LrCeNsynXNh0b500Chtup5xE"

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import make_aware

from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Index.")

@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']

    user = auth.authenticate(username=email, email=email, password=password)
    if user is not None:
        auth.login(request, user)
        # Redirect to a success page.
        return JsonResponse({
            "id": user.id,
            "email": user.email,
            "payment_status": user.payment.payment_status
        })

    return HttpResponse("Login Error", status=400)

def caminhos(request):
    return HttpResponse()

def logout(request):
    auth.logout(request)
    return HttpResponse()

@api_view(['POST'])
def signup(request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.create_user(username=email, email=email, password=password)

    Payment.objects.create(
        user=user,
        client_reference_id=str(user.id),
        payment_status="unpaid"
    )

    user.save()

    return JsonResponse({
        "id": user.id,
        "email": user.email,
    })

@api_view(['POST'])
def confirm_checkout(request):
    session_id = request.data['session_id']
    # curl https://api.stripe.com/v1/checkout/sessions/cs_test_a15HZMxTo1aSsDhwKvKku7Kzi2pjRFYJ4D5goKB7Y3Kv0SwyJfWQMnJj1d -u sk_test_51HqiHpFm7x7XSTxAXGegtstsdrB3MJKlfwrfxGdZN8AfLJTdSm5QyHqbOQr3IO40uPenLpNG70LrCeNsynXNh0b500Chtup5xE:
    session = stripe.checkout.Session.retrieve(session_id)

    user = User.objects.get(id=session["client_reference_id"])
    user.payment.client_reference_id = session["client_reference_id"]
    user.payment.payment_status = session["payment_status"]
    user.save()

    session_obj = Session.objects.create(
        user = user,
        session_id = session["id"],
        client_reference_id = session["client_reference_id"],
        created = make_aware(datetime.fromtimestamp(session["created"])),
        currency = session["currency"],
        customer = session["customer"],
        customer_creation = session["customer_creation"],
        customer_email = session["customer_email"],
        expires_at = make_aware(datetime.fromtimestamp(session["expires_at"])),
        livemode = session["livemode"],
        mode = session["mode"],
        session_object = session["object"],
        payment_intent = session["payment_intent"],
        payment_link = session["payment_link"],
        payment_status = session["payment_status"],
        setup_intent = session["setup_intent"],
        status = session["status"],
        submit_type = session["submit_type"],
        subscription = session["subscription"],
        success_url = session["success_url"],
        cancel_url = session["cancel_url"],
        url = session["url"]
    )

    customer_details = CustomerDetails.objects.create(
        customer_details = session_obj,
        email = session["customer_details"]["email"],
        name = session["customer_details"]["name"],
        phone = session["customer_details"]["phone"],
        tax_exempt = session["customer_details"]["tax_exempt"]
    )

    CustomerAddress.objects.create(
        address = customer_details,
        city = session["customer_details"]["address"]["city"],
        country = session["customer_details"]["address"]["country"],
        line1 = session["customer_details"]["address"]["line1"],
        lin2 = session["customer_details"]["address"]["line2"],
        postal_code = session["customer_details"]["address"]["postal_code"],
        state = session["customer_details"]["address"]["state"]
    )

    return JsonResponse({
        "payment_status": user.payment.payment_status
    })
