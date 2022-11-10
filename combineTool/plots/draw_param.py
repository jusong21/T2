from ROOT import *
import re

def hist2d(par1, par2, title, xtitle, ytitle, outname):
	par1_txt = open(par1)
	par2_txt = open(par2)

	h = TH2D(title, title, 20, 0.5, 1.5, 20, 0.5, 1.5)
	h.SetXTitle(xtitle)
	h.SetYTitle(ytitle)
	for i in range(0, 1000):
		par1_line = re.split('   |/| ', par1_txt.readline())
		par2_line = re.split('   |/| ', par2_txt.readline())
		p1 = float(par1_line[4])
		p2 = float(par2_line[4])
		h.Fill(p1, p2)

	c = TCanvas('c', 'c', 3)
	gStyle.SetOptStat(0)
	h.Write()
	h.Draw('colz')
	c.Print(outname)


f_out = TFile('param2d.root', 'RECREATE')
hist2d('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par1.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par2.txt', 'Gen_1vsGen_2', 'ttbb_Gen_1', 'ttbb_Gen_2', 'Gen_1vsGen_2.pdf')
hist2d('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par1.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par3.txt', 'Gen_1vsGen_3', 'ttbb_Gen_1', 'ttbb_Gen_3', 'Gen_1vsGen_3.pdf')
hist2d('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par1.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par4.txt', 'Gen_1vsGen_4', 'ttbb_Gen_1', 'ttbb_Gen_4', 'Gen_1vsGen_4.pdf')
hist2d('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par2.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par3.txt', 'Gen_2vsGen_3', 'ttbb_Gen_2', 'ttbb_Gen_3', 'Gen_2vsGen_3.pdf')
hist2d('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par2.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par4.txt', 'Gen_2vsGen_4', 'ttbb_Gen_2', 'ttbb_Gen_4', 'Gen_2vsGen_4.pdf')
hist2d('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par3.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par4.txt', 'Gen_3vsGen_4', 'ttbb_Gen_3', 'ttbb_Gen_4', 'Gen_3vsGen_4.pdf')

hist2d('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/Pttbb/fitPttbb/par1.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/Pttbb/fitPttbb/par2.txt', 'ttbbvsttbj', 'ttbb', 'ttbj', 'ttbbvsttbj.pdf')
hist2d('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/Pttbb/fitPttbb/par1.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/Pttbb/fitPttbb/par3.txt', 'ttbbvsBkg', 'ttbb', 'Bkg', 'ttbbvsBkg.pdf')
hist2d('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/Pttbb/fitPttbb/par2.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/Pttbb/fitPttbb/par3.txt', 'ttbjvsBkg', 'ttbj', 'Bkg', 'ttbjvsBkg.pdf')

f_out.Close()
