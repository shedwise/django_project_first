from django.shortcuts import redirect
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create email views here.
def send_message(request):
    if request.method == 'POST':
        receiver_email = request.POST.get('receiver_email')
        email_title = request.POST.get('email_title')
        message_body = request.POST.get('message_body')
        sender_name = request.POST.get('sender_name')
        sender_contact = request.POST.get('sender_contact')
        sender_email = request.POST.get('sender_email')
        student_slug = request.POST.get("student_slug")

        # Validate the email format of the recipient
        try:
            validate_email(receiver_email)
        except ValidationError:
            messages.error(request, "Invalid email format for receiver.")
            return redirect('profile')  # Adjust if you need to redirect elsewhere

        # Prepare the email content
        email_content = f"From: {sender_name}\nContact: {sender_contact}\n\nMessage:\n{message_body}"

        # Send the email
        try:
            send_mail(
                subject=email_title,
                message=email_content,
                from_email=sender_email,
                recipient_list=[receiver_email],
                fail_silently=False,
            )
            messages.success(request, "Message sent successfully.")
        except Exception as e:
            messages.error(request, f"Failed to send message: {e}")

        return redirect('profile', slug =student_slug )  # Redirect back to the profile page
    else:
     return redirect('html/index.html')
