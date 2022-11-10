import ROOT
from ROOT import *

#split ttbb into 4 by Gen bins

ntupleDir = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/'
target = 'split_ttbb.root'
saveLoc = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/fit/afterFit/'

f = TFile.Open(ntupleDir+target)
prob1 = [1.068, 0.967, 1.050, 1.314]
pttbb = [1.076, 0.973, 1.012, 1.009]

list_ttbb = pttbb
hist = 'h_Pttbb'
opt = 'UPDATE'

for i in range(1, len(list_ttbb)+1):
	f_out= TFile(saveLoc+'ttbb_Gen_'+str(i)+'.root', opt)
	h = f.Get(hist+'_Gen_'+str(i)).Clone()
	h_scale = h * list_ttbb[i-1]
	h_scale.SetName(hist)
	h_scale.Write()
	f_out.Close()


