from ROOT import *
import re
#import pandas as pd
import numpy as np
import time

def getRe(file, title):
	#d = pd.read_fwf(file , header=None)
	#counts = d[0]
#	r_txt = open('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/random/ratio.txt')
	p_txt = open(file)

	h_fit = TH1D(title, title, 40, 0, 2)
	for i in range(0, 998):
#		ratio = round(float(r_txt.readline()),3)
		line = re.split('   |/| ', p_txt.readline())
		par = float(line[4])
#		com_par = round(ratio*par,3)
#		print i, ' ratio ', ratio, 'par ', par, 'com ', com_par

		h_fit.Fill(par)
	h_fit.Fit('gaus')
	gStyle.SetOptFit(kTRUE)

	f_out.Write()
	mean_gauss = h_fit.GetListOfFunctions().FindObject('gaus').GetParameter(1)
	sig_gauss = h_fit.GetListOfFunctions().FindObject('gaus').GetParameter(2)
	#tot = tot+mean_gauss

	#h_fit.Write()
	with open('result_gaus.txt', 'a') as log:
		log.write(title+'\n')
		log.write('mean: '+str(mean_gauss)+'\n')
		log.write('sigma: '+str(sig_gauss)+'\n\n')


f_out = TFile('gausHist.root', 'RECREATE')

inputDir1 = '/home/juhee5819/cheer/T2/combineTool/runCombine/Pttbb/fit/'
inputDir2 = '/home/juhee5819/cheer/T2/combineTool/runCombine/1stProb/fit/'
getRe(inputDir1+'par1.txt', 'ttbb_Pttbb')
getRe(inputDir1+'par2.txt', 'ttbj_Pttbb')
getRe(inputDir1+'par3.txt', 'Bkg_Pttbb')
getRe(inputDir1+'par4.txt', 'TTTo2L2Nu_Pttbb')
getRe(inputDir1+'par5.txt', 'TTToHadronic_Pttbb')
getRe(inputDir1+'par6.txt', 'WJets_Pttbb')

getRe(inputDir2+'par1.txt', 'ttbb_Gen_1')
getRe(inputDir2+'par2.txt', 'ttbb_Gen_2')
getRe(inputDir2+'par3.txt', 'ttbb_Gen_3')
getRe(inputDir2+'par4.txt', 'ttbb_Gen_4')
getRe(inputDir2+'par5.txt', 'ttbj')
getRe(inputDir2+'par6.txt', 'Bkg_ttcc+ttLF+ttother')
getRe(inputDir2+'par7.txt', 'TTTo2L2Nu')
getRe(inputDir2+'par8.txt', 'TTToHadronic')
getRe(inputDir2+'par9.txt', 'WJets')

f_out.Close()

