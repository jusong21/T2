from ROOT import *

f = TFile('../split_ttbb.root')
#f = TFile('noRebin_split_ttbb.root')
colors = [kRed, kBlue, kGreen, kOrange]
h=[0, 0, 0, 0]

c = TCanvas('c', 'c', 3)
c.SetLeftMargin(0.15)
gStyle.SetOptStat(0)

leg = TLegend(0.19, 0.8, 0.89, 0.85)
leg.SetNColumns(4)
leg.SetLineWidth(0)
leg.SetTextSize(.04)


for i in range(0, 4):
	h[i] = f.Get('h_1stProb_parReco_Gen_'+str(i+1))
	h[i].SetLineColor(colors[i])
	h[i].SetLineWidth(2)
	h[i].Scale(1/h[i].Integral())
	leg.AddEntry(h[i], 'Gen_'+str(i+1))

maxi = max(h[0].GetMaximum(), h[1].GetMaximum(), h[2].GetMaximum(), h[3].GetMaximum())
h[0].SetMaximum(maxi*1.3)
h[0].SetTitle('')
h[0].SetYTitle('Normalized entries')
h[0].Draw('hist')
h[1].Draw('hist same')
h[2].Draw('hist same')
h[3].Draw('hist same')

leg.Draw('same')

c.Print('h_1stProb_ttbb.pdf')

