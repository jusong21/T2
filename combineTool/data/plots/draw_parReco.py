from ROOT import *

def draw(file, hist, outname):
	f = TFile(file, 'READ')

	h = f.Get(hist)

	c = TCanvas('c', 'c', 3)
	c.SetLeftMargin(0.15)
	gStyle.SetOptStat(0)

	h.SetMaximum( h.GetMaximum()*1.2)
	h.SetLineWidth(2)
	h.Draw('hist')

	c.Print(outname)


draw('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/split_ttbb.root', 'h_1stProb_Gen_1_Reco_1', 'h_1stProb_Gen_1_Reco_1_ttbb.pdf')
draw('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/split_ttbb.root', 'h_1stProb_Gen_1_Reco_2', 'h_1stProb_Gen_1_Reco_2_ttbb.pdf')
draw('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/split_ttbb.root', 'h_1stProb_Gen_1_Reco_3', 'h_1stProb_Gen_1_Reco_3_ttbb.pdf')
draw('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/split_ttbb.root', 'h_1stProb_Gen_1_Reco_4', 'h_1stProb_Gen_1_Reco_4_ttbb.pdf')
draw('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/split_ttbb.root', 'h_1stProb_parReco_Gen_1', 'h_1stProb_parReco_Gen_1_ttbb.pdf')
draw('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/split_ttbb.root', 'h_1stProb_parReco_Gen_2', 'h_1stProb_parReco_Gen_2_ttbb.pdf')
draw('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/split_ttbb.root', 'h_1stProb_parReco_Gen_3', 'h_1stProb_parReco_Gen_3_ttbb.pdf')
draw('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/split_ttbb.root', 'h_1stProb_parReco_Gen_4', 'h_1stProb_parReco_Gen_4_ttbb.pdf')

draw('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/rebin/rebinned_ttbj.root', 'h_1stProb_parReco', 'h_1stProb_parReco_ttbb.pdf')
draw('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/rebin/rebinned_Bkg_ttcc+ttLF+ttother.root', 'h_1stProb_parReco', 'h_1stProb_parReco_Bkg_ttcc+ttLF+ttother_.pdf')

