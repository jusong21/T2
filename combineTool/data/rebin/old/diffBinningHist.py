from ROOT import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--v', required=False)
args = parser.parse_args()
ver = args.v

def drawPttbb():
	f1 = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_ttbb_'+ver+'.root')
	f2 = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_ttbj_'+ver+'.root')
	f3 = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_Bkg_'+ver+'.root')
	f = [f1, f2, f3]
	#f = [f1, f2, f3, f4]
		
	name = ['ttbb', 'ttbj', 'Bkg']
	colors = [kRed, kBlue, kGreen, kOrange]
	#colors = [kBlue, kGreen, kOrange, kRed]
	
	h = [0,0,0]
	hmax = [0, 0, 0]
	
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
	
	c.Print('h_Pttbb_'+ver+'.pdf')


def draw1stProb():
	f1 = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_ttbb_'+ver+'.root')
	f2 = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_ttbj_'+ver+'.root')
	f3 = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_Bkg_'+ver+'.root')
	f = [f1, f2, f3]
	#f = [f1, f2, f3, f4]
		
	gen_name = ['Gen_1', 'Gen_2', 'Gen_3', 'Gen_4']
	gen_colors = [kRed, kBlue, kGreen, kOrange]
	name = ['ttbb', 'ttbj', 'Bkg']
	colors = [kCyan, kCyan, kMagenta]
	
	h = [0,0,0, 0, 0, 0]
	hmax = [0, 0, 0, 0, 0, 0]
	
	c = TCanvas('c', 'c', 3)
	c.SetLeftMargin(0.15)
	gStyle.SetOptStat(0)
	
	leg = TLegend(0.2, 0.75, 0.87, 0.85)
	leg.SetNColumns(4)
	leg.SetLineWidth(0)
	leg.SetTextSize(.04)
		
	for i in range(0, len(f)):
		if i==0:
			for j in range(0, 4):
				h[j] = f[i].Get('h_1stProb_Gen_'+str(j+1))
				h[j].SetLineColor(gen_colors[j])
				h[j].SetLineWidth(2)
				h[j].Scale(1/h[j].Integral())
				leg.AddEntry(h[j], gen_name[j])
				hmax[j] = h[j].GetMaximum()
		else:	
			n = i+3
			print n
			h[n] = f[i].Get('h_1stProb')
			h[n].SetLineColor(colors[i])
			h[n].SetLineWidth(2)
			h[n].Scale(1/h[n].Integral())
			leg.AddEntry(h[n], name[i])
			hmax[n] = h[n].GetMaximum()
	
	maxi = max(hmax)
	
	h[5].SetMaximum(maxi*1.3)
	h[5].SetYTitle('Normalized entries')
	h[5].Draw('hist')
	h[4].Draw('hist same')
	h[3].Draw('hist same')
	h[2].Draw('hist same')
	h[1].Draw('hist same')
	h[0].Draw('hist same')
	
	leg.Draw('same')
	
	c.Print('h_1stProb_'+ver+'.pdf')


drawPttbb()
draw1stProb()
