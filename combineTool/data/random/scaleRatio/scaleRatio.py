from ROOT import *
import math

def getRatio(file_in, file_out):

	f = TFile(file_in) 
	f_out = TFile(file_out, 'RECREATE')

	for i in range(1, 1001):
		hist1 = 'h_Pttbb_'+str(i)
		hist2 = 'h_1stProb_'+str(i)

		h1 = f.Get(hist1)
		h2 = f.Get(hist2)

		e1 = h1.GetEntries()
		e2 = h2.GetEntries()

		r = float(e1/e2)

		h2_scale = h2*r
		h2_scale.Write()

	f_out.Close()


getRatio('../random_ttbb.root', 'scale_ttbb.root')
getRatio('../random_ttbj.root', 'scale_ttbj.root')
getRatio('../random_Bkg_ttcc+ttLF+ttother.root', 'scale_Bkg.root')
getRatio('../random_TTTo2L2Nu.root', 'scale_TTTo2L2Nu.root')
getRatio('../random_TTToHadronic.root', 'scale_TTToHadronic.root')
getRatio('../random_WJetsToLNu.root', 'scale_WJetsToLNu.root')
