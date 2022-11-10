from ROOT import *

f1 = TFile.Open('rebinned_Bkg_ttcc+ttLF+ttother.root', 'read')
f2 = TFile.Open('rebinned_ttbj.root', 'read')
f3 = TFile.Open('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/ttbb.root')

hist = 'h_1stProb'
hist = 'h_Pttbb'
h1 = f1.Get(hist)
h2 = f2.Get(hist)
h3 = f3.Get(hist)

c = TCanvas('c', 'c', 3)
c.SetLeftMargin(0.12)
gStyle.SetOptStat(0)

h1.SetLineColor(kGreen)
h2.SetLineColor(kBlue)
h3.SetLineColor(kRed)
h1.SetLineWidth(2)
h2.SetLineWidth(2)
h3.SetLineWidth(2)

h1.Scale(1/h1.Integral())
h2.Scale(1/h2.Integral())
h3.Scale(1/h3.Integral())

maxi = max( h1.GetMaximum(), h2.GetMaximum(), h3.GetMaximum() )
h1.SetMaximum( maxi*1.2 )
h1.Draw('hist')
h2.Draw('hist same')
h3.Draw('hist same')

leg = TLegend(0.2, 0.8, 0.8, 0.85)
leg.SetNColumns(3)
leg.SetLineWidth(0)
leg.SetTextSize(.04)
leg.AddEntry(h3, 'ttbb')
leg.AddEntry(h2, 'ttbj')
leg.AddEntry(h1, 'ttcc+ttLF+ttother')
leg.Draw('same')

c.Print('h_Pttbb.pdf')
