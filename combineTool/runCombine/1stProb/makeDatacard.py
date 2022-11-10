import os, re

def makeCard(num):
	hist = 'h_1stProb'
	obs_hist = hist+'_'+str(num)
	n = str(num)
	inputDir = '/home/juhee5819/cheer/T2/combineTool/data/rebin/'

	datacard=open(cardName+'.txt', "w")
	datacard.write("* imax 4 \n")
	datacard.write("* jmax 8 \n")
	datacard.write("* kmax * \n")

	datacard.write("----------------\n")
	datacard.write('shapes data_obs * ')
	datacard.write(inputDir+'rebinned_data.root ')
	datacard.write(obs_hist+'\n')
	datacard.write('shapes Gen_1 * ')
	datacard.write(inputDir+'rebinned_ttbb.root ')
	datacard.write(hist+'_Gen_1\n')
	datacard.write('shapes Gen_2 * ')
	datacard.write(inputDir+'rebinned_ttbb.root ')
	datacard.write(hist+'_Gen_2\n')
	datacard.write('shapes Gen_3 * ')
	datacard.write(inputDir+'rebinned_ttbb.root ')
	datacard.write(hist+'_Gen_3\n')
	datacard.write('shapes Gen_4 * ')
	datacard.write(inputDir+'rebinned_ttbb.root ')
	datacard.write(hist+'_Gen_4\n')
	datacard.write('shapes ttbj * ')
	datacard.write(inputDir+'rebinned_ttbj.root ')
	datacard.write(hist+'\n')
	datacard.write('shapes Bkg * ')
	datacard.write(inputDir+'rebinned_Bkg.root ')
	datacard.write(hist+'\n')
	datacard.write('shapes TTTo2L2Nu * ')
	datacard.write(inputDir+'rebinned_TTTo2L2Nu.root ')
	datacard.write(hist+'\n')
	datacard.write('shapes TTToHadronic * ')
	datacard.write(inputDir+'rebinned_TTToHadronic.root ')
	datacard.write(hist+'\n')
	datacard.write('shapes WJets * ')
	datacard.write(inputDir+'rebinned_WJetsToLNu.root ')
	datacard.write(hist+'\n')
	datacard.write("----------------\n")

	datacard.write("bin bin1")
	datacard.write("\n")

	datacard.write("observation -1")
	datacard.write("\n")
	datacard.write("----------------\n")

	datacard.write("bin			bin1 bin1 bin1 bin1 bin1 bin1 bin1 bin1 bin1")
	datacard.write("\n")

	datacard.write("process 	")
	datacard.write('Gen_1 Gen_2 Gen_3 Gen_4 ttbj Bkg TTTo2L2Nu TTToHadronic WJets')
	datacard.write('\n')

	datacard.write('process 	-1 -2 -3 -4 1 2 3 4 5')
	datacard.write('\n')

	datacard.write('rate		-1 -1 -1 -1 -1 -1 -1 -1 -1')
	datacard.write('\n')
	datacard.write("----------------\n")

	datacard.write("### RUN WITH COMMANDS: ####\n")
	datacard.write('# '+t2wLine)
	datacard.write('# Run with command: '+comLine)
	#datacard.write("# text2workspace.py "+cardName+".txt -o "+cardName+".root -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel "+po+"\n")
	#datacard.write("# Run with command: combine -M MultiDimFit --algo singles --setParameters=r_bin1=1,r_bin2=1,r_bin3=1,r_bin4=1 -d "+cardName+".root -t 0 \n")
	datacard.write("############################\n")
	datacard.close()

t2w = open('t2w.sh', 'w')
com = open('combine.sh', 'w')
outDir = './datacards/'
os.makedirs( outDir )

parDir = '/home/juhee5819/cheer/T2/combineTool/runCombine/Pttbb/fit/'
f1 = open(parDir+'par1.txt')
f2 = open(parDir+'par2.txt')
f3 = open(parDir+'par3.txt')
f4 = open(parDir+'par4.txt')
f5 = open(parDir+'par5.txt')
f6 = open(parDir+'par6.txt')

for i in range(1, 1001):
	
	# get parameters
	# ttbb
	p1 = re.split('   |/| ', f1.readline())
	p_ttbb = float(p1[4])
	# ttbj
	p2 = re.split('   |/| ', f2.readline())
	p_ttbj = float(p2[4])
	nm_ttbj = p_ttbj+(float(p2[5])*3)
	np_ttbj = p_ttbj+(float(p2[6])*3)
	# Bkg
	p3 = re.split('   |/| ', f3.readline())
	p_Bkg = float(p3[4])
	nm_Bkg = p_Bkg+(float(p3[5])*3)
	np_Bkg = p_Bkg+(float(p3[6])*3)
	# TTTo2L2Nu
	p4 = re.split('   |/| ', f4.readline())
	p_TTTo2L2Nu = float(p4[4])
	nm_TTTo2L2Nu = p_TTTo2L2Nu+(float(p4[5])*3)
	np_TTTo2L2Nu = p_TTTo2L2Nu+(float(p4[6])*3)
	# TTToHadronic
	p5 = re.split('   |/| ', f5.readline())
	if p5[3]=='':
		p_TTToHadronic = float(p5[4])
		nm_TTToHadronic = p_TTToHadronic+(float(p5[5])*3)
		np_TTToHadronic = p_TTToHadronic+(float(p5[6])*3)
	else:
		p_TTToHadronic = float(p5[3])
		nm_TTToHadronic = p_TTToHadronic+(float(p5[4])*3)
		np_TTToHadronic = p_TTToHadronic+(float(p5[5])*3)

	# WJets
	p6 = re.split('   |/| ', f6.readline())
	p_WJets = float(p6[4])
	nm_WJets = p_WJets+(float(p6[5])*3)
	np_WJets = p_WJets+(float(p6[6])*3)

	cardName = outDir+'datacard_'+str(i)
	po ="--PO map='.*/Gen_1:r_bin1["+str(p_ttbb)+",0,10]' --PO map='.*/Gen_2:r_bin2["+str(p_ttbb)+",0,10]' --PO map='.*/Gen_3:r_bin3["+str(p_ttbb)+",0,10]' --PO map='.*/Gen_4:r_bin4["+str(p_ttbb)+",0,10]'  --PO map='.*/ttbj:r_bin5["+str(p_ttbj)+","+str(nm_ttbj)+","+str(np_ttbj)+"]'  --PO map='.*/Bkg:r_bin6["+str(p_Bkg)+","+str(nm_Bkg)+","+str(np_Bkg)+"]'  --PO map='.*/TTTo2L2Nu:r_bin7["+str(p_TTTo2L2Nu)+","+str(nm_TTTo2L2Nu)+","+str(np_TTTo2L2Nu)+"]' --PO map='.*/TTToHadronic:r_bin8["+str(p_TTToHadronic)+","+str(nm_TTToHadronic)+","+str(np_TTToHadronic)+"]'  --PO map='.*/WJets:r_bin9["+str(p_WJets)+","+str(nm_WJets)+","+str(np_WJets)+"]'"

	t2wLine = "text2workspace.py "+cardName+".txt -o "+cardName+".root -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel "+po+"\n"
	comLine = "combine -M MultiDimFit --algo singles --setParameters=r_bin1=1,r_bin2=1,r_bin3=1,r_bin4=1,r_bin5=1,r_bin6=1,r_bin7=1,r_bin8=1,r_bin9=1 -d "+cardName+".root -t 0 \n"
	t2w.write(t2wLine)
	com.write(comLine)
	makeCard(i)

