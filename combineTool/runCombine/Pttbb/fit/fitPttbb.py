from ROOT import *

#f = TFile.Open('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/scaled/split_ttbb.root', 'READ')
#f_out = TFile.Open('ttbb_fitPttbb.root', 'RECREATE')
#param = open('par1.txt', 'r')
#param_list = param.readlines()
#param_list = map(float, param_list)
#
##print( param_list )
#
#for i in range(1, 1001):
#	par = param_list[i-1]
#	print i, ' par: ', par
#	for j in range(1, 5):
#		h = f.Get('h_1stProb_Gen_'+str(j)).Clone()
#		h_scale = h * par
#		h_scale.SetName('h_1stProb_Gen_'+str(j)+'_'+str(i))
#		print h_scale.GetName(), '\n'
#		h_scale.Write()
#
#f_out.Close()

def fit(file_in, file_out, parameters):

	f = TFile.Open(file_in, 'READ')
	f_out = TFile.Open(file_out, 'RECREATE')

	param = open(parameters, 'r')
	param_list = map(float, param.readlines())

	for i in range(1, 1001):
		par = param_list[i-1]
		print i, ' par: ', par

		if 'ttbb' in file_in:
			for j in range(1, 5):
				name1 = 'h_1stProb_Gen_'+str(j)
				h1 = f.Get(name1).Clone()
				h1_scale = h1 * par
				h1_scale.SetName(name1+'_'+str(i))
				print h1_scale.GetName()
				h1_scale.Write()
				
#				name2 = 'h_Pttbb_Gen_'+str(j)
#				h2 = f.Get(name2).Clone()
#				h2_scale = h2 * par
#				h2_scale.SetName(name2+'_'+str(i))
#				print h2_scale.GetName()
#				h2_scale.Write()
				
		else:
			name1 = 'h_1stProb'
			h1 = f.Get(name1).Clone()
			h1_scale = h1 * par
			h1_scale.SetName(name1+'_'+str(i))
			print h1_scale.GetName()
			h1_scale.Write()

#			name2 = 'h_Pttbb'
#			h2 = f.Get(name2).Clone()
#			h2_scale = h2 * par
#			h2_scale.SetName(name+'_'+str(i))
#			print h2_scale.GetName()
#			h2_scale.Write()

		print '\n'

	f_out.Close()


fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/split_ttbb.root', 'ttbb_fitPttbb.root', 'par1.txt')
fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/rebin/rebinned_ttbj.root', 'ttbj_fitPttbb.root', 'par2.txt')
fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/rebin/rebinned_Bkg_ttcc+ttLF+ttother.root', 'Bkg_ttcc+ttLF+ttother_fitPttbb.root', 'par3.txt')

