from ROOT import *

def getE(file, hist):
	f = TFile(file)
	h = f.Get(hist)
	
	tot = 0
	for i in range(1, h.GetNbinsX()+1):
		print h.GetBinContent(i)
		tot = tot + h.GetBinContent(i)
	
	print "tot ",tot


#getE("merge.root")
#getE("ttbj.root")
#getE("ttcc.root")
#getE("ttLF.root")
#getE("ttother.root")
#getE("rebinned_Bkg.root")
getE("../split_ttbb.root", 'h_1stProb_Gen_2_Reco_1')
getE("../split_ttbb.root", 'h_1stProb_Gen_2_Reco_2')
getE("../split_ttbb.root", 'h_1stProb_Gen_2_Reco_3')
getE("../split_ttbb.root", 'h_1stProb_Gen_2_Reco_4')
