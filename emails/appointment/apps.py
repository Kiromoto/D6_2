from django.apps import AppConfig


class AppointmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointment'

    def ready(self):
        import appointment.signals


        from .tasks import send_mail
        from .scheduler import appointment_scheduler
        print('def ready...OK! import...OK! Started!')

        appointment_scheduler.add_job(
            id='mail send',
            func=send_mail,
            trigger='interval',
            seconds=10,
        )

        appointment_scheduler.start()

