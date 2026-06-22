from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .gallery_data import gallery_items
import os


def home(request):
    return render(request, "home.html", {
        "calendly_url": os.getenv("CALENDLY_URL")
    })


def contact_view(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        recipient_email = os.getenv("CONTACT_RECEIVER")

        full_message = f"""
                        New message from SetsByRe website

                        Name: {name}
                        Email: {email}

                        Message:
                        {message}
                        """

        send_mail(
            subject,
            full_message,
            'selorm.etse5@gmail.com',
            [recipient_email],
            fail_silently=False,
        )

        messages.success(request, "Message sent successfully!")

    return redirect(f"{reverse('home')}#contact")


def gallery(request):
    return render(request, 'gallery.html', {
        "gallery_items": gallery_items,
        "calendly_url": os.getenv("CALENDLY_URL")
    })


def newsletter_subscribe(request):

    if request.method == "POST":

        recipient_email = os.getenv("CONTACT_RECEIVER")

        subscriber_email = request.POST.get("email")

        subject = "New Newsletter Subscription"

        message = f"""
                    A new user subscribed to the SetsByRe newsletter.

                    Subscriber Email:
                    {subscriber_email}
                    """

        send_mail(
            subject,
            message,
            'selorm.etse5@gmail.com',
            [recipient_email],
            fail_silently=False,
        )

        messages.success(
            request,
            "Thank you for subscribing!"
        )

    return redirect(f"{reverse('home')}#subscribe")

context = {
    "calendly_url": os.getenv("CALENDLY_URL")
}