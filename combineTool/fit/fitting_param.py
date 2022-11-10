import ROOT
from ROOT import *
import sys,os

#split ttbb into 4 by Gen bins
#modi: Multiplying parameters for the .. background

ntupleDir = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/scalePttbb/'
#target = 'ttbj.root'
target = ['ttbj','ttcc','Bkg']
saveLoc = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/fit/afterFit/'

#Fixed background
#prob1 = [0.874, 0.960, 0.951]
#pttbb = [1.001, 0.977, 1.008]

ttbb_list = [1.469, 0.674, 1.394, 1.703]
bkg_list = [0.408, 0.769, 1.018]

hist = 'h_1stProb'

f_ttbb = TFile(ntupleDir+'scaled_ttbb.root')
for par in range(0, len(ttbb_list)):
	h = f_ttbb.Get(hist+'_Gen_'+str(par+1))
	
	f_out = TFile.Open(saveLoc+'ttbb_Gen_'+str(par+1)+'.root', 'RECREATE')
	h_mul = h.Clone()
	h_mul = h_mul * ttbb_list[par]
	h_mul.SetName(hist)
	h_mul.Write()
	f_out.Close()

for par in range(0, len(bkg_list)):

	f = TFile(ntupleDir+'scaled_'+target[par]+'.root')
	h = f.Get(hist)

	f_out = TFile.Open(saveLoc+'multiplied_'+target[par]+'.root', 'RECREATE')
	h_mul = h.Clone()
	h_mul = h_mul * bkg_list[par] 
	h_mul.SetName(hist)
	h_mul.Write()
	f_out.Close()


#for items in range(0, len(target)):
#
#    f = TFile.Open(ntupleDir+target[items]+".root")
#    hReco_dr = f.Get(hist)
#    
#    f_output = TFile.Open(saveLoc+'multiplied_'+target[items]+'.root',opt)
#    TH1 = hReco_dr.Clone()
#    print "prefit"
#    print TH1.GetBinContent(1)
#    print TH1.GetBinContent(2)
#    print TH1.GetBinContent(3)
#    print TH1.GetBinContent(4)
#   
#    TH1 = TH1 * param_list[items]
#    print "postfit"
#    print TH1.GetBinContent(1)
#    print TH1.GetBinContent(2)
#    print TH1.GetBinContent(3)
#    print TH1.GetBinContent(4)
#    
#    print "TH1 write and close"
#  
#    TH1.Write()
#    f_output.Close()
#    f.Close()
#
