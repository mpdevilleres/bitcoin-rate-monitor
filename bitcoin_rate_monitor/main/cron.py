def update_rates():
    from ..main.models import Provider
    provider_set = Provider.objects.all()
    for provider in provider_set:
        provider.do_update_rate()
        provider.save()
