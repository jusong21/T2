from ROOT import *
from array import array

def rebin(f, hist, hist_name, lastbin, delIdx):
	h = f.Get(hist)

	binEdge = [h.GetBinLowEdge(i) for i in range(1, h.GetNbinsX()+1)]
	binEdge.append(lastbin)

	for idel in sorted(delIdx, reverse=True):
		del binEdge[idel]
		#print idel
		#print binEdge

	h_rebin = h.Rebin(len(binEdge)-1, hist, array('d', binEdge))
	h_rebin.SetName(hist_name)
	h_rebin.SetTitle(hist_name)
	h_rebin.Write()


def mkDel(delList):
	print delList
	temp = delList
	for i in range(1, 4):
		a = [delList[j]+20*i for j in range(len(delList))]
		temp = temp+a
	print temp
	return temp

#del_Pttbb_v1 = [19]
#del_1stProb_v1 = mkDel([1, 2, 3])

#del_Pttbb_v2 = [ 18, 19]
#del_1stProb_v2 = mkDel([1, 2, 3, 4, 5, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19])

del_Pttbb_v3 = [ 13, 14, 15,  17, 18, 19]
del_1stProb_v3 = mkDel([1, 2, 3, 4,  7, 9, 11, 13, 15, 17, 19])

print '\nRebin ttbb'
inputDir = '/home/juhee5819/cheer/T2/combineTool/data/scaled/'
outDir = '/home/juhee5819/cheer/T2/combineTool/data/rebin/'

#f_ttbb = TFile(inputDir+'ttbb.root')
#f_ttbb_out = TFile(outDir+'rebinned_ttbb_v1.root', 'RECREATE')
#rebin(f_ttbb, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v1)
#rebin(f_ttbb, 'h_1stProb_super_Gen_1', 'h_1stProb_Gen_1', 80, del_1stProb_v1)
#rebin(f_ttbb, 'h_1stProb_super_Gen_2', 'h_1stProb_Gen_2', 80, del_1stProb_v1)
#rebin(f_ttbb, 'h_1stProb_super_Gen_3', 'h_1stProb_Gen_3', 80, del_1stProb_v1)
#rebin(f_ttbb, 'h_1stProb_super_Gen_4', 'h_1stProb_Gen_4', 80, del_1stProb_v1)
#f_ttbb_out.Close()
#print 'ttbb done'
#
## ttbj
#print '\nRebin ttbj'
#
#f_ttbj = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/scaled/ttbj.root')
#f_ttbj_out = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_ttbj_v1.root', 'RECREATE')
#rebin(f_ttbj, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v1)
#rebin(f_ttbj, 'h_1stProb_super', 'h_1stProb', 80, del_1stProb_v1)
#f_ttbj_out.Close()
#print 'ttbj done'
#
## Bkg
#print '\nRebin Bkg'
#
#f_Bkg = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/scaled/Bkg_ttcc+ttLF+ttother.root')
#f_Bkg_out = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_Bkg_v1.root', 'RECREATE')
#rebin(f_Bkg, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v1)
#print 'done'
#rebin(f_Bkg, 'h_1stProb_super', 'h_1stProb',  80, del_1stProb_v1)
#f_Bkg_out.Close()
#print 'Bkg done'
#
#
## data
#f_data_Pttbb = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/random/data_Pttbb.root')
#f_data_1stProb = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/random/scaleRatio/data_1stProb.root')
#f_data_out = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_data_v1.root', 'RECREATE')
#for i in range(1, 1001):
#	ihist = 'h_Pttbb_'+str(i)
#	rebin(f_data_Pttbb, ihist, ihist, 1, del_Pttbb_v1)
#
#for i in range(1, 1001):
#	ihist = 'h_1stProb_'+str(i)
#	rebin(f_data_1stProb, ihist, ihist, 80, del_1stProb_v1)
#
#f_data_out.Close()
#	
#
#
#print '\nRebin ttbb'
#
#f_ttbb = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/scaled/ttbb.root')
#f_ttbb_out = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_ttbb_v2.root', 'RECREATE')
#rebin(f_ttbb, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v2)
#rebin(f_ttbb, 'h_1stProb_super_Gen_1', 'h_1stProb_Gen_1', 80, del_1stProb_v2)
#rebin(f_ttbb, 'h_1stProb_super_Gen_2', 'h_1stProb_Gen_2', 80, del_1stProb_v2)
#rebin(f_ttbb, 'h_1stProb_super_Gen_3', 'h_1stProb_Gen_3', 80, del_1stProb_v2)
#rebin(f_ttbb, 'h_1stProb_super_Gen_4', 'h_1stProb_Gen_4', 80, del_1stProb_v2)
#f_ttbb_out.Close()
#print 'ttbb done'
#
## ttbj
#print '\nRebin ttbj'
#
#f_ttbj = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/scaled/ttbj.root')
#f_ttbj_out = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_ttbj_v2.root', 'RECREATE')
#rebin(f_ttbj, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v2)
#rebin(f_ttbj, 'h_1stProb_super', 'h_1stProb', 80, del_1stProb_v2)
#f_ttbj_out.Close()
#print 'ttbj done'
#
## Bkg
#print '\nRebin Bkg'
#
#f_Bkg = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/scaled/Bkg_ttcc+ttLF+ttother.root')
#f_Bkg_out = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_Bkg_v2.root', 'RECREATE')
#rebin(f_Bkg, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v2)
#print 'done'
#rebin(f_Bkg, 'h_1stProb_super', 'h_1stProb',  80, del_1stProb_v2)
#f_Bkg_out.Close()
#print 'Bkg done'
#
#
## data
#f_data_Pttbb = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/random/data_Pttbb.root')
#f_data_1stProb = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/random/scaleRatio/data_1stProb.root')
#f_data_out = TFile('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/rebin/rebinned_data_v2.root', 'RECREATE')
#for i in range(1, 1001):
#	ihist = 'h_Pttbb_'+str(i)
#	rebin(f_data_Pttbb, ihist, ihist, 1, del_Pttbb_v2)
#
#for i in range(1, 1001):
#	ihist = 'h_1stProb_'+str(i)
#	rebin(f_data_1stProb, ihist, ihist, 80, del_1stProb_v2)
#
#f_data_out.Close()
	


print '\nRebin ttbb'

f_ttbb = TFile(inputDir+'ttbb.root')
f_ttbb_out = TFile(outDir+'rebinned_ttbb.root', 'RECREATE')
rebin(f_ttbb, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v3)
rebin(f_ttbb, 'h_1stProb_super_Gen_1', 'h_1stProb_Gen_1', 80, del_1stProb_v3)
rebin(f_ttbb, 'h_1stProb_super_Gen_2', 'h_1stProb_Gen_2', 80, del_1stProb_v3)
rebin(f_ttbb, 'h_1stProb_super_Gen_3', 'h_1stProb_Gen_3', 80, del_1stProb_v3)
rebin(f_ttbb, 'h_1stProb_super_Gen_4', 'h_1stProb_Gen_4', 80, del_1stProb_v3)
f_ttbb_out.Close()
print 'ttbb done'

# ttbj
print '\nRebin ttbj'

f_ttbj = TFile(inputDir+'ttbj.root')
f_ttbj_out = TFile(outDir+'rebinned_ttbj.root', 'RECREATE')
rebin(f_ttbj, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v3)
rebin(f_ttbj, 'h_1stProb_super', 'h_1stProb', 80, del_1stProb_v3)
f_ttbj_out.Close()
print 'ttbj done'

# Bkg
print '\nRebin Bkg'

f_Bkg = TFile(inputDir+'Bkg_ttcc+ttLF+ttother.root')
f_Bkg_out = TFile(outDir+'rebinned_Bkg.root', 'RECREATE')
rebin(f_Bkg, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v3)
print 'done'
rebin(f_Bkg, 'h_1stProb_super', 'h_1stProb',  80, del_1stProb_v3)
f_Bkg_out.Close()
print 'Bkg done'

print '\nRebin TTToHadronic'

f_TTToHadronic = TFile(inputDir+'TTToHadronic.root')
f_TTToHadronic_out = TFile(outDir+'rebinned_TTToHadronic.root', 'RECREATE')
rebin(f_TTToHadronic, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v3)
rebin(f_TTToHadronic, 'h_1stProb_super', 'h_1stProb', 80, del_1stProb_v3)
f_TTToHadronic_out.Close()
print 'TTToHadronic done'

print '\nRebin WJetsToLNu'

f_WJetsToLNu = TFile(inputDir+'WJetsToLNu.root')
f_WJetsToLNu_out = TFile(outDir+'rebinned_WJetsToLNu.root', 'RECREATE')
rebin(f_WJetsToLNu, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v3)
rebin(f_WJetsToLNu, 'h_1stProb_super', 'h_1stProb', 80, del_1stProb_v3)
f_WJetsToLNu_out.Close()
print 'WJetsToLNu done'


print '\nRebin TTTo2L2Nu'

f_TTTo2L2Nu = TFile(inputDir+'TTTo2L2Nu.root')
f_TTTo2L2Nu_out = TFile(outDir+'rebinned_TTTo2L2Nu.root', 'RECREATE')
rebin(f_TTTo2L2Nu, 'h_Pttbb', 'h_Pttbb', 1, del_Pttbb_v3)
rebin(f_TTTo2L2Nu, 'h_1stProb_super', 'h_1stProb', 80, del_1stProb_v3)
f_TTTo2L2Nu_out.Close()
print 'TTTo2L2Nu done'

# data
f_data_Pttbb = TFile(inputDir+'../random/data_Pttbb.root')
f_data_1stProb = TFile(inputDir+'../random/scaleRatio/data_1stProb.root')
f_data_out = TFile(outDir+'rebinned_data.root', 'RECREATE')
for i in range(1, 1001):
	ihist = 'h_Pttbb_'+str(i)
	rebin(f_data_Pttbb, ihist, ihist, 1, del_Pttbb_v3)

for i in range(1, 1001):
	ihist = 'h_1stProb_'+str(i)
	rebin(f_data_1stProb, ihist, ihist, 80, del_1stProb_v3)

f_data_out.Close()
	


