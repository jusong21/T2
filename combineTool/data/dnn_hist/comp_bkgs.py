from ROOT import *

#f1 = TFile('hist_TTToSemiLeptonic_ttbj_2018.root')
#f2 = TFile('hist_TTToSemiLeptonic_ttcc_2018.root')
#f3 = TFile('hist_TTToSemiLeptonic_ttother_2018.root')
f1 = TFile('hist_TTToSemiLeptonic_ttbj_2018.root')
f2 = TFile('hist_TTToSemiLeptonic_ttcc_2018.root')
f3 = TFile('hist_TTToSemiLeptonic_Bkg.root')
f = [f1, f2, f3]

name = ['ttbj', 'ttcc', 'ttLF+ttother']
colors = [kRed, kBlue, kGreen, kOrange]
h=[0, 0, 0]

c = TCanvas('c', 'c', 3)
c.SetLeftMargin(0.15)
gStyle.SetOptStat(0)

leg = TLegend(0.2, 0.8, 0.8, 0.85)
leg.SetNColumns(3)
leg.SetLineWidth(0)
leg.SetTextSize(.04)

for i in range(0, 3):
	h[i] = f[i].Get('h_Pttbb')
	h[i].SetLineColor(colors[i])
	h[i].SetLineWidth(2)
	h[i].Scale(1/h[i].Integral())
	leg.AddEntry(h[i], name[i])

maxi = max(h[0].GetMaximum(), h[1].GetMaximum(), h[2].GetMaximum())
h[0].SetMaximum(maxi*1.3)
h[0].Draw('hist')
h[1].Draw('hist same')
h[2].Draw('hist same')

leg.Draw('same')

c.Print('h_Pttbb_bkgs.pdf')


