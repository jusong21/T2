from ROOT import *

def getE(file, hist):
	f = TFile(file)
	h = f.Get(hist)
	
	tot = 0
	for i in range(1, h.GetNbinsX()+1):
		#print h.GetBinContent(i)
		tot = tot + h.GetBinContent(i)
	
	print "tot ",tot
	return tot


def draw(file, hist, outname):
	f = TFile(file)
	
	num = getE(file, hist)

	print num
	h = f.Get(hist)
	c = TCanvas('c', 'c', 3)
	c.SetLeftMargin(0.15)
	gStyle.SetOptStat(0)


	h.Draw('hist')

	c.Print(outname)


#draw('random_ttbb.root', 'h_Pttbb_100', 'h_Pttbb_100_ttbb.pdf')
draw('scaleRatio/scale_ttbb.root', 'h_1stProb_100', 'h_1stProb_100_scale_ttbb.pdf')
