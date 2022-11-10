from ROOT import *
from array import array

#f = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/ttbb.root')
f = TFile('/home/juhee5819/cheer/T2/combineTool/data/scaled/ttbb.root')
saveDir = '/home/juhee5819/cheer/T2/combineTool/data/scaled/'
#saveDir = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/'
new = TFile.Open(saveDir+'split_ttbb.root', 'RECREATE')

def splitPttbb(hist):
	h = f.Get(hist)
	rename = hist.split('_')[-1]

	h_bin = h.ProjectionZ('for bin', 1, 1, 1, 1)
	bins = [h_bin.GetBinLowEdge(i) for i in range(1, h_bin.GetNbinsX()+1)]
	bins.append(1.0)

	h_name = 'h_'+rename
	h_merge = TH1D(h_name, h_name, len(bins)-1, array('d', bins))
	for ibin in range(1, h.GetNbinsX()+1):
		split_name = 'h_'+rename+'_Gen_'+str(ibin)
		h_splitGen  = h.ProjectionZ(split_name, 1, h.GetNbinsX(), ibin, ibin)
		h_splitGen.Write()
		h_merge.Add(h_splitGen)
	h_merge.Write()

def split1stProb(hist):
	h = f.Get(hist)
	rename = hist.split('_')[-1]

	h_merge = TH1D('h_1stProb', 'h_1stProb', 20, 0, 20)
	for ibin in range(1, h.GetNbinsY()+1):
		split_name = 'h_'+rename+'parReco_Gen_'+str(ibin)
		h_splitGen = h.ProjectionZ(split_name, 1, h.GetNbinsX(), ibin, ibin)

		h_par = TH1D('h_1stProb_Gen_'+str(ibin),'h_1stProb_Gen_'+str(ibin), 20, 0, 20) 
#		else:
#			split_hist = h.ProjectionX(split_name, ibin, ibin)
					
		# split gen & reco
		for jbin in range(1, h.GetNbinsX()+1):
			split_name2 = split_name+'_Reco_'+str(jbin)
			h_splitReco = h.ProjectionZ(split_name2, jbin, jbin, ibin, ibin)
			h_splitReco.Write()
					
			for kbin in range(1, h_splitReco.GetNbinsX()+1):
				#print 'ibin ', ibin, 'kbin ', kbin
				binN = (jbin-1)*5 + kbin
				print 'bin ', binN
				h_par.SetBinContent( binN, h_splitReco.GetBinContent(kbin) )
		h_par.Write()
		h_merge.Add(h_par)
	h_merge.Write()

splitPttbb('h_responseMatrix_dRbb_Pttbb')
split1stProb('h_responseMatrix_dRbb_1stProb')

#splitGen('h_responseMatrix_mbb')
#splitGen('h_responseMatrix_dRbb')
#splitGen('h_responseMatrix_mbb_1stProb')
#splitGen('h_responseMatrix_dRbb_1stProb')
#splitGen('h_responseMatrix_mbb_Pttbb')
#splitGen('h_responseMatrix_dRbb_Pttbb')

#new.Write()
new.Close()

