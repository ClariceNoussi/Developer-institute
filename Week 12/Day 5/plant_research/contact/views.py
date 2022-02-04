from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from plant_research import settings
from .models import Contact


def contact(request,):
    if request.method == "POST":
        product_id = request.POST['product_id']
        product = request.POST['product']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        # Check if user has made inquiry already:
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(product_id=product_id, user_id=request.user)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this product')
                return redirect('/products/'+product_id)

        contact = Contact(lproduct=product, product_id=product_id, name=name, email=email, phone=phone, message=message, user_id=request.user )

        contact.save()


        send_mail(
            'Property product Inquiry',
            'There has been an inquiry for' + product + '. Sign in to the admin panel for more information.',
            settings.EMAIL_HOST_USER,
            ['clarice.djouwoug@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been succesfully submitted, we will get back to you soon')
        return redirect('/products/'+product_id)
