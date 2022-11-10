from ROOT import *
from array import array

def mkSuperHist( file, hist ):

	f = TFile.Open(file, 'UPDATE')
	h = f.Get(hist)
	rename = hist.split('_')[-1]

	nbins = h.GetNbinsX() * h.GetNbinsY()

	h_new = TH1D('h_1stProb_super', 'h_1stProb_super', nbins, 0, nbins)

	for ibin in range(1, h.GetNbinsX()+1):
		split_name = 'h_'+rename+'_Reco_'+str(ibin)
		h_split = h.ProjectionY(split_name, ibin, ibin)

		for jbin in range(1, h_split.GetNbinsX()+1):
			binN = (ibin-1)*h_split.GetNbinsX() + jbin
			print( 'bin ', binN)
			h_new.SetBinContent(binN, h_split.GetBinContent(jbin))

	h_new.Write()
	f.Close()

def mkSuperHistTtbb( file ):

	f = TFile.Open(file, 'UPDATE')
	h_temp = f.Get('h_1stProb')
	
	nbins = h_temp.GetNbinsX() * 4
	h_merge = TH1D('h_1stProb_super', 'h_1stProb_super', nbins, 0, nbins)
	for i in range(1, 5):
		h_new = TH1D('h_1stProb_super_Gen_'+str(i), 'h_1stProb_super_Gen_'+str(i), nbins, 0, nbins)

		for j in range(1, 5):
			h = f.Get('h_1stProb_Gen_'+str(i)+'_Reco_'+str(j))
			
			for k in range(1, h.GetNbinsX()+1):
				binN = (j-1)*h.GetNbinsX() + k
				h_new.SetBinContent(binN, h.GetBinContent(k))

		h_new.Write()
		h_merge.Add(h_new)

	h_merge.Write()
	f.Close()

inputDir = '/home/juhee5819/cheer/T2/combineTool/data/scaled/'
mkSuperHistTtbb(inputDir+'ttbb.root')
mkSuperHist(inputDir+'ttbj.root', 'h_dRbb_1stProb')
mkSuperHist(inputDir+'Bkg_ttcc+ttLF+ttother.root', 'h_dRbb_1stProb')
mkSuperHist(inputDir+'TTTo2L2Nu.root', 'h_dRbb_1stProb')
mkSuperHist(inputDir+'TTToHadronic.root', 'h_dRbb_1stProb')
mkSuperHist(inputDir+'WJetsToLNu.root', 'h_dRbb_1stProb')

