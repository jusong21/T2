from ROOT import *

f1 = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/ttbj.root')
f2 = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/ttcc.root')
f3 = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/Bkg_ttLF+ttother.root')
#f4 = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/dnn_hist/notRebin_ttbb_2018.root')
f = [f1, f2, f3]
#f = [f1, f2, f3, f4]
	
name = ['ttbj', 'ttcc', 'ttLF+ttother', 'ttbb']
colors = [kRed, kBlue, kGreen, kOrange]
#colors = [kBlue, kGreen, kOrange, kRed]

h = [0,0,0]
hmax = [0, 0, 0]

#h = [0,0,0,0]
#hmax = [0, 0, 0, 0]

c = TCanvas('c', 'c', 3)
c.SetLeftMargin(0.15)
gStyle.SetOptStat(0)

leg = TLegend(0.2, 0.8, 0.8, 0.85)
leg.SetNColumns(len(f))
leg.SetLineWidth(0)
leg.SetTextSize(.04)
	
for i in range(0, len(f)):
	h[i] = f[i].Get('h_Pttbb')
	h[i].SetLineColor(colors[i])
	h[i].SetLineWidth(2)
	h[i].Scale(1/h[i].Integral())
	leg.AddEntry(h[i], name[i])
	hmax[i] = h[i].GetMaximum()

maxi = max(hmax)

h[0].SetMaximum(maxi*1.3)
h[0].SetYTitle('Normalized entries')
h[0].Draw('hist')
h[1].Draw('hist same')
h[2].Draw('hist same')
#h[3].Draw('hist same')

leg.Draw('same')

c.Print('h_Pttbb.pdf')

#def comp(f, name, outname):
#	colors = [kRed, kBlue, kGreen, kOrange]
#	h=[]
#	h = [0 for i in range(0, len(f))]
#	c = TCanvas('c', 'c', 3)
#	c.SetLeftMargin(0.15)
#	gStyle.SetOptStat(0)
#	
#	leg = TLegend(0.2, 0.8, 0.8, 0.85)
#	leg.SetNColumns(len(f))
#	leg.SetLineWidth(0)
#	leg.SetTextSize(.04)
#	
#	for i in range(0, len(f)):
#		print f[i]
#		rf = TFile(f[i])
#		hist = rf.Get('h_Pttbb')
#		h[i] = hist
#		print hist
#		#h[i] = f[i].Get('h_Pttbb')
#		print colors[i]
#		h[i].SetLineColor(colors[i])
#		h[i].SetLineWidth(2)
#		h[i].Scale(1/h[i].Integral())
#		leg.AddEntry(h[i], name[i])
#	
#	maxi = 0
#	for i in range(0, len(h)):
#		print h[i]
#		hmax = h[i].GetMaximum()
#		print 'hmax ', hmax
#		#if hmax > maxi: 
#		#	maxi = max(maxi, hmax)
#		
#	h[0].SetMaximum(maxi*1.3)
#	h[0].Draw('hist')
#	for i in range(1, len(h)):
#		h[i].Draw('hist same')
#	
#	#maxi = max(h[0].GetMaximum(), h[1].GetMaximum())
#	#h[0].SetMaximum(maxi*1.3)
#	#h[0].Draw('hist')
#	#h[1].Draw('hist same')
#	
#	leg.Draw('same')
#	
#	c.Print(outname)
#
#comp(['/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/ttbj.root', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/ttcc.root', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/Bkg_ttLF+ttother.root'], ['ttbj', 'ttcc', 'ttLF+ttother'], 'h_Pttbb_bkgs.pdf')
#
#
