from ROOT import *

param = ['par1.txt', 'par2.txt', 'par3.txt', 'par4.txt', 'par5.txt', 'par6.txt']

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
				name1 = 'h_1stProb_Gen_'+str(j)+'_'+str(i)
				h1 = f.Get(name1).Clone()
				h1_scale = h1 * par
				#h1_scale.SetName(name1+'_'+str(i))
				print h1_scale.GetName()
				h1_scale.Write()
				
				name2 = 'h_Pttbb_Gen_'+str(j)+'_'+str(i)
				h2 = f.Get(name2).Clone()
				print h2
				h2.Write()
				
		else:
			name1 = 'h_1stProb_'+str(i)
			h1 = f.Get(name1).Clone()
			h1_scale = h1 * par
			#h1_scale.SetName(name+'_'+str(i))
			print h1_scale.GetName()
			h1_scale.Write()

			name2 = 'h_Pttbb_'+str(i)
			h2 = f.Get(name2).Clone()
			#h2_scale.SetName(name+'_'+str(i))
			print h2.GetName()
			h2.Write()

		print '\n'

	f_out.Close()


fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/Pttbb/fitPttbb/ttbb_fitPttbb.root', 'ttbb_fit.root', 'par1.txt')
fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/rebin/rebinned_ttbj.root', 'ttbj_fitPttbb.root', 'par2.txt')
fit('/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/rebin/rebinned_Bkg_ttcc+ttLF+ttother.root', 'Bkg_ttcc+ttLF+ttother_fitPttbb.root', 'par3.txt')

