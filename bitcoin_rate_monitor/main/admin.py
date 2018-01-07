from django import forms
from django.contrib import admin
from .models import Provider, Rate


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = '__all__'


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    form = ProviderForm
    readonly_fields = ['latest_rate', 'latest_rate_updated_on']


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    form = RateForm
