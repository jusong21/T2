import re, os
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import load_model
from keras.utils.np_utils import to_categorical
from ROOT import *
from array import array
import math
from sklearn.metrics import confusion_matrix
import uproot

os.environ["CUDA_VISIBLE_DEVICES"] = "0, 1"

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--y', required=True, default=1000)
parser.add_argument('--p', required=True)
args = parser.parse_args()
year = args.y
process = args.p

############################################
########## Data load & evaluation ##########
############################################

print('Data loading...')
#input_data = '/home/juhee5819/cheer/T2/ntuples/arrays/'+process+'_ULv2_'+str(year)+'.h5'
#data = pd.read_hdf(input_data)
data = uproot.open('/home/juhee5819/cheer/T2/ntuples/rootfiles/'+process+'_ULv2_'+str(year)+'.root')['tree'].arrays(library='pd')

print('Data processing...')
#event_var = ['nbjets_m', 'ncjets_m', 'ngoodjets', 'Ht', 'lepton_pt', 'lepton_eta', 'lepton_phi', 'lepton_m', 'MET_pt', 'MET_phi', "dEta12", "dEta13", "dEta14", "dEta23", "dEta24", "dEta34", "dPhi12", "dPhi13", "dPhi14", "dPhi23", "dPhi24", "dPhi34", "invm12", "invm13", "invm14", "invm23", "invm24", "invm34", "dRnulep12", "dRnulep13", "dRnulep14", "dRnulep23", "dRnulep24", "dRnulep34"]
event_var = ['nbjets_m', 'ncjets_m', 'ngoodjets', 'Ht', 'lepton_pt', 'lepton_eta', 'lepton_phi', 'lepton_m', "dEta12", "dEta13", "dEta14", "dEta23", "dEta24", "dEta34", "dPhi12", "dPhi13", "dPhi14", "dPhi23", "dPhi24", "dPhi34", "invm12", "invm13", "invm14", "invm23", "invm24", "invm34", "dRnulep12", "dRnulep13", "dRnulep14", "dRnulep23", "dRnulep24", "dRnulep34"]
#jet_var = ["jet1_pt", "jet1_eta", "jet1_m", "jet1_btag", "jet1_cvsl", "dRlep1", "dRnu1", "invmlep1", "jet2_pt", "jet2_eta", "jet2_m", "jet2_btag", "jet2_cvsl", "dRlep2", "dRnu2", "invmlep2", "jet3_pt", "jet3_eta", "jet3_m", "jet3_btag", "jet3_cvsl", "dRlep3", "dRnu3", "invmlep3", "jet4_pt", "jet4_eta", "jet4_m", "jet4_btag", "jet4_cvsl", "dRlep4", "dRnu4", "invmlep4"]
jet_var = ["jet1_pt", "jet1_eta", "jet1_btag", "jet1_cvsl", "dRlep1", "invmlep1", "jet2_pt", "jet2_eta", "jet2_btag", "jet2_cvsl", "dRlep2", "invmlep2", "jet3_pt", "jet3_eta", "jet3_btag", "jet3_cvsl", "dRlep3", "invmlep3", "jet4_pt", "jet4_eta", "jet4_btag", "jet4_cvsl", "dRlep4", "invmlep4"]

# split data
def process_full():
	# event info	
	full_event_input = data.filter( items=event_var )
	full_event_input = np.array( full_event_input )
	full_event_out = data.filter( items=['event_category'] )
	full_event_out = to_categorical( full_event_out )
	# jet info
	full_jet_input = data.filter( items=jet_var )
	full_jet_input = np.array( full_jet_input )
	full_jet_input = full_jet_input.reshape( full_jet_input.shape[0], 4, -1 )
	full_jet_out = data.filter( items=['jet_perm'] )
	full_jet_out = to_categorical( full_jet_out )
	return full_event_input, full_event_out, full_jet_input, full_jet_out

def evaluation(model_path, best_weights):
	# load model and weights
	model = tf.keras.models.load_model( model_path )
	model.load_weights( best_weights )
	prediction = model.predict( [full_event_input, full_jet_input] )
	return prediction

full_event_input, full_event_out,full_jet_input, full_jet_out = process_full()

print('Evaluating...')
# jet eval
weights_jet = '/home/juhee5819/cheer/T2/train/results/jet/try1/best_model.h5'
model_jet = '/home/juhee5819/cheer/T2/train/models/jet_model'
predict_jet = evaluation(model_jet, weights_jet)
pred_jet = np.argmax(predict_jet, axis=1)
real_jet = np.argmax(full_jet_out, axis=1)
predict_jet.sort()
data['pred_jet'] = pred_jet
data['prob1'] = predict_jet[:,-1]

#event eval
weights_event = '/home/juhee5819/cheer/T2/train/results/event/try1/best_model.h5'
model_event = '/home/juhee5819/cheer/T2/train/models/event_model'
predict_event = evaluation(model_event, weights_event)
pred_event = np.argmax(predict_event, axis=1)
real_event = np.argmax(full_event_out, axis=1)
data['pred_event'] = pred_event
data['pttbb'] = predict_event[:,0]

# reco
def getReco(r0, r1, r2, r3, r4, r5, pred):
	arr = [r0, r1, r2, r3, r4, r5]
	return arr[pred]

data['reco_dRbb'] = data.apply(lambda row: getReco(row.dR12, row.dR13, row.dR14, row.dR23, row.dR24, row.dR34, int(row.pred_jet)), axis=1)
data['reco_mbb'] = data.apply(lambda row: getReco(row.invm12, row.invm13, row.invm14, row.invm23, row.invm24, row.invm34, int(row.pred_jet)), axis=1)

############################################
############# Save histograms ##############
############################################

print('Saving histograms...')
outfilename = 'hist_'+process+'_'+str(year)+'.root'
outfile = TFile.Open(outfilename, 'RECREATE')

def find_bins( xmin, xmax, binwidth ):
    n = int( (xmax-xmin) / binwidth ) + 1 
    bins = np.linspace( xmin, xmax, n ) 
    return bins

def histTH1D(h_name, xbins, xtitle, ytitle):
	h = TH1D(h_name, '', len(xbins)-1, array('d', xbins))
	h.SetXTitle(xtitle)
	h.SetYTitle(ytitle)
	h.Sumw2()
	return h

def histTH2D(h_name, xbins, ybins, xtitle, ytitle):
	h = TH2D(h_name, '', len(xbins)-1, array('d', xbins), len(ybins)-1, array('d', ybins))
	h.SetXTitle(xtitle)
	h.SetYTitle(ytitle)
	h.Sumw2()
	return h

def histTH3D(h_name, xbins, ybins, zbins, xtitle, ytitle, ztitle):
	h = TH3D(h_name, '', len(xbins)-1, array('d', xbins), len(ybins)-1, array('d', ybins), len(zbins)-1, array('d', zbins))
	h.SetXTitle(xtitle)
	h.SetYTitle(ytitle)
	h.SetZTitle(ztitle)
	h.Sumw2()
	return h

def overflow1D(h):
	nbins = h.GetNbinsX()
	# underflow
	firstCon = h.GetBinContent(1)
	underCon = h.GetBinContent(-1)
	h.SetBinContent(1, firstCon+underCon)
	# overflow
	lastCon = h.GetBinContent(nbins)
	overCon = h.GetBinContent(nbins+1)
	h.SetBinContent(nbins, lastCon+overCon)

def overflow2D(h):
	nxbins = h.GetNbinsX()
	nybins = h.GetNbinsY()
	# overflow
	for xbin in range(1, nxbins+1):
		lastCon = h.GetBinContent(xbin, nybins)
		overCon = h.GetBinContent(xbin, nybins+1)
		h.SetBinContent(xbin, nybins, lastCon+overCon)
	for ybin in range(1, nybins+1):
		lastCon = h.GetBinContent(nxbins, ybin)
		overCon = h.GetBinContent(nxbins+1, ybin)
		h.SetBinContent(nxbins, ybin, lastCon+overCon)
	lastCon = h.GetBinContent(nxbins, nybins)
	overCon = h.GetBinContent(nxbins+1, nybins+1)
	h.SetBinContent(nxbins, nybins, lastCon+overCon)
	
	# underflow
	for xbin in range(1, nxbins+1):
		firstCon = h.GetBinContent(xbin, 1)
		underCon = h.GetBinContent(xbin, -1)
		h.SetBinContent(xbin, 1, firstCon+underCon)
	for ybin in range(1, nybins+1):
		firstCon = h.GetBinContent(1, ybin)
		underCon = h.GetBinContent(-1, ybin)
		h.SetBinContent(1, ybin, firstCon+underCon)
	firstCon = h.GetBinContent(1, 1)
	underCon = h.GetBinContent(-1, -1)
	h.SetBinContent(1, 1, firstCon+underCon)
	
def overflow3D(h):
	nxbins = h.GetNbinsX()
	nybins = h.GetNbinsY()
	nzbins = h.GetNbinsZ()
	# overflow
	# x
	for ybin in range(1, nybins+1):
		lastCon = h.GetBinContent(nxbins, ybin, nzbins)
		overCon = h.GetBinContent(nxbins+1, ybin, nzbins+1)
		h.SetBinContent(nxbins, ybin, nzbins, lastCon+overCon)
		for zbin in range(1, nzbins+1):
			lastCon = h.GetBinContent(nxbins, ybin, zbin)
			overCon = h.GetBinContent(nxbins+1, ybin, zbin)
			h.SetBinContent(nxbins, ybin, zbin, lastCon+overCon)
	# y
	for zbin in range(1, nzbins+1):
		lastCon = h.GetBinContent(nxbins, nybins, zbin)
		overCon = h.GetBinContent(nxbins+1, nybins+1, zbin)
		h.SetBinContent(nxbins, nybins, zbin, lastCon+overCon)
		for xbin in range(1, nxbins+1):
			lastCon = h.GetBinContent(xbin, nybins, zbin)
			overCon = h.GetBinContent(xbin, nybins+1, zbin)
			h.SetBinContent(xbin, nybins, zbin, lastCon+overCon)
	lastCon = h.GetBinContent(nxbins, nybins, nzbins)
	overCon = h.GetBinContent(nxbins+1, nybins+1, nzbins+1)
	h.SetBinContent(nxbins+1, nybins+1, nzbins+1, lastCon+overCon)
	# underflow
	# x
	for ybin in range(1, nybins+1):
		firstCon = h.GetBinContent(1, ybin, 1)
		underCon = h.GetBinContent(-1, ybin, -1)
		h.SetBinContent(1, ybin, 1, firstCon+underCon)
		for zbin in range(1, nzbins+1):
			firstCon = h.GetBinContent(1, ybin, zbin)
			underCon = h.GetBinContent(-1, ybin, zbin)
			h.SetBinContent(1, ybin, zbin, firstCon+underCon)
	# y
	for zbin in range(1, nzbins+1):
		firstCon = h.GetBinContent(1, 1, zbin)
		underCon = h.GetBinContent(-1, -1, zbin)
		h.SetBinContent(1, 1, zbin, firstCon+underCon)
		for xbin in range(1, nxbins+1):
			firstCon = h.GetBinContent(xbin, 1, zbin)
			underCon = h.GetBinContent(xbin, -1, zbin)
			h.SetBinContent(xbin, 1, zbin, firstCon+underCon)
	firstCon = h.GetBinContent(1, 1, 1)
	underCon = h.GetBinContent(-1, -1, -1)
	h.SetBinContent(1, 1, 1, firstCon+underCon)

def getEntries1D(h):
	nbins = h.GetNbinsX()
	entries = 0
	for bin in range(1, nbins+1):
		entries += h.GetBinContent(bin)
	return entries

def getEntries2D(h):
	nxbins = h.GetNbinsX()
	nybins = h.GetNbinsY()
	entries = 0
	for xbin in range(1, nxbins+1):
		for ybin in range(1, nybins+1):
			entries += h.GetBinContent(xbin, ybin)
	return entries

def getEntries3D(h):
	nxbins = h.GetNbinsX()
	nybins = h.GetNbinsY()
	nzbins = h.GetNbinsZ()
	entries = 0
	for xbin in range(1, nxbins+1):
		for ybin in range(1, nybins+1):
			for zbin in range(1, nzbins+1):
				entries += h.GetBinContent(xbin, ybin, zbin)
	return entries

dRbins = [0.4, 0.6, 1.0, 2.0, 4.0]
mbins = [0.0, 60.0, 100.0, 170.0, 400.0]
pbins = find_bins(0, 1, 0.05)

h_mbb = histTH1D('h_mbb', mbins, 'Reco. m_{b#bar{b}}(GeV)', 'Entries')
h_dRbb = histTH1D('h_dRbb', dRbins, 'Reco. #DeltaR_{b#bar{b}}', 'Entries')
h_1stProb = histTH1D('h_1stProb', pbins, 'The highest probability', 'Entries')
h_Pttbb = histTH1D('h_Pttbb', pbins, 'Probability to be ttbb', 'Entries')

h_mbb_1stProb = histTH2D('h_mbb_1stProb', mbins, pbins, 'Reco. m_{b#bar{b}}(GeV)', 'The highest probability')
h_dRbb_1stProb = histTH2D('h_dRbb_1stProb', dRbins, pbins, 'Reco. #DeltaR_{b#bar{b}}', 'The highest probability')
h_mbb_Pttbb = histTH2D('h_mbb_Pttbb', mbins, pbins, 'Reco. m_{b#bar{b}}(GeV)', 'Probability to be ttbb')
h_dRbb_Pttbb = histTH2D('h_dRbb_Pttbb', dRbins, pbins, 'Reco. #DeltaR_{b#bar{b}}', 'Probability to be ttbb')

if process=='ttbb':

	h_gen_mbb = histTH1D('h_gen_mbb', mbins, 'Gen. m_{b#bar{b}}(GeV)', 'Entries')
	h_gen_dRbb = histTH1D('h_gen_dRbb', dRbins, 'Gen. #DeltaR_{b#bar{b}}', 'Entries')
	h_responseMatrix_mbb = histTH2D('h_responseMatrix_mbb', mbins, mbins, 'Reco. m_{b#bar{b}}(GeV)', 'Gen. m_{b#bar{b}}(GeV)')
	h_responseMatrix_dRbb = histTH2D('h_responseMatrix_dRbb', dRbins, dRbins, 'Reco. #DeltaR_{b#bar{b}}', 'Gen. #DeltaR_{b#bar{b}}')
	h_responseMatrix_mbb_1stProb = histTH3D('h_responseMatrix_mbb_1stProb', mbins, mbins, pbins, 'Reco. m_{b#bar{b}}(GeV)', 'Gen. m_{b#bar{b}}(GeV)', 'The highest probability')
	h_responseMatrix_dRbb_1stProb = histTH3D('h_responseMatrix_dRbb_1stProb', dRbins, dRbins, pbins, 'Reco. #DeltaR_{b#bar{b}}', 'Gen. #DeltaR_{b#bar{b}}', 'The highest probability')
	h_responseMatrix_mbb_Pttbb = histTH3D('h_responseMatrix_mbb_Pttbb', mbins, mbins, pbins, 'Reco. m_{b#bar{b}}(GeV)', 'Gen. m_{b#bar{b}}(GeV)', 'Probability to be ttbb')
	h_responseMatrix_dRbb_Pttbb = histTH3D('h_responseMatrix_dRbb_Pttbb', dRbins, dRbins, pbins, 'Reco. #DeltaR_{b#bar{b}}', 'Gen. #DeltaR_{b#bar{b}}', 'Probability to be ttbb')

for index, event in data.iterrows():
	real = event['jet_perm']
	pred = event['pred_jet']
	reco_mbb = event['reco_mbb']
	reco_dRbb = event['reco_dRbb']
	prob1 = event['prob1']
	Pttbb = event['pttbb']

	h_mbb.Fill(reco_mbb)
	h_dRbb.Fill(reco_dRbb)
	h_1stProb.Fill(prob1)
	h_Pttbb.Fill(Pttbb)
	h_mbb_1stProb.Fill(reco_mbb, prob1)
	h_dRbb_1stProb.Fill(reco_dRbb, prob1)
	h_mbb_Pttbb.Fill(reco_mbb, Pttbb)
	h_dRbb_Pttbb.Fill(reco_dRbb, Pttbb)

	if process=='ttbb':
		gen_mbb = event['gen_mbb']
		gen_dRbb = event['gen_dRbb']

		h_gen_mbb.Fill(gen_mbb)
		h_gen_dRbb.Fill(gen_dRbb)
		h_responseMatrix_mbb.Fill(reco_mbb, gen_mbb)
		h_responseMatrix_dRbb.Fill(reco_dRbb, gen_dRbb)
		h_responseMatrix_mbb_1stProb.Fill(reco_mbb, gen_mbb, prob1)
		h_responseMatrix_dRbb_1stProb.Fill(reco_dRbb, gen_dRbb, prob1)
		h_responseMatrix_mbb_Pttbb.Fill(reco_mbb, gen_mbb, Pttbb)
		h_responseMatrix_dRbb_Pttbb.Fill(reco_dRbb, gen_dRbb, Pttbb)

# overflow and set entries
overflow1D(h_mbb)
overflow1D(h_dRbb)
overflow1D(h_1stProb)
overflow1D(h_Pttbb)
overflow2D(h_mbb_1stProb)
overflow2D(h_dRbb_1stProb)
overflow2D(h_mbb_Pttbb)
overflow2D(h_dRbb_Pttbb)

h_mbb.SetEntries(getEntries1D(h_mbb))
h_dRbb.SetEntries(getEntries1D(h_dRbb))
h_1stProb.SetEntries(getEntries1D(h_1stProb))
h_Pttbb.SetEntries(getEntries1D(h_Pttbb))
h_mbb_1stProb.SetEntries(getEntries2D(h_mbb_1stProb))
h_dRbb_1stProb.SetEntries(getEntries2D(h_dRbb_1stProb))
h_mbb_Pttbb.SetEntries(getEntries2D(h_mbb_Pttbb))
h_dRbb_Pttbb.SetEntries(getEntries2D(h_dRbb_Pttbb))

if process=='ttbb':
	overflow1D(h_gen_mbb)
	overflow1D(h_gen_dRbb)
	overflow2D(h_responseMatrix_mbb)
	overflow2D(h_responseMatrix_dRbb)
	overflow3D(h_responseMatrix_mbb_1stProb)
	overflow3D(h_responseMatrix_dRbb_1stProb)
	overflow3D(h_responseMatrix_mbb_Pttbb)
	overflow3D(h_responseMatrix_dRbb_Pttbb)

	h_gen_mbb.SetEntries(getEntries1D(h_gen_mbb))
	h_gen_dRbb.SetEntries(getEntries1D(h_gen_dRbb))
	h_responseMatrix_mbb.SetEntries(getEntries2D(h_responseMatrix_mbb))
	h_responseMatrix_dRbb.SetEntries(getEntries2D(h_responseMatrix_dRbb))
	h_responseMatrix_mbb_1stProb.SetEntries(getEntries3D(h_responseMatrix_mbb_1stProb))
	h_responseMatrix_dRbb_1stProb.SetEntries(getEntries3D(h_responseMatrix_dRbb_1stProb))
	h_responseMatrix_mbb_Pttbb.SetEntries(getEntries3D(h_responseMatrix_mbb_Pttbb))
	h_responseMatrix_dRbb_Pttbb.SetEntries(getEntries3D(h_responseMatrix_dRbb_Pttbb))

	# 
	h_Pttbb_Gen_1 = h_responseMatrix_dRbb_Pttbb.ProjectionZ('h_Pttbb_Gen_1', 1, 4, 1, 1)
	h_Pttbb_Gen_2 = h_responseMatrix_dRbb_Pttbb.ProjectionZ('h_Pttbb_Gen_2', 1, 4, 2, 2)
	h_Pttbb_Gen_3 = h_responseMatrix_dRbb_Pttbb.ProjectionZ('h_Pttbb_Gen_3', 1, 4, 3, 3)
	h_Pttbb_Gen_4 = h_responseMatrix_dRbb_Pttbb.ProjectionZ('h_Pttbb_Gen_4', 1, 4, 4, 4)

	h_1stProb_Gen_1_Reco_1 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_1_Reco_1', 1, 1, 1, 1)
	h_1stProb_Gen_1_Reco_2 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_1_Reco_2', 2, 2, 1, 1)
	h_1stProb_Gen_1_Reco_3 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_1_Reco_3', 3, 3, 1, 1)
	h_1stProb_Gen_1_Reco_4 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_1_Reco_4', 4, 4, 1, 1)

	h_1stProb_Gen_2_Reco_1 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_2_Reco_1', 1, 1, 2, 2)
	h_1stProb_Gen_2_Reco_2 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_2_Reco_2', 2, 2, 2, 2)
	h_1stProb_Gen_2_Reco_3 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_2_Reco_3', 3, 3, 2, 2)
	h_1stProb_Gen_2_Reco_4 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_2_Reco_4', 4, 4, 2, 2)

	h_1stProb_Gen_3_Reco_1 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_3_Reco_1', 1, 1, 3, 3)
	h_1stProb_Gen_3_Reco_2 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_3_Reco_2', 2, 2, 3, 3)
	h_1stProb_Gen_3_Reco_3 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_3_Reco_3', 3, 3, 3, 3)
	h_1stProb_Gen_3_Reco_4 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_3_Reco_4', 4, 4, 3, 3)

	h_1stProb_Gen_4_Reco_1 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_4_Reco_1', 1, 1, 4, 4)
	h_1stProb_Gen_4_Reco_2 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_4_Reco_2', 2, 2, 4, 4)
	h_1stProb_Gen_4_Reco_3 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_4_Reco_3', 3, 3, 4, 4)
	h_1stProb_Gen_4_Reco_4 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_4_Reco_4', 4, 4, 4, 4)

	h_1stProb_Gen_1 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_1', 1, 4, 1, 1)
	h_1stProb_Gen_2 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_2', 1, 4, 2, 2)
	h_1stProb_Gen_3 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_3', 1, 4, 3, 3)
	h_1stProb_Gen_4 = h_responseMatrix_dRbb_1stProb.ProjectionZ('h_1stProb_Gen_4', 1, 4, 4, 4)

outfile.Write()
outfile.Close()
print('Saved')

