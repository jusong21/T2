


def multi(parameters, ratios, file_out):

	param = open(parameters, 'r')
	param_list = map(float, param.readlines())

	ratio = open(ratios, 'r')
	ratio_list = map(float, rat.readlines())

	mul = 0
	f_out = open(file_out, 'w')
	for i in range(0, 1000):
		par = param_list[i]
		rat = ratio_list[i]
		mul = par*rat
		f_out.write(str(mul)+'\n')

	f_out.close()

multi('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par1.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/random/ratio.txt', 'multipliedPar1.txt')
multi('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par2.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/random/ratio.txt', 'multipliedPar2.txt')
multi('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par3.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/random/ratio.txt', 'multipliedPar3.txt')
multi('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par4.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/random/ratio.txt', 'multipliedPar4.txt')
multi('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par5.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/random/ratio.txt', 'multipliedPar5.txt')
multi('/home/juhee5819/cheer/HiggsAnalysis/combineTool/data/1stProb/fit/par5.txt', '/home/juhee5819/cheer/HiggsAnalysis/combineTool/scale/random/ratio.txt', 'multipliedPar5.txt')


