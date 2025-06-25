from django.shortcuts import render, redirect
from django.urls import reverse
from urllib import request
from django.utils.http import urlencode
from django.views.generic import TemplateView, ListView, FormView, DetailView
from budgetcalc.forms import MyForm

class BudgetCalcView(TemplateView, FormView):
    template_name = 'budgetcalc.html'
    form_class = MyForm
    #success_url = 'budgetcalc/'

class RetirementView(TemplateView):
    template_name = 'ret_cal.html'

    def form_valid(self,form):
        #cleaned_data = super(self).clean()
        input = form.cleaned_data #cleaned_data

        spend = input['spend']#.get('spend')
        revenue = input['revenue']

        dx = form.estimate(spend,revenue)

        ps = dx['predictSpend']
        pr = dx['predictRevenue']

        if dx['predictSpend']['spend'] == 100:
            return redirect('/budgetcalc/?'+urlencode(pr))

        else: #if dx['predictRevenue']['spend'] == 100:
            return redirect('/budgetcalc/?'+urlencode(ps))
