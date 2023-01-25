from django.shortcuts import render, redirect
import requests
import secrets
from django.contrib.auth.models import User
from .models import Payment
# Create your tests here.
from django.shortcuts import render, redirect
import requests 
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()


def funds_collection(request):
    configure()
    if request.method == 'POST':
        # gather required information from the user
        amount = request.POST.get("amount")
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        country = request.POST.get("country")
        transaction_ref = request.POST.get('transaction_ref') or secrets.token_urlsafe(50)
        redirect_url = request.POST.get("redirect_url")
        callbackurl = "wingipay.com"
        setAmountByCostomer = "false"

        # check if transaction_ref already exist
        while Payment.objects.filter(transaction_ref=transaction_ref).exists():
            transaction_ref = secrets.token_urlsafe(50)

        # make a POST request to the Funds Collection URL
        url = "https://test.wingipay.com/web/checkout/add/"
        payload = {
            "apikey": os.getenv("api_key"),
            "currency": "GHS",
            'phone': phone,
            "amount": amount,
            "full_name": full_name,
            "email": email,
            "country": country,
            "transaction_ref": transaction_ref,
            "callbackurl": callbackurl,
            "redirect_url": redirect_url,
            "setAmountByCostomer": setAmountByCostomer
        }
        response = requests.post(url, data=payload)

        # check for a successful response
        if response.json()["status"] == True:
            redirect_url = response.json()["redirect_url"]
            user = User.objects.get(email=email)
            Payment.objects.create(transaction_ref=transaction_ref, amount=amount, user=user, status='Pending')
            return redirect(redirect_url) # redirect the user to the redirect_url to complete their payment
        else:
            error_message = response.json()["exception"]
            return render(request, "payment_error.html", {"error_message": error_message})
    else:
        return render(request, 'funds_collection.html')
