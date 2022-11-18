from ROOT import *
from array import array
import os,sys

inputDir = '/home/juhee5819/cheer/T2/combineTool/data/scaled/'
outDir = '/home/juhee5819/cheer/T2/combineTool/data/rebin/'
del_Pttbb = [ 13, 14, 15,  17, 18, 19]
del_1stProb = [1, 2, 3, 4,  7, 9, 11, 13, 15, 17, 19]

def superHist(f):
	h = f.Get('h_dRbb_1stProb')
	nbins = h.GetNbinsX() * h.GetNbinsY()
	h_super = TH1D('h_1stProb_super', 'h_1stProb_super', nbins, 0, nbins)
	# ttbb
	if 'ttbb' in f.GetName():
		print('This is ttbb precess')
		for ibin in range(1, h.GetNbinsX()+1):
			h_gen_super = TH1D('h_1stProb_Gen_'+str(ibin)+'_super', 'h_1stProb_Gen_'+str(ibin)+'_super', nbins, 0, nbins)
			for jbin in range(1, h.GetNbinsX()+1):
				h_gen = f.Get('h_1stProb_Gen_'+str(ibin)+'_Reco_'+str(jbin))
				for kbin in range(1, h_gen.GetNbinsX()+1):
					binN = (jbin-1) * h_gen.GetNbinsX() + kbin
					h_gen_super.SetBinContent(binN, h_gen.GetBinContent(kbin))
			h_gen_super.Write()
			print('>>> Super histogram:', h_gen_super.GetName(), 'done')
			h_super.Add(h_gen_super)

	# not ttbb
	else:
		for ibin in range(1, h.GetNbinsX()+1):
			h_split = h.ProjectionY('h_1stProb_Reco_'+str(ibin), ibin, ibin)
			for jbin in range(1, h_split.GetNbinsX()+1):
				binN = (ibin-1) * h_split.GetNbinsX() + jbin
				h_super.SetBinContent(binN, h_split.GetBinContent(jbin))

	h_super.Write()
	print('>>> Super histogram:', h_super.GetName(), 'done')

def rebin(f, hist, hist_name, delIdx):
	h = f.Get(hist)
	lastbin = h.GetNbinsX() * h.GetBinWidth(1)
	binEdge = [h.GetBinLowEdge(i) for i in range(1, h.GetNbinsX()+1)]
	binEdge.append(lastbin)

	if '1stProb' in hist:
		temp = delIdx[:]
		for i in range(1, 4):
			add = [delIdx[j]+20*i for j in range(len(delIdx))]
			temp += add
		delIdx = temp[:]

	for idel in sorted(delIdx, reverse=True):
		del binEdge[idel]
	
	h_rebin = h.Rebin(len(binEdge)-1, hist, array('d', binEdge))
	h_rebin.SetName(hist_name)
	h_rebin.SetTitle(hist_name)
	h_rebin.Write()
	print('>>> Rebin histgram:', h_rebin.GetName(), 'done')

# main
for target in os.listdir(inputDir):
	if not target.endswith('.root'):
		continue
	process = target.split('.')[0]
	print('\n>>> Rebinning', process)
	f_in = TFile.Open(inputDir+target, 'READ')
	f_out = TFile.Open(outDir+'rebinned_'+process+'.root', 'RECREATE')
	superHist(f_in)

	rebin(f_in, 'h_Pttbb', 'h_Pttbb', del_Pttbb)
	if 'ttbb' in target:
		rebin(f_out, 'h_1stProb_Gen_1_super', 'h_1stProb_Gen_1', del_1stProb)
		rebin(f_out, 'h_1stProb_Gen_2_super', 'h_1stProb_Gen_2', del_1stProb)
		rebin(f_out, 'h_1stProb_Gen_3_super', 'h_1stProb_Gen_3', del_1stProb)
		rebin(f_out, 'h_1stProb_Gen_4_super', 'h_1stProb_Gen_4', del_1stProb)
	else:
		rebin(f_out, 'h_1stProb_super', 'h_1stProb', del_1stProb)

	f_out.Close()
	print('>>>', process, 'done')

