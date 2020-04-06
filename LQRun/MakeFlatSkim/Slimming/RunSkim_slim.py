import os, getpass, sys
import time
from functions import *

sampledir = ["WZ_TuneCUETP8M1_13TeV-pythia8",
                          "WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
                          "TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8",
                          "ZZ_TuneCUETP8M1_13TeV-pythia8",
                          "WW_TuneCUETP8M1_13TeV-pythia8",
                          "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
                          "TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8",
                          "TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8",
                           "TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8",
                          "TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8",
                          "ttHTobb_M125_13TeV_powheg_pythia8",
                          "ttHToNonbb_M125_13TeV_powheg_pythia8",
                          "VBF_HToMuMu_M125_13TeV_powheg_pythia8",
#                          "GluGlu_HToMuMu_M125_13TeV_powheg_pythia8",
             "QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                          "QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8",
                           "ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1",
                          "ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1",
                          "ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1",
                          "ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1",
                          "TT_TuneCUETP8M1_13TeV-powheg-pythi8"]

sampledir = ["WZ_TuneCUETP8M1_13TeV-pythia8"]

for i in sampledir:
   output=i
   print "Making dir: " + output
   
   if not (os.path.exists(output)):
      os.system("mkdir " + output)
      os.system("mkdir " + output + "/output/")
   else:
      os.system("rm -r " + output + "/*")
      if not (os.path.exists(output + "/output/")):
         os.system("mkdir " + output + "/output/")
              
      
   os.system("ls /data7/DATA/cattoflat/skim/" + i + " > " + output + "/list.txt" )

   fr = open(output + "/list.txt" , 'r')
   counter=0
   for line in fr:
      if ".root" in line:
         counter=counter+1


   runscript= "SlimFlatCat.h"
   runscriptC="SlimFlatCat.C"
   for j in range(1,counter+1):
      if not (os.path.exists(output+ "/" + str(j))):
         os.system("mkdir " + output+ "/" + str(j))
         
      configfile=open(output+ "/"  + str(j) + "/" + runscript,'w')
      configfile.write(makeNtupleMakerSlimH("/data7/DATA/cattoflat/skim/" + output,output+ "/list.txt",j, output))
      configfile.close()

      configfileC=open(output+ "/" + str(j) + "/" + runscriptC,'w')
      configfileC.write(makeNtupleMakerSlimC(output + "/" +  str(j),output+ "/list.txt", j))
      configfileC.close()
      
      os.system("root -l -q -b " +  output+ "/" + str(j) + "/SlimFlatCat.C &> " + output + "/" + str(j) + "/log.txt&" )


   job_finised=False
   while not job_finised:
      time.sleep(20.)
      os.system("ls " +  output+ "/output/ > " + output + "/checkoutput.txt")
      count=0
      for line in open( output + "/checkoutput.txt", 'r'):
         if ".root" in line:
            count = count+1

         if count == counter:
            job_finised=True


   if not (os.path.exists("/data7/DATA/cattoflat/skim/slim/" + i)):
      os.system("mkdir " + "/data7/DATA/cattoflat/skim/slim/" + i)

      
   print "Moving samples to /data7/DATA/cattoflat/skim/slim/" + i    
   os.system("mv "  +  output+ "/output/*.root /data7/DATA/cattoflat/skim/slim/" + i )
   print "mv "  +  output+ "/output/*.root /data7/DATA/cattoflat/skim/slim/" + i 
   
   os.system("rm -r " + output)
