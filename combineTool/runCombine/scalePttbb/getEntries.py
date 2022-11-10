from ROOT import *

target = ['ttbb', 'ttbj', 'ttcc', 'Bkg']

for i in range(0, len(target)):
	f = TFile('scaled_'+target[i]+'.root')

	if target[i]=='ttbb':
		for igen in range(1, 5):
			h = f.Get('h_1stProb_Gen_'+str(igen))
			tot = 0
			for bin in range(1, h.GetNbinsX()+1):
				tot = tot + h.GetBinContent(bin)
			print target[i],' gen', igen, ' ', tot
	
	else:
		h = f.Get('h_1stProb')
		tot = 0
		for bin in range(1, h.GetNbinsX()+1):
			tot = tot + h.GetBinContent(bin)
		print target[i], ' ', tot
			


