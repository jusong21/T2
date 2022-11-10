import ROOT
from ROOT import *

#split ttbb into 4 by Gen bins

ntupleDir = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/'
#target = 'split_ttbb.root'
#target = ['split_ttbb', 'ttbj', 'ttcc', 'Bkg']
#target = ['split_ttbb', 'rebinned_ttbj', 'new_Bkg']
target = ['split_ttbb', 'rebinned_ttbj', 'rebinned_Bkg']
saveLoc = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/scalePttbb/'

#param_list = [18.902, 19.630, 15.338, 19.647]
param_list = [1.013, 0.722, 1.137]
#param_list = [1.005, 0.997]

#hist = 'h_Pttbb'
hist = 'h_1stProb'
opt = 'update'
#opt = 'recreate'


for i in range(0, len(param_list)):
	f = TFile(ntupleDir+target[i]+'.root', 'read')
	h_def = f.Get(hist)

	if 'ttbb' in target[i]:
		f_out = TFile(saveLoc+'scaled_ttbb_3.root', opt)
		for igen in range(1, 5):
			h_def = f.Get(hist+'_Gen_'+str(igen)).Clone()
			h_scale = h_def * param_list[i]
			h_scale.SetName(hist+'_Gen_'+str(igen))
			h_scale.Write()
		f_out.Close()
	else:
		f_out = TFile(saveLoc+'scaled_'+target[i]+'_3.root', opt)
		h_def = f.Get(hist)
		h_scale = h_def * param_list[i]
		h_scale.SetName(hist)
		h_scale.Write()
		f_out.Close()

