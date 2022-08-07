from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_managers
from .models import Appointment
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail


@receiver(post_save, sender=Appointment)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.client_name} {instance.date.strftime("%Y-%m-%d")}'
    else:
        subject = f'Appointment changed for {instance.client_name} {instance.date.strftime("%Y-%m-%d")}'

    html_content = render_to_string('appointment_created.html', {'appointment': instance, })

    msg = EmailMultiAlternatives(subject=subject,
                                 body=instance.message,
                                 from_email='tlfordjango@mail.ru',
                                 to=['kiromotossindzi@gmail.com', ],
                                 )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@receiver(post_delete, sender=Appointment)
def notify_managers_appointment(sender, instance,  **kwargs):
    send_mail(subject=f'{instance.client_name} has deleted appointment!',
              message=f'Canceled appointment for {instance.date.strftime("%Y-%m-%d")} about: {instance.message}',
              from_email='tlfordjango@mail.ru',
              recipient_list=['kiromotossindzi@gmail.com', ],
              )
