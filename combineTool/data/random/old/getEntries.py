from ROOT import *

def getE(file, hist):
	f = TFile(file)
	h = f.Get(hist)
	
	tot = 0
	for i in range(1, h.GetNbinsX()+1):
		#print h.GetBinContent(i)
		tot = tot + h.GetBinContent(i)
	
	print "tot ",tot
	return tot


getE("data_Pttbb.root", 'h_Pttbb_1')
getE("data_Pttbb.root", 'h_Pttbb_2')
getE("data_Pttbb.root", 'h_Pttbb_3')
getE("scaleRatio/data_1stProb.root", 'h_1stProb_1')
getE("scaleRatio/data_1stProb.root", 'h_1stProb_2')
getE("scaleRatio/data_1stProb.root", 'h_1stProb_3')


#getE('random_ttbb.root', 'h_1stProb_2')
#getE('random_ttbb.root', 'h_1stProb_3')
#getE('random_ttbb.root', 'h_1stProb_4')
#getE('random_ttbj.root', 'h_Pttbb_2')
#getE('scaleRatio/scale_ttbj.root', 'h_1stProb_2')
#
#getE('random_ttbj.root', 'h_Pttbb_3')
#getE('scaleRatio/scale_ttbj.root', 'h_1stProb_3')
#
#getE('random_ttbj.root', 'h_Pttbb_4')
#getE('scaleRatio/scale_ttbj.root', 'h_1stProb_4')

for i in range(1, 1001):
	n1 = getE('data_Pttbb.root', 'h_Pttbb_'+str(i))
	n2 = getE('scaleRatio/data_1stProb.root', 'h_1stProb_'+str(i))

	r = round(n1/n2, 4)

	if r != 1.0:
		print i, ' ', n1, ' ', n2, ' ', r


