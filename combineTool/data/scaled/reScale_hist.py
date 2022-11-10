import ROOT
from ROOT import *
from array import array
import os,sys
import time

#switch = 1
#switch = 0 # mc
#switch = 1 # ttbb

#if switch == 0: inputDir = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/dnn_hist/'
#elif switch == 1: inputDir = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/dnn_hist/'
#ntupleDir = '/data1/common/skimmed_NanoAOD/ttbb_ntuple_v3/2018/'

#inputDir = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/dnn_hist/'
inputDir = '/home/juhee5819/cheer/T2/combineTool/data/dnn_hist/'
ntupleDir = '/data/users/juhee5819/ntuple/nanoaod/ttbb_ntuple_ULv2/2018/'
#ntupleDir = '/data1/common/skimmed_NanoAOD/ttbb_ntuple_ULv2/2018/'
#saveLoc = '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/'
saveLoc = '/home/juhee5819/cheer/T2/combineTool/data/scaled/'

lumi18 = 59741
#lumi18 = 59741 nano 59352 mini
lumi17 = 41529
lumi16 = 35922

lumi = lumi18

#def reScale(process, nevt,i):
def reScale(process, nevt):

	Scaler = -1
	xsec = -1

	#### TTbar ####
	if "TTToSemiLeptonic" in process: xsec = 365.34
	elif "TTTo2L2Nu" in process: xsec = 88.29
	elif "TTToHadronic" in process: xsec = 377.96

	#### SingleTop ####
	elif "ST_s-" in process: xsec = 3.36
	elif "ST_t-channel_top" in process: xsec = 136.02
	elif "ST_t-channel_antitop" in process: xsec = 80.95
	elif "ST_tW_top" in process: xsec = 35.85
	elif "ST_tW_antitop" in process: xsec = 35.85

	#### W+Jet ####
	#elif "W1Jet" in process: xsec = 9625
	#elif "W2Jet" in process: xsec = 2793
	#elif "W3Jet" in process: xsec = 992.5
	#elif "W4Jet" in process: xsec = 544.3
	elif "WJet" in process: xsec = 13954.8

	### VV ###
	elif "WWTo2L2Nu" in process: xsec = 12.178
	elif "WWToLNuQQ" in process: xsec = 49.997
	elif "WZTo2L2Q" in process:  xsec = 5.595
	elif "WZTo3LNu" in process: xsec = 4.42965
	elif "ZZTo2L2Q" in process: xsec = 3.22

	### Z+Jets ### 
	elif "DYJetsToLL_M-10to50" in process: xsec = 18610.0
	elif "DYJetsToLL_M-50" in process: xsec = 6077.22

	### ttH ###
	elif "ttHToNonbb" in process: xsec = 0.2151
	elif "ttHTobb" in process: xsec = 0.2934

	### ttX ###
	elif "TTWJetsToLNu" in process: xsec = 0.2043
	elif "TTWJetsToQQ" in process: xsec = 0.4062
	elif "TTZToLLNuNu_M-10" in process: xsec = 0.2529
	elif "TTZToQQ_TuneCP5" in process: xsec = 0.5297

	else:
		print("RAISE "+str(process))
		sys.exit()

	Scaler = xsec * lumi / nevt
	print("\nsample: "+str(process))
	print("nevt "+str(nevt))
	print("xsec "+str(xsec)+"\n")

	#f = TFile.Open(inputDir+"hist_array_dnn_"+process+"_Ch"+str(i)+".root")
	f = TFile.Open(inputDir+"hist_"+process+"_2018.root")

	h_mbb = f.Get('h_mbb')
	h_dRbb = f.Get('h_dRbb')
	h_1stProb = f.Get('h_1stProb')
	h_Pttbb = f.Get('h_Pttbb')

	h_mbb_1stProb = f.Get('h_mbb_1stProb')
	h_dRbb_1stProb = f.Get('h_dRbb_1stProb')
	h_mbb_Pttbb = f.Get('h_mbb_Pttbb')
	h_dRbb_Pttbb = f.Get('h_dRbb_Pttbb')
	
	h_mbb.Scale(Scaler)
	h_dRbb.Scale(Scaler)
	h_1stProb.Scale(Scaler)
	h_Pttbb.Scale(Scaler)

	h_mbb_1stProb.Scale(Scaler)
	h_dRbb_1stProb.Scale(Scaler)
	h_mbb_Pttbb.Scale(Scaler)
	h_dRbb_Pttbb.Scale(Scaler)

#	nf = TFile.Open(saveLoc+'scaled_'+process+"_Ch"+str(i)+".root", 'RECREATE')
	if 'TTToSemiLeptonic' in process:
		proc = process.split('_')[1]
	else:
		proc = process.split('.')[0]
	nf = TFile.Open(saveLoc+proc+".root", 'RECREATE')

	h_mbb.Write()   
	h_dRbb.Write()
	h_1stProb.Write()
	h_Pttbb.Write()

	h_mbb_1stProb.Write()
	h_dRbb_1stProb.Write()
	h_mbb_Pttbb.Write()
	h_dRbb_Pttbb.Write()

	if "ttbb" in process:
		print ("ttbb is here")
		print (Scaler)

		h_Pttbb_Gen_1 = f.Get('h_Pttbb_Gen_1')
		h_Pttbb_Gen_2 = f.Get('h_Pttbb_Gen_2')
		h_Pttbb_Gen_3 = f.Get('h_Pttbb_Gen_3')
		h_Pttbb_Gen_4 = f.Get('h_Pttbb_Gen_4')
		h_1stProb_Gen_1_Reco_1 = f.Get('h_1stProb_Gen_1_Reco_1')
		h_1stProb_Gen_1_Reco_2 = f.Get('h_1stProb_Gen_1_Reco_2')
		h_1stProb_Gen_1_Reco_3 = f.Get('h_1stProb_Gen_1_Reco_3')
		h_1stProb_Gen_1_Reco_4 = f.Get('h_1stProb_Gen_1_Reco_4')
		h_1stProb_Gen_2_Reco_1 = f.Get('h_1stProb_Gen_2_Reco_1')
		h_1stProb_Gen_2_Reco_2 = f.Get('h_1stProb_Gen_2_Reco_2')
		h_1stProb_Gen_2_Reco_3 = f.Get('h_1stProb_Gen_2_Reco_3')
		h_1stProb_Gen_2_Reco_4 = f.Get('h_1stProb_Gen_2_Reco_4')
		h_1stProb_Gen_3_Reco_1 = f.Get('h_1stProb_Gen_3_Reco_1')
		h_1stProb_Gen_3_Reco_2 = f.Get('h_1stProb_Gen_3_Reco_2')
		h_1stProb_Gen_3_Reco_3 = f.Get('h_1stProb_Gen_3_Reco_3')
		h_1stProb_Gen_3_Reco_4 = f.Get('h_1stProb_Gen_3_Reco_4')
		h_1stProb_Gen_4_Reco_1 = f.Get('h_1stProb_Gen_4_Reco_1')
		h_1stProb_Gen_4_Reco_2 = f.Get('h_1stProb_Gen_4_Reco_2')
		h_1stProb_Gen_4_Reco_3 = f.Get('h_1stProb_Gen_4_Reco_3')
		h_1stProb_Gen_4_Reco_4 = f.Get('h_1stProb_Gen_4_Reco_4')
		
		h_Pttbb_Gen_1.Scale(Scaler)
		h_Pttbb_Gen_2.Scale(Scaler)
		h_Pttbb_Gen_3.Scale(Scaler)
		h_Pttbb_Gen_4.Scale(Scaler)
		h_1stProb_Gen_1_Reco_1.Scale(Scaler)
		h_1stProb_Gen_1_Reco_2.Scale(Scaler)
		h_1stProb_Gen_1_Reco_3.Scale(Scaler)
		h_1stProb_Gen_1_Reco_4.Scale(Scaler)
		h_1stProb_Gen_2_Reco_1.Scale(Scaler)
		h_1stProb_Gen_2_Reco_2.Scale(Scaler)
		h_1stProb_Gen_2_Reco_3.Scale(Scaler)
		h_1stProb_Gen_2_Reco_4.Scale(Scaler)
		h_1stProb_Gen_3_Reco_1.Scale(Scaler)
		h_1stProb_Gen_3_Reco_2.Scale(Scaler)
		h_1stProb_Gen_3_Reco_3.Scale(Scaler)
		h_1stProb_Gen_3_Reco_4.Scale(Scaler)
		h_1stProb_Gen_4_Reco_1.Scale(Scaler)
		h_1stProb_Gen_4_Reco_2.Scale(Scaler)
		h_1stProb_Gen_4_Reco_3.Scale(Scaler)
		h_1stProb_Gen_4_Reco_4.Scale(Scaler)

		h_Pttbb_Gen_1.Write()
		h_Pttbb_Gen_2.Write()
		h_Pttbb_Gen_3.Write()
		h_Pttbb_Gen_4.Write()
		h_1stProb_Gen_1_Reco_1.Write()
		h_1stProb_Gen_1_Reco_2.Write()
		h_1stProb_Gen_1_Reco_3.Write()
		h_1stProb_Gen_1_Reco_4.Write()
		h_1stProb_Gen_2_Reco_1.Write()
		h_1stProb_Gen_2_Reco_2.Write()
		h_1stProb_Gen_2_Reco_3.Write()
		h_1stProb_Gen_2_Reco_4.Write()
		h_1stProb_Gen_3_Reco_1.Write()
		h_1stProb_Gen_3_Reco_2.Write()
		h_1stProb_Gen_3_Reco_3.Write()
		h_1stProb_Gen_3_Reco_4.Write()
		h_1stProb_Gen_4_Reco_1.Write()
		h_1stProb_Gen_4_Reco_2.Write()
		h_1stProb_Gen_4_Reco_3.Write()
		h_1stProb_Gen_4_Reco_4.Write()

#		h_gen_mbb = f.Get('h_gen_mbb')
#		h_gen_dRbb = f.Get('h_gen_dRbb')
#		h_responseMatrix_mbb = f.Get('h_responseMatrix_mbb')
#		h_responseMatrix_dRbb = f.Get('h_responseMatrix_dRbb')
#	
#		h_responseMatrix_mbb_1stProb = f.Get('h_responseMatrix_mbb_1stProb')
#		h_responseMatrix_dRbb_1stProb = f.Get('h_responseMatrix_dRbb_1stProb')
#		h_responseMatrix_mbb_Pttbb = f.Get('h_responseMatrix_mbb_Pttbb')
#		h_responseMatrix_dRbb_Pttbb = f.Get('h_responseMatrix_dRbb_Pttbb')
#	
#		h_gen_mbb.Scale(Scaler)
#		h_gen_dRbb.Scale(Scaler)
#		h_responseMatrix_mbb.Scale(Scaler)
#		h_responseMatrix_dRbb.Scale(Scaler)
#	
#		h_responseMatrix_mbb_1stProb.Scale(Scaler)
#		h_responseMatrix_dRbb_1stProb.Scale(Scaler)
#		h_responseMatrix_mbb_Pttbb.Scale(Scaler)
#		h_responseMatrix_dRbb_Pttbb.Scale(Scaler)
#	
#		h_gen_mbb.Write()
#		h_gen_dRbb.Write()
#		h_responseMatrix_mbb.Write()
#		h_responseMatrix_dRbb.Write()
#	
#		h_responseMatrix_mbb_1stProb.Write()
#		h_responseMatrix_dRbb_1stProb.Write()
#		h_responseMatrix_mbb_Pttbb.Write()
#		h_responseMatrix_dRbb_Pttbb.Write()
 
	nf.Close()
	
def merge(inputDir, process):
	f = TFile.Open(inputDir+process)
	hist = f.Get('hcounter1_nocut')
	h_merge.Add(hist)

start_time = time.time()
print("Start processing")

for target in os.listdir(ntupleDir):

#	if switch == 0 :
#		if "EGamma" in target or "Single" in target: continue
#		elif "ttbb" in target: continue
#	if switch == 1 : 
#		if not "ttbb" in target: continue
#		if "gen" in target or "4f" in target: continue

	if "EGamma" in target or "Single" in target: continue
	if "ttH" in target or "ST" in target or "DY" in target: continue
	if "TTZ" in target or "TTW" in target or "WW" in target or "WZ" in target or "ZZ" in target: continue
	if "donepre" in target or "data" in target or "cd" in target: continue

	h_merge = TH1D('h_merge','Event counter',2,-0.5,1.5)

	#for process in os.listdir(ntupleDir+target):
	#	merge(ntupleDir+target+"/", process)

	#if "TTToSemi" in target: nevt = 298744402.0 #2018 only!
	#if not 'TTToSemi' in target: continue
	if "TTToSemi" in target: nevt = 468182000.0 #2018 only!
	else:
		f = TFile.Open(ntupleDir+target)
		hist = f.Get('hcounter1_nocut')
		nevt = hist.Integral()

	#for i in range(0,2):
	#  reScale(target,nevt,i)
	process = target.split('.')[0] 
	reScale(process,nevt)

print("Done! Total running time :%s " %(time.time() - start_time))

