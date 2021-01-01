
conversion_mobile_2020 = .0028198688
conversion_desktop_2020 = .007603823670
aov_mobile_2020 = 436.76
aov_desktop_2020 = 532.93
cpc_mobile_2020 = .69
cpc_desktop_2020 = .96
mix_mobile_2020 = .7239
mix_desktop_2020 = 1.0 - mix_mobile_2020

from django.http import HttpResponse




class scenario():

    def __init__(self, conversion_mobile, conversion_desktop, aov_mobile, aov_desktop, cpc_mobile, cpc_desktop, mix_mobile):
                self.conversion_mobile = conversion_mobile_2020 + ((conversion_mobile/100) * conversion_mobile_2020)
                self.conversion_desktop = conversion_desktop_2020 + ((conversion_desktop/100)* conversion_desktop_2020)
                self.aov_mobile = aov_mobile_2020 + ((aov_mobile/100) * aov_mobile_2020)
                self.aov_desktop = aov_desktop_2020 + ((aov_desktop/100) * aov_desktop_2020)
                self.cpc_mobile = cpc_mobile_2020 + ((cpc_mobile/100) * cpc_mobile_2020)
                self.cpc_desktop = cpc_desktop_2020 + ((cpc_desktop/100) * cpc_desktop_2020)
                self.mix_mobile = mix_mobile_2020 + ((mix_mobile/100) * mix_mobile_2020)
                self.mix_desktop = 1-self.mix_mobile


    def modelRevenue(self,revenue):
            '''Insert Revenue Goal to find required spend'''
            spend = revenue / ( (self.mix_mobile*self.conversion_mobile*self.aov_mobile) / self.cpc_mobile +
                                (self.mix_desktop*self.conversion_desktop*self.aov_desktop) /self.cpc_desktop )
            traffic_m = (spend * self.mix_mobile)/self.cpc_mobile
            traffic_d = (spend * self.mix_desktop) / self.cpc_desktop
            transactions = ((traffic_m+traffic_d) * ((self.conversion_mobile+self.conversion_desktop)/2))* .6995
            aov = revenue/transactions
            sessions = (traffic_m+traffic_d) *.8710
            ##spend = sessions * ((self.cpc_mobile+self.cpc_desktop)/2)
            rpv = revenue/sessions
            d = dict();
            d['spend'] = spend
            #d['spend'] = sessions * ((self.cpc_mobile+self.cpc_desktop)/2)
            d['revenue'] = revenue
            d['aov']= aov
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
        traffic = (traffic_m+traffic_d) * 0.8710
        revenue = (traffic_m * self.conversion_mobile * self.aov_mobile) + (traffic_d * self.conversion_desktop * self.aov_desktop)
        rpv = revenue/traffic
        aov = revenue/(((traffic_m+traffic_d) * ((self.conversion_mobile+self.conversion_desktop)/2)) * 0.6995)
        d = dict();
        d['spend'] = spend
        d['revenue'] = revenue
        d['aov']= aov
        d['traffic'] = traffic
        d['transactions'] = ((traffic_m+traffic_d) * ((self.conversion_mobile+self.conversion_desktop)/2)) * 0.6995
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

    sco = scenario(.0033,.0043,489.3,516,0.59,2.09,0.6984)
    predictSpend = sco.modelSpend(237037037)
    predictRevenue = sco.modelRevenue(1000000000)
    print(predictSpend)
    #print(mix_desktop)



