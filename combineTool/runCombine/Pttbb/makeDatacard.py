import os

def makeCard(num):
	hist = 'h_Pttbb'
	obs_hist = hist+'_'+str(num)
	inputDir = '/home/juhee5819/cheer/T2/combineTool/data/rebin/'

	datacard=open(cardName+'.txt', "w")
	datacard.write("* imax 1 \n")
	datacard.write("* jmax 5 \n")
	datacard.write("* kmax * \n")

	datacard.write("----------------\n")
	datacard.write('shapes data_obs * ')
	datacard.write(inputDir+'rebinned_data.root ')
	datacard.write(obs_hist+'\n')
	datacard.write('shapes ttbb * ')
	datacard.write(inputDir+'rebinned_ttbb.root ')
	datacard.write(hist+'\n')
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

	#datacard.write("bin			bin1 bin1 bin1 bin1")
	datacard.write("bin			bin1 bin1 bin1 bin1 bin1 bin1")
	datacard.write("\n")

	datacard.write("process 	")
	datacard.write('ttbb ttbj Bkg TTTo2L2Nu TTToHadronic WJets')
	datacard.write('\n')

	datacard.write('process 	-1 1 2 3 4 5')
	datacard.write('\n')

	datacard.write('rate		-1 -1 -1 -1 -1 -1')
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
for i in range(1, 1001):
	cardName = outDir+'datacard_'+str(i)
	#po ="--PO map='.*/ttbb:r_bin1[1,0,10]' --PO map='.*/ttbj:r_bin2[1,0,10]' --PO map='.*/ttcc:r_bin3[1,0,10]' --PO map='.*/Bkg:r_bin4[1,0,10]'"
	po ="--PO map='.*/ttbb:r_bin1[1,0,10]' --PO map='.*/ttbj:r_bin2[1,0,10]' --PO map='.*/Bkg:r_bin3[1,0,10]' --PO map='.*/TTTo2L2Nu:r_bin4[1,0,10]' --PO map='.*/TTToHadronic:r_bin5[1,0,10]' --PO map='.*/WJets:r_bin6[1,0,10]'"
	t2wLine = "text2workspace.py "+cardName+".txt -o "+cardName+".root -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel "+po+"\n"
	#comLine = "combine -M MultiDimFit --algo singles --setParameters=r_bin1=1,r_bin2=1,r_bin3=1,r_bin4=1 -d "+cardName+".root -t 0 \n"
	comLine = "combine -M MultiDimFit --algo singles --setParameters=r_bin1=1,r_bin2=1,r_bin3=1,r_bin4=1,r_bin5=1,r_bin6=1 -d "+cardName+".root -t 0 \n"
	t2w.write(t2wLine)
	com.write(comLine)
	makeCard(i)

