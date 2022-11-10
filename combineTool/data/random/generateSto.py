from ROOT import *
from array import array
import math
import time

def getE(file, hist):
	f = TFile(file)
	h = f.Get(hist)

	tot = 0 
	for i in range(1, h.GetNbinsX()+1):
	#	print h.GetBinContent(i)
		tot = tot + h.GetBinContent(i)
	
	print "tot ",tot
	f.Close()
	return int(round(tot))

def ran( f, hist, hist_name, lastbin):

	h = f.Get(hist)

	entries = 0
	for i in range(1, h.GetNbinsX()+1):
		entries = entries + h.GetBinContent(i)

	bins = [h.GetBinLowEdge(i) for i in range(1, h.GetNbinsX()+1)]
	bins.append(lastbin)
	print(bins)
	print entries

	gRandom.SetSeed(int(time.time()))
	ran_entries = 0
	sig = int(math.sqrt(entries))
	for i in range(0, 1000):
		h_name = hist_name+'_'+str(i+1)
		h_ran = TH1F(h_name, h_name, len(bins)-1, array('d', bins))
		#print h
		ran_entries = int(gRandom.Gaus(entries, sig))
		h_ran.FillRandom(h, ran_entries)
		h_ran.Write()


# ttbb
print '\nGenerate random ttbb hists'

inputDir = '/home/juhee5819/cheer/T2/combineTool/data/scaled/'

f_ttbb = TFile(inputDir+'ttbb.root')
f_ttbb_out = TFile('random_ttbb.root', 'RECREATE')
ran(f_ttbb,  'h_Pttbb', 'h_Pttbb', 1)
ran(f_ttbb,  'h_1stProb_super', 'h_1stProb', 80)
f_ttbb_out.Close()
print 'ttbb done'

# ttbj
print '\nGenerate random ttbj hists'

f_ttbj = TFile(inputDir+'ttbj.root')
f_ttbj_out = TFile('random_ttbj.root', 'RECREATE')
ran(f_ttbj,  'h_Pttbb', 'h_Pttbb', 1)
ran(f_ttbj,  'h_1stProb_super', 'h_1stProb', 80)
f_ttbj_out.Close()
print 'ttbj done'

# Bkg ttcc+ttLF+ttother
print '\nGenerate random Bkg hists'

f_Bkg = TFile(inputDir+'Bkg_ttcc+ttLF+ttother.root')
f_Bkg_out = TFile('random_Bkg_ttcc+ttLF+ttother.root', 'RECREATE')
ran(f_Bkg,  'h_Pttbb', 'h_Pttbb', 1)
ran(f_Bkg,  'h_1stProb_super', 'h_1stProb', 80)
f_Bkg_out.Close()
print 'Bkg done'
#
f_TTTo2L2Nu = TFile(inputDir+'TTTo2L2Nu.root')
f_TTTo2L2Nu_out = TFile('random_TTTo2L2Nu.root', 'RECREATE')
ran(f_TTTo2L2Nu,  'h_Pttbb', 'h_Pttbb', 1)
ran(f_TTTo2L2Nu,  'h_1stProb_super', 'h_1stProb', 80)
f_TTTo2L2Nu_out.Close()
print 'TTTo2L2Nu done'

f_TTToHadronic = TFile(inputDir+'TTToHadronic.root')
f_TTToHadronic_out = TFile('random_TTToHadronic.root', 'RECREATE')
ran(f_TTToHadronic,  'h_Pttbb', 'h_Pttbb', 1)
ran(f_TTToHadronic,  'h_1stProb_super', 'h_1stProb', 80)
f_TTToHadronic_out.Close()
print 'TTToHadronic done'

f_WJetsToLNu = TFile(inputDir+'WJetsToLNu.root')
f_WJetsToLNu_out = TFile('random_WJetsToLNu.root', 'RECREATE')
ran(f_WJetsToLNu,  'h_Pttbb', 'h_Pttbb', 1)
ran(f_WJetsToLNu,  'h_1stProb_super', 'h_1stProb', 80)
f_WJetsToLNu_out.Close()
print 'WJetsToLNu done'

#


#f = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/rebin/rebinned_merge.root')
#
#h_1stProb = f.Get('h_1stProb_parReco')
##h_Pttbb = f.Get('h_Pttbb')
#
#bins_1stProb = [h_1stProb.GetBinLowEdge(i) for i in range(1, h_1stProb.GetNbinsX()+1)]
#bins_1stProb.append(1.0)
##bins_Pttbb = [h_Pttbb.GetBinLowEdge(i) for i in range(1, h_Pttbb.GetNbinsX()+1)]
##bins_Pttbb.append(1.0)
#
##f_out = TFile.Open('scaled/random_data.root', 'RECREATE')
#f_out = TFile.Open('parReco_data.root', 'RECREATE')
#
#for i in range(0, 1000):
#	h_name1 = 'h_1stProb_parReco_'+str(i+1)
##	h_name2 = 'h_Pttbb_'+str(i+1)
#	#h_1stProb_ran = TH1F(h_name1, h_name1, len(bins_1stProb)-1, array('d', bins_1stProb))
#	h_1stProb_ran = TH1F(h_name1, h_name1, 20, 0, 20)
##	h_Pttbb_ran = TH1F(h_name2, h_name2, len(bins_Pttbb)-1, array('d', bins_Pttbb))
#	h_1stProb_ran.FillRandom(h_1stProb, 5272)
##	h_Pttbb_ran.FillRandom(h_Pttbb, 5272)
#	h_1stProb_ran.Write()
##	h_Pttbb_ran.Write()
#
##h_1stProb_ran = TH1F('h_1stProb', 'h_1stProb', len(bins_1stProb)-1, array('d', bins_1stProb))
##h_Pttbb_ran = TH1F('h_Pttbb', 'h_Pttbb', len(bins_Pttbb)-1, array('d', bins_Pttbb))
##
##h_1stProb_ran.FillRandom(h_1stProb, 5272)
##h_Pttbb_ran.FillRandom(h_Pttbb, 5272)
##h_1stProb_ran.FillRandom(h_1stProb, 100000)
##h_Pttbb_ran.FillRandom(h_Pttbb, 100000)
#
#
##f_out.Write()
#f_out.Close()
