from ROOT import *
import math

def getRatio(file_in, txt_out, outname1, outname2):

	f = TFile(file_in) 
	txt = open(txt_out, 'w')

	ran_n = f.Get('h_Pttbb_1').GetEntries()
	sig = int(math.sqrt(ran_n))+150
	dis1 = TH1D('N_Pttbb', 'N_Pttbb', 50, ran_n-sig, ran_n+sig) 
	dis2 = TH1D('N_1stProb', 'N_1stProb', 50, ran_n-sig, ran_n+sig) 

	c = TCanvas('c', 'c', 3)
	gStyle.SetOptStat(0)

	for i in range(1, 1001):
		hist1 = 'h_Pttbb_'+str(i)
		hist2 = 'h_1stProb_'+str(i)

		h1 = f.Get(hist1)
		h2 = f.Get(hist2)

		e1 = h1.GetEntries()
		e2 = h2.GetEntries()

		dis1.Fill(e1)
		dis2.Fill(e2)

		r = round(float(e1/e2), 3)
		txt.write(str(r)+'\n')

	dis1.Draw()
	c.Print(outname1)
	c.Clear()
	dis2.Draw()
	c.Print(outname2)
	c.Clear()
	txt.close()


#getRatio('random_ttbb.root', 'ratio_ttbb.txt', 'N_Pttbb_ttbb.pdf', 'N_1stProb_ttbb.pdf')
getRatio('random_ttbj.root', 'ratio_ttbj.txt', 'N_Pttbb_ttbj.pdf', 'N_1stProb_ttbj.pdf')
getRatio('random_Bkg_ttcc+ttLF+ttother.root', 'ratio_Bkg.txt', 'N_Pttbb_Bkg.pdf', 'N_1stProb_Bkg.pdf')


