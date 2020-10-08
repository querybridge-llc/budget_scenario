
from django import forms
from .scenario import scenario
from django.http import HttpResponse




class MyForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    spend = forms.IntegerField()
    revenue = forms.IntegerField()
    conversion_mobile = forms.FloatField(initial=0.35)
    conversion_desktop = forms.FloatField(initial=0.35)
    #traffic = forms.IntegerField()
    aov_mobile = forms.IntegerField(initial=500)
    aov_desktop = forms.IntegerField(initial=500)
    cpc_mobile = forms.FloatField(initial=2.00)
    cpc_desktop = forms.FloatField(initial=3.00)
    mix_mobile = forms.FloatField(initial=.60)


    def estimate(self,spend,revenue):
        spend = self.cleaned_data.get('spend') #request['spend'].value()
        revenue = self.cleaned_data.get('revenue')
        conversion_mobile = self.cleaned_data.get('conversion_mobile')
        conversion_desktop = self.cleaned_data.get('conversion_desktop')
        #traffic = self.cleaned_data.get('traffic')
        aov_mobile = self.cleaned_data.get('aov_mobile')
        aov_desktop = self.cleaned_data.get('aov_desktop')
        cpc_mobile = self.cleaned_data.get('cpc_mobile')
        cpc_desktop = self.cleaned_data.get('cpc_desktop')
        mix_mobile = self.cleaned_data.get('mix_mobile')

        sco = scenario(conversion_mobile, conversion_desktop,
            aov_mobile, aov_desktop, cpc_mobile, cpc_desktop, mix_mobile)

        predictSpend = sco.modelSpend(spend)
        predictRevenue = sco.modelRevenue(revenue)

        context = {}
        context['predictSpend'] = predictSpend
        context['predictRevenue'] = predictRevenue

        return context #predictSpend #HttpResponse(str('spend'))
