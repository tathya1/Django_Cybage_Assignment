from django.apps import AppConfig


class EmployeeAppConfig(AppConfig):
    name = 'employee_app'

    def ready(self):
        import employee_app.signals
