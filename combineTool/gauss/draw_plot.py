from ROOT import *

def draw(hist):
	f = TFile('gausHist.root')
	h = f.Get(hist)

	c = TCanvas('c', 'c', 3)

	maxi = h.GetMaximum()*1.2
	h.SetMaximum(maxi)
	h.SetLineWidth(2)
	gStyle.SetStatBorderSize(0)
	h.Draw()
	c.Print(hist+'.pdf')

#draw('Bkg_ttcc+ttLF+ttother')
#draw('ttbj')
#draw('ttbb_Gen_1')
#draw('ttbb_Gen_2')
#draw('ttbb_Gen_3')
#draw('ttbb_Gen_4')
#draw('WJets')
#draw('TTTo2L2Nu')
#draw('TTToHadronic')
#draw('WJets_Pttbb')
#draw('TTTo2L2Nu_Pttbb')
#draw('TTToHadronic_Pttbb')
draw('Bkg_Pttbb')
draw('ttbj_Pttbb')
draw('ttbb_Pttbb')
