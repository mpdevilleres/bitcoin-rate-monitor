from django.apps import AppConfig


class BitcoinRateConfig(AppConfig):
    name = 'bitcoin_rate_monitor.main'
    verbose_name = "Main"

    def ready(self):
        """Override this to put in:
            system checks
            signal registration
        """
        pass
