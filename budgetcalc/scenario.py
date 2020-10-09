
'''conversion_mobile = .0035
conversion_desktop = .01
traffic = 1
aov_mobile = 550
aov_desktop = 500
cpc_mobile = 0.75
cpc_desktop = 1.25
mix_mobile = .3
mix_desktop = 1.0 - mix_mobile
'''
from django.http import HttpResponse




class scenario():

    def __init__(self, conversion_mobile, conversion_desktop, aov_mobile, aov_desktop, cpc_mobile, cpc_desktop, mix_mobile):
                self.conversion_mobile = conversion_mobile * .003
                self.conversion_desktop = conversion_desktop
                self.aov_mobile = aov_mobile
                self.aov_desktop = aov_desktop
                self.cpc_mobile = cpc_mobile
                self.cpc_desktop = cpc_desktop
                self.mix_mobile = mix_mobile
                self.mix_desktop = 1.0 - mix_mobile


    def modelRevenue(self,revenue):
        '''Insert Revenue Goal to find required spend'''
        transactions = revenue/((self.aov_mobile+self.aov_desktop)/2)
        sessions = transactions/((self.conversion_mobile+self.conversion_desktop)/2)
        #spend = sessions * ((self.cpc_mobile+self.cpc_desktop)/2)
        rpv = revenue/sessions
        d = dict();
        d['spend'] = sessions * ((self.cpc_mobile+self.cpc_desktop)/2)
        d['revenue'] = revenue
        d['traffic'] = sessions
        d['transactions'] = transactions
        d['rpv'] = rpv
        d['conversion_mobile'] = self.conversion_mobile
        d['conversion_desktop'] = self.conversion_desktop
        d['aov_mobile'] = self.aov_mobile
        d['aov_desktop'] = self.aov_desktop
        d['cpc_mobile'] = self.cpc_mobile
        d['cpc_desktop'] = self.cpc_desktop
        d['mix_mobile'] = self.mix_mobile
        d['mix_desktop'] = 1 - self.mix_mobile
        d['highlight'] = 1
        return d

    def modelSpend(self,spend):
        '''Insert Spend to see Revenue output'''
        traffic_m = (spend * self.mix_mobile)/self.cpc_mobile
        traffic_d = (spend * self.mix_desktop)/self.cpc_desktop
        revenue = (traffic_m * self.conversion_mobile * self.aov_mobile) + (traffic_d * self.conversion_desktop * self.aov_desktop)
        rpv = revenue/(traffic_d+traffic_m)
        d = dict();
        d['spend'] = spend
        d['revenue'] = revenue
        d['traffic'] = traffic_m+traffic_d
        d['transactions'] = (traffic_m+traffic_d) * ((self.conversion_mobile+self.conversion_desktop)/2)
        d['rpv'] = rpv
        d['conversion_mobile'] = self.conversion_mobile
        d['conversion_desktop'] = self.conversion_desktop
        d['aov_mobile'] = self.aov_mobile
        d['aov_desktop'] = self.aov_desktop
        d['cpc_mobile'] = self.cpc_mobile
        d['cpc_desktop'] = self.cpc_desktop
        d['mix_mobile'] = self.mix_mobile
        d['mix_desktop'] = 1 - self.mix_mobile
        d['highlight'] = 2
        return d





if __name__ == "__main__":

    sco = scenario(.0035,.01,120000000,750,500,0.75,1.25,0.3)
    predictSpend = sco.modelSpend(100000000)
    predictRevenue = sco.modelRevenue(1000000000)
    print(predictRevenue)
