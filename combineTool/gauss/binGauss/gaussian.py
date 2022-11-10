from ROOT import *
import pandas as pd
import numpy as np
from root_numpy import array2tree

def test(file, file_out, text_out):
	f = TFile(file)

	hists = ['h_Pttbb', 'h_1stProb']
	data = []
	for hist in hists:
		nbins = f.Get(hist+'_1').GetNbinsX()
		d = pd.DataFrame(columns=range(nbins))
		d.name = hist

		for ihist in range(1, 1001):
			hist_name = hist+'_'+str(ihist)
			h = f.Get(hist_name)
	
			#nbins = h.GetNbinsX()
			contents = []
			for ibin in range(1, nbins+1):
				contents.append(h.GetBinContent(ibin))
			#print '\n', ihist, ' ', contents
			
			d.loc[ihist-1] = contents
			#d.append(contents, ignore_index=True)
		#print '\n', d
		data.append(d)
	#print data

	f_out = TFile(file_out, 'RECREATE')
	
	for d in data:
		tot = 0
		for icol in range(0, len(d.columns)):
		#for icol in range(0, 1):
			counts = d[icol]
			title = d.name+'_bin_'+str(icol+1)

			mini = min(counts)
			maxi = max(counts)
			
			h_fit = TH1D(title, title, int(maxi-mini+3), min(counts), max(counts))
			for i in range(0, len(counts)):
				h_fit.Fill(counts[i])
			h_fit.Fit('gaus')
			mean_gauss = h_fit.GetListOfFunctions().FindObject('gaus').GetParameter(1)
			sig_gauss = h_fit.GetListOfFunctions().FindObject('gaus').GetParameter(2)
			tot = tot+mean_gauss

			with open(text_out, 'a') as log:
				log.write(title+'\n')
				log.write('mean: '+str(mean_gauss)+'\n')
				log.write('sigma: '+str(sig_gauss)+'\n\n')
#			counts_arr = np.array(counts, dtype=[('counts', np.float32)])
#			tree = array2tree(counts_arr)
#
#			count = RooRealVar("counts", title, mini-1, maxi+1)
#			
#			count.setBins(int(maxi-mini+3))
#			mean = RooRealVar("mean", "mean", counts.mean(), 0, maxi)
#			sig = RooRealVar("sigma", "sigma", counts.std(), 0, maxi)
#			
#			name = 'data'
#			data = RooDataSet( name, name, RooArgSet(count), RooFit.Import(tree) )
#			
#			gauss = RooGaussian("Gaussian", "Gaussian", count, mean, sig)
#			result = gauss.fitTo(data, RooFit.Save())
#		
#			xframe = count.frame(RooFit.Title(title))
#			data.plotOn(xframe)
#			gauss.plotOn(xframe)
#			maxiy = xframe.GetMaximum() * 1.1
#			xframe.SetMaximum( maxiy )
#		
#			data.statOn(xframe, RooFit.Layout(0.62, 0.88, 0.89))
#			st1 = xframe.getAttText()
#			st1.SetBorderSize(0)
#			st1.SetTextSize(0.026)
#			gauss.paramOn(xframe, RooFit.Layout(0.62, 0.88, 0.71))
#			st2 = xframe.getAttText()
#			st2.SetBorderSize(0)
#			st2.SetTextSize(0.026)
#		
#			#gauss.GetListOfFuntions().FindObject/
#			#c = TCanvas('c', 'c', 3)
#			#c.SetLeftMargin(0.15)
#			
#			xframe.GetXaxis().SetTitleSize(0.04)
#			xframe.GetYaxis().SetTitleSize(0.04)
#			#xframe.Draw()
#			
#			f_out.WriteObject(xframe, title)
#			with open(text_out, 'a') as log:
#				log.write(title+'\n')
#				log.write(str(result.floatParsFinal().find(mean)))
#				log.write(str(result.floatParsFinal().find(sig))+'\n')
#
		with open(text_out, 'a') as log:
			log.write('Total of entries: '+str(tot)+'\n\n')
	f_out.Close()
test('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/random/random_ttbb.root',  'ttbb_binFit.root', 'ttbb_binFit.txt')
test('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/random/random_ttbj.root',  'ttbj_binFit.root', 'ttbj_binFit.txt')
test('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/random/random_Bkg_ttcc+ttLF+ttother.root',  'Bkg_ttcc+ttLF+ttother_binFit.root', 'Bkg_ttcc+ttLF+ttother_binFit.txt')

#def fit(par, title, outname):
#	d = pd.read_fwf(par , header=None)
#	d = d.loc[ d[0]>0 ]
#
#	counts = d[0]
#	
#	counts_arr = np.array( counts , dtype=[('counts', np.float32)])
#	tree = array2tree(counts_arr)
#	
#	count = RooRealVar("counts", "Fitting parameter", 0, 2 )
#	count.setBins(20)
#	mean = RooRealVar("mean", "mean", counts.mean(), 0, 3)
#	sig = RooRealVar("sigma", "sigma", counts.std(), 0, 3)
#	
#	name = 'data'
#	data = RooDataSet( name, name, RooArgSet(count), RooFit.Import(tree) )
#	
#	gauss = RooGaussian("Gaussian", "Gaussian", count, mean, sig)
#	result = gauss.fitTo(data, RooFit.Save())
#
#	log = std.ofstream('result_gauss.txt')
#	result.floatParsFinal().printMultiline(log, 1111, True)
#	result.floatParsFinal().printValue(log)
#	log.close()
#
#	xframe = count.frame(RooFit.Title(title))
#	data.plotOn(xframe)
#	gauss.plotOn(xframe)
#	maxi = xframe.GetMaximum() * 1.1
#	xframe.SetMaximum( maxi )
#
#	data.statOn(xframe, RooFit.Layout(0.62, 0.88, 0.89))
#	st1 = xframe.getAttText()
#	st1.SetBorderSize(0)
#	st1.SetTextSize(0.026)
#	gauss.paramOn(xframe, RooFit.Layout(0.62, 0.88, 0.71))
#	st2 = xframe.getAttText()
#	st2.SetBorderSize(0)
#	st2.SetTextSize(0.026)
#	
#	#xframe.SetStats()
#	c = TCanvas('c', 'c', 3)
#	c.SetLeftMargin(0.15)
#	#gStyle.SetOptStat('e')
#	#c.SetTopMargin(0.15)
#	
#	xframe.GetXaxis().SetTitleSize(0.04)
#	xframe.GetYaxis().SetTitleSize(0.04)
#	xframe.Draw()
#	
#	#gauss.fitTo(data)
#	c.Print(outname)
#
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par1.txt', 'ttbb_Gen_1', 'ttbb_Gen_1_2steps.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par2.txt', 'ttbb_Gen_2', 'ttbb_Gen_2_2steps.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par3.txt', 'ttbb_Gen_3', 'ttbb_Gen_3_2steps.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par4.txt', 'ttbb_Gen_4', 'ttbb_Gen_4_2steps.pdf')
#
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/Pttbb/fitPttbb/par1.txt', 'ttbb_Pttbb', 'ttbb_Pttbb.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/Pttbb/fitPttbb/par2.txt', 'ttbj_Pttbb', 'ttbj_Pttbb.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/Pttbb/fitPttbb/par3.txt', 'Bkg_ttcc+ttLF+ttother_Pttbb', 'Bkg_ttcc+ttLF+ttother_Pttbb.pdf')
#
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/alone/fit/par1.txt', 'ttbb_Gen_1_1stProb', 'ttbb_Gen_1_1stProb.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/alone/fit/par2.txt', 'ttbb_Gen_2_1stProb', 'ttbb_Gen_2_1stProb.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/alone/fit/par3.txt', 'ttbb_Gen_3_1stProb', 'ttbb_Gen_3_1stProb.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/alone/fit/par4.txt', 'ttbb_Gen_4_1stProb', 'ttbb_Gen_4_1stProb.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/alone/fit/par5.txt', 'ttbj_1stProb', 'ttbj_1stProb.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/alone/fit/par6.txt', 'ttcc_1stProb', 'ttcc_1stProb.pdf')
#fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/alone/fit/par7.txt', 'Bkg_ttLF+ttother_1stProb', 'Bkg_ttLF+ttother_1stProb.pdf')
