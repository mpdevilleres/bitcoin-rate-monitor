from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Provider


class ProviderListView(LoginRequiredMixin, ListView):
    model = Provider

    slug_field = 'name'
    slug_url_kwarg = 'name'


class ProviderDetailView(LoginRequiredMixin, DetailView):
    model = Provider

    slug_field = 'name'
    slug_url_kwarg = 'name'


class SummaryView(View):
    model = Provider
    template_name = 'main/provider_summary.html'

    def get(self, request, *args, **kwargs):
        providers = self.model.objects.all()
        latest_rates = [i.latest_rate for i in providers]
        average_rate = 0.0
        if len(latest_rates) != 0:
            average_rate = sum(latest_rates) / len(latest_rates)

        data = {
            'average_rate': average_rate,
            'providers': []
        }

        for provider in providers:
            detail = {
                'name': provider.name,
                'latest_rate': provider.latest_rate,
                'latest_update': provider.latest_rate_updated_on
            }

            detail.update({'differences': []})

            for i in providers:
                if i.name == provider.name:
                    continue
                detail['differences'].append({
                    'name': '{}'.format(i.name),
                    'rate': abs(provider.latest_rate - i.latest_rate)
                })

            data['providers'].append(detail)

        return render(request, self.template_name, {'data': data})
