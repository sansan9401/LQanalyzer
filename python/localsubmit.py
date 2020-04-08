################################################################## 
### configure Job
################################################################### 
timeWait=1#

###################################################
### Make Input File
###################################################
import os, getpass, sys
from functions import *

from optparse import OptionParser

#Import parser to get options
parser = OptionParser()
parser.add_option("-p", "--period", dest="period", default="A",help="which data period or mc sample")
parser.add_option("-s", "--stream", dest="stream", default="", help="Which data channel- ee,or mumu?")
parser.add_option("-j", "--jobs", dest="jobs", default=1, help="Name of Job")
parser.add_option("-c", "--cycle", dest="cycle", default="Analyzer", help="which cycle")
parser.add_option("-t", "--tree", dest="tree", default="rootTupleTree/tree", help="What is input tree name?")
parser.add_option("-o", "--logstep", dest="logstep", default=-1, help="How many events betwene log messages")
parser.add_option("-d", "--data_lumi", dest="data_lumi", default="A", help="How much data are you running on/ needed to weight mc?")
parser.add_option("-l", "--loglevel", dest="loglevel", default="INFO", help="Set Log output level")
parser.add_option("-n", "--nevents", dest="nevents", default=-1, help="Set number of events to process")
parser.add_option("-k", "--skip", dest="skip", default=-1, help="Set number of events to skip")
parser.add_option("-a", "--datatype", dest="datatype", default="", help="Is data or mc?")
parser.add_option("-e", "--totalev", dest="totalev", default=-1, help="How many events in sample?")
parser.add_option("-x", "--xsec", dest="xsec", default=-1., help="How many events in sample?")
parser.add_option("-T", "--targetlumi", dest="targetlumi", default=-1., help="How many events in sample?")
parser.add_option("-E", "--efflumi", dest="efflumi", default=-1., help="How many events in sample?")
parser.add_option("-O", "--outputdir", dest="outputdir", default="${LQANALYZER_DIR}/data/output/", help="Where do you like output to go?")
parser.add_option("-w", "--remove", dest="remove", default=True, help="Remove the work space?")
parser.add_option("-S", "--skinput", dest="skinput", default="True", help="Use SKTree as input?")
parser.add_option("-R", "--runevent", dest="runevent", default=True, help="Run Specific Event?")
parser.add_option("-N", "--samples2016", dest="samples2016", default="True", help="samples2016? add samples2016='True' to run on these samples")
parser.add_option("-L", "--LibList", dest="LibList", default="", help="Add extra lib files to load")
parser.add_option("-D", "--debug", dest="debug", default=False, help="Run submit script in debug mode?")
parser.add_option("-m", "--useskim", dest="useskim", default="Lepton", help="Run submit script in debug mode?")
parser.add_option("-P", "--runnp", dest="runnp", default="runnp", help="Run fake mode for np bkg?")
parser.add_option("-Q", "--runcf", dest="runcf", default="runcf", help="Run fake mode for np bkg?")
parser.add_option("-b", "--usebatch", dest="usebatch", default="NULL", help="Run in batch queue?")
parser.add_option("-q", "--queue", dest="queue", default="", help="which queue?")


###################################################
#set the local variables using options
###################################################
(options, args) = parser.parse_args()
number_of_cores = int(options.jobs)
sample = options.period
channel = options.stream
cycle = options.cycle
logstep = int(options.logstep)
loglevel = options.loglevel
runnp = options.runnp
runcf = options.runcf
queue = options.queue
usebatch =options.usebatch
### THESE ARE OPTIONS THAT CAN BE INCLUDED but not in example
tree = options.tree
number_of_events_per_job= int(options.nevents)
skipev = int(options.skip)
dataType = options.datatype
totalev = int(options.totalev)
xsec = float(options.xsec)
tar_lumi = float(options.targetlumi)
eff_lumi = float(options.efflumi)
data_lumi = options.data_lumi
Finaloutputdir = options.outputdir
remove_workspace=options.remove
useskinput=options.skinput
runevent= options.runevent
samples2016 = options.samples2016
tmplist_of_extra_lib=options.LibList
DEBUG = options.debug
useskim = options.useskim

new_channel = channel.replace(":", "")
original_channel = new_channel

queue_command = ""
if queue  == "exclude_1":
    queue_command = " -q allbut1 "
elif queue  == "exclude_2":
    queue_command = " -q allbut2 "
elif queue  == "exclude_3":
    queue_command = " -q allbut3 "
elif queue  == "exclude_4":
    queue_command = " -q allbut4 "
elif queue  == "exclude_5":
    queue_command = " -q allbut5 "
elif queue  == "exclude_6":
    queue_command = " -q allbut6 "
elif queue  == "exclude_7":
    queue_command = " -q allbut7 "
elif queue  == "exclude_8":
    queue_command = " -q allbut8 "
elif  queue  == "node_1":
    queue_command = " -q single1 "
elif  queue  == "node_2":
    queue_command = " -q single2 "
elif  queue  == "node_3":
    queue_command = " -q single3 "
elif  queue  == "node_4":
    queue_command = " -q single4 "
elif  queue  == "node_5":
    queue_command = " -q single5 "
elif  queue  == "node_6":
    queue_command = " -q single6 "
elif  queue  == "node_7":
    queue_command = " -q single7 "
elif  queue  == "node_8":
    queue_command = " -q single8 "
elif  queue  == "all":
    queue_command = ""
else:
    queue_command = " -q single1 "

##############################
### check output dir exists
##############################

if not os.path.exists(Finaloutputdir):
    os.system("mkdir " +Finaloutputdir)
    
    if not os.path.exists(Finaloutputdir):
        print "Output directory changes to " + Finaloutputdir + ". This directory does not exist. Create this directory and rerun."
        sys.exit()
    else:
        print "Output directory changes to " + Finaloutputdir + ". Creating this directory"

if "/home/" in Finaloutputdir:
    print "WARNING!!!!!!!!!!!!!!!!!!!!!!!!"
    print "output directory is set to /home/. Advise to set directory to default (or similar): "+ os.getenv("LQANALYZER_OUTPUT_PATH")


list_of_extra_lib=[]
libname=''
for lib in tmplist_of_extra_lib:
    if '"' in libname:
        libname=""
    if ',' in libname:
        libname=""
        
    libname+=lib
    if ".so" in libname:
        list_of_extra_lib.append(libname)
        libname=""
    
if libname:
    if len(list_of_extra_lib) ==0:
        print "Name of library has to contain .so."
   
for lib in list_of_extra_lib:
    print "Adding " + lib + " to list of Libraies to Load"


if str(DEBUG) == "True":
    print "In debug mode"

print "Running : " + cycle

if str(useskinput) == "True": 
    print "Using SKTrees as input."
elif str(useskinput) == "true":
    print "Using SKTrees as input."
else:
    print "Using LQntuples as input"    

########  Sample specific configuration ###############
## set the job conguration set for a specific sample###
#######################################################
sample = sample.replace(":", " ")
datatype=""
splitsample  = sample.split()
if not len(splitsample)==1:
    sample = splitsample[0]
    for conf in range(1,len(splitsample)-1):
        if "nevents" in splitsample[conf]:
            conf+=1
            number_of_events_per_job = splitsample[conf]
        if "remove" in splitsample[conf]:    
            conf+=1
            remove_workspace  = splitsample[conf]
        if "loglevel" in splitsample[conf]:
            conf+=1
            loglevel = splitsample[conf]
        if "cycle"  in splitsample[conf]:
            conf+=1
            cycle = splitsample[conf]
        if "njobs" in splitsample[conf]:
            conf+=1
            number_of_cores = splitsample[conf]
        if "skipevent" in splitsample[conf]:
            conf+=1
            skipev = splitsample[conf]
        if "skinput" in splitsample[conf]:
            conf+=1
            useskinput = splitsample[conf]
        if "runevent" in splitsample[conf]:
            conf+=1
            runevent = splitsample[conf]

###########################################################################################
###########################################################################################
### DEFAULT  settings for runnning in batch mode. True for tamsa2.snu.ac.kr
running_batch=True

if str(usebatch) == "NULL":
    if str(running_batch) == "True":
        print "%%%%%%%%%%%%%%%%%%%%%%%%"
        print "Running batch job:"
        print "%%%%%%%%%%%%%%%%%%%%%%%%"
    else:
        print "Running standard root interactive job:"
else:
    if str(usebatch) == "False":
        running_batch=False
    elif  str(usebatch) == "false":
        running_batch=False

##########################################################################################
###########################################################################################

####################
####
####################

if not str(cycle) == "SKTreeMaker":
    if not str(cycle) == "SKTreeMakerNoCut":
        if not str(cycle) == "SKTreeMakerDiLep":
            if not str(useskinput) == "True":
                if not (useskinput) == "true":
                    print "Running on LQNtuples"
#update = raw_input("You are running on LQntuples. This will be cpu extensive. This is only advisable if you are testing some new branches NOT in SKTrees. Will change settings to run on SKTrees: Type 'N' if you wish to stick to LQntuples.")
                    #if not  str(update) == "N":
                    #    useskinput="True"

##########################################################
### Make tmp directory for job
############################################################

output_mounted="/data7/DATA"

tmpwork = output_mounted+"/LQ_SKTreeOutput/"+ getpass.getuser() + "/"
if not (os.path.exists(tmpwork)):
    os.system("mkdir " + tmpwork)

timestamp_dir=tmpwork + "/" + cycle + "_joboutput_" +now() +"_" +os.getenv("HOSTNAME")

while  (os.path.exists(timestamp_dir)):
    app_dir=1
    timestamp_dir = timestamp_dir + "_v" + str(app_dir)
    app_dir = app_dir+1
if not (os.path.exists(timestamp_dir)):
    os.system("mkdir " + timestamp_dir)

    
if not os.path.exists(timestamp_dir+"/job_output/"):
    os.system("mkdir " + timestamp_dir+"/job_output/")
    
local_sub_dir=  timestamp_dir + "/job_output/"  + sample + '_' + new_channel + '_' + now()
if not os.path.exists(local_sub_dir):
    os.system("mkdir " + local_sub_dir)

        

                        
        
##################################################################################################################
#### HARD CODE THE MAXIMUM number of subjobs
##################################################################################################################
ncore_def=number_of_cores
import platform
username = str(os.getenv("USER"))
if platform.system() == "Linux":
    os.system("top -n 1 -b | grep 'root.exe' &> " + local_sub_dir + "/toplog")
    filename = local_sub_dir +'/toplog'

    n_previous_jobs=0
    njob_user=0
    for line in open(filename, 'r'):
        n_previous_jobs+=1
        if username in line:
            njob_user+=1
            
    if n_previous_jobs > 15:
        number_of_cores = 1
        print "Number of subjobs is reduced to 1, since there are over 15 subjobs running on this machine."

    if njob_user  > 10:
        number_of_cores = 1
    os.system("rm " + filename)

    os.system("top  -n 1 -b | grep 'cmsRun' &> " + local_sub_dir + "/toplog2")
    filename2 = local_sub_dir +'/toplog2'
    for line in open(filename2, 'r'):
        n_previous_jobs+=1
    os.system("rm " + filename2)
    if n_previous_jobs > 15:
        number_of_cores = 1
        print "Number of subjobs is reduced to 1, since there are over 15 jobs running on this machine."
        
IsSKTree= False
if str(useskinput) == "true":
    IsSKTree = True
elif (useskinput) == "True":
    IsSKTree = True        

if number_of_cores > 1:
    if IsSKTree:
        if (15 - n_previous_jobs) < number_of_cores:
            number_of_cores = 15 - n_previous_jobs
        if number_of_cores > 10:
            number_of_cores = 10

    else:
        if number_of_cores > 5:
            if not str(cycle) == "SKTreeMaker":
                if not str(cycle) == "SKTreeMakerNoCut":
                    if not str(cycle) == "SKTreeMakerDiLep":
                        number_of_cores = 5

if "SKTreeMaker" in str(cycle):
    if number_of_cores > 1:
        number_of_cores = 30
       
    
if number_of_cores < 0:
    number_of_cores=1
##################################################################################################################            
##### FINISHED CONFIGURATION
##################################################################################################################
singlejob = number_of_cores==1            




#### determine if input is data/mc
mc = len(sample)>1
if mc:
    datatype="mc"
else:
    datatype="data"

if sample == "AtoD":
    datatype="data"

if datatype == "mc":
    timeWait=10

if not dataType =="":
    datatype=dataType

##################################################################################################################
### Make a list of input samples: at the moment this is useless. Will add code to include * options in input
##################################################################################################################
list = []
import re
if ("*" in sample) and mc:
    print "ADD code"
else:
    list.append(sample)
#list has only size ==1 currently

##################################################################################################################
##### Specify if the job is running on SKTrees or LQNtuples
##################################################################################################################
original_sample = sample
host_postfix=""
new_sample_fix=""

if not IsSKTree:
    samples2016="False"

if samples2016 =="True":
    new_sample_fix="_2016"
elif samples2016 == "true":
    new_sample_fix="_2016"
#if "tamsa2.snu.ac.kr" in str(os.getenv("HOSTNAME")):
new_sample_fix=""


if IsSKTree:
    if not mc:
        if useskim == "Lepton":
            new_channel="SK" + host_postfix +new_channel + new_sample_fix
        else:
            if useskim == "NoCut":
                new_channel="SK" + host_postfix + new_channel + new_sample_fix+ "_nocut"
            else:
                if useskim == "DiLep":
                    new_channel="SK" + host_postfix + new_channel + new_sample_fix+ "_dilep"

    else:
        if useskim == "Lepton":
            sample="SK" + host_postfix +  sample+ new_sample_fix
        else:
            if useskim == "NoCut":
                sample="SK" + host_postfix  + sample + new_sample_fix +"_nocut"
            else:
                if useskim == "DiLep":
                    sample="SK" + host_postfix + sample + new_sample_fix+"_dilep"

                
print "Input sample : "   + sample
if not mc:
    print "Input channel  : " + new_channel

##############################################################################################
#### Check if sktrees are located on current machines  (not used when running on cmsX at snu)                        
#############################################################################################

isfile = os.path.isfile
join = os.path.join
if platform.system() != "Linux":

    localDir = os.getenv("LQANALYZER_DIR")+ "/data/input/" 
    if not mc:        
        localDir = os.getenv("LQANALYZER_DIR")+ "/data/input/data/" + new_channel  + sample
    else:
        localDir = os.getenv("LQANALYZER_DIR")+ "/data/input/mc/"  + sample
    
    if not os.path.exists(localDir):
        print "No files in current location: Will copy them over"
        CopySKTrees(new_channel,sample,mc,"True")
    elif  sum(1 for item in os.listdir(localDir) if isfile(join(localDir, item))) == 0:
        print "No files are located locally: Will copy from cms21 machine"
        CopySKTrees(new_channel,sample,mc,"True")
    else:
        update = raw_input("Files already located on current machine. Do you want these updating? Yes/No")
        if update == "Yes":
            print "Updating local sktree"
            CopySKTrees(new_channel,sample,mc,"True")
        elif update == "yes":
            print "Updating local sktree"
            CopySKTrees(new_channel,sample,mc,"True")
        else:
            CheckPathInFile(new_channel,sample,mc)
            
##################################################################################################################
#Find the DS name (and lumi if MC) from txt/datasets.txt
##################################################################################################################
inDS = ""
mcLumi = 1.0
filechannel=""

if platform.system() == "Linux":
    version="_5_3_14"
    if samples2016=="True":
        print "Using ntuple Version 5320"
    else:
        print "Using ntuple Version 5314"

    filename = os.getenv("LQANALYZER_RUN_PATH") + '/txt/datasets_snu' + version +  '.txt'
    
else:
    filename = os.getenv("LQANALYZER_RUN_PATH") + 'txt/datasets_mac.txt'


ntup_path_link=""
if IsSKTree:
    if not mc:
        for line in open(filename, 'r'):
            if not line.startswith("#"):
                entries = line.split()
                if len(entries)==5:
                    if new_channel ==entries[0] and sample == entries[1]:
                        inDS = entries[4]        
                        ntup_path_link = entries[2]
                        
        sample = "period"+sample
        eff_lumi=1.
        tar_lumi=1.
        filechannel = new_channel+"_"

    else:
        for line in open(filename, 'r'):
            if not line.startswith("#"):
                entries = line.split()
                if len(entries)==5:
                    if sample == entries[0]:
                        eff_lumi = entries[1]
                        inDS = entries[4]
                        ntup_path_link = entries[2]
else:
    if not mc:
        for line in open(filename, 'r'):
            if not line.startswith("#"):
                entries = line.split()
                if len(entries)==5:
                    if new_channel ==entries[0] and sample == entries[1]:
                        inDS = entries[4]
                        ntup_path_link = entries[2]
        sample = "period"+sample
        eff_lumi=1.
        tar_lumi=1.
        filechannel = new_channel+"_"

    else:
        for line in open(filename, 'r'):
            if not line.startswith("#"):
                entries = line.split()
                if len(entries)==5:
                    if sample == entries[0]:
                        eff_lumi = entries[1]
                        inDS = entries[4]
                        ntup_path_link = entries[2]

                        
ntuple_path=""
for line in open(filename, 'r'):
    if not line.startswith("#"):
        entries = line.split()
        if len(entries)==2:
            if ntup_path_link == entries[0]:
                ntuple_path= entries[1]
print "ntup_path_link = " +ntup_path_link

dir_break="/"
if ntuple_path.endswith('/'):
    dir_break=""

InputDir = ntuple_path + dir_break + inDS    

print "##################################################################################################################"
print "Input directory= " + InputDir    ## now have defined what dur contains input files
print "##################################################################################################################     "

############################################################
############################################################
###### RUN JOB
############################################################
############################################################

os.system("ls " + InputDir + "/*.root > " + local_sub_dir + "/inputlist.txt")

############################################################
## Get number of files in Input directory
############################################################
isfile = os.path.isfile
join = os.path.join
number_of_files = sum(1 for item in os.listdir(InputDir) if isfile(join(InputDir, item)))

if DEBUG == "True":
    print "Job has " + str(number_of_files) + " files to process:"


############################################################                                                                                                                                                                 
### Do not change njobs if using batch                                                                                                                                                                                                  
############################################################                                                                                                                                                                 
if running_batch:
    number_of_cores= ncore_def
    n_qsub_jobs=int(os.popen("condor_q -al -af requestcpus|paste -sd+|bc").read().strip() or 0)
    if n_qsub_jobs > 500:
        print "WARNING: More than 500 jobs in batch queue. If job is small and uses dilepton skim consider running on cms1-6"
    
    #### Allow each user to submit 300 jobs at a time.???
    n_user_qsub_jobs=int(os.popen("condor_q -af requestcpus|paste -sd+|bc").read().strip() or 0)

    running_large_sample=False
    large_samples = []
    large_samples.append("DY")
    large_samples.append("ttbar")
    if not  "SKTreeMaker" in str(cycle):
        if mc:
            for l_s in  large_samples:
                if l_s in sample:
                    running_large_sample=True
            if running_large_sample:
                if number_of_cores > 100:
                    number_of_cores=100
            else:
                if queue == "all":
                    if n_user_qsub_jobs > 300:
                        number_of_cores=5
                    elif n_user_qsub_jobs > 200:
                        number_of_cores=15
                    elif n_user_qsub_jobs > 100:
                        number_of_cores=20
                    elif n_user_qsub_jobs > 60:
                        number_of_cores=30
                    elif n_user_qsub_jobs > 40:
                        number_of_cores=50
                    else:
                        if n_qsub_jobs < 30:
                            number_of_cores=100
                        else:
                            number_of_cores=50
        else:
            if number_of_cores > 100:
                number_of_cores = 100

if ncore_def == 1:
    number_of_cores = 1
                                                   
############################################################
### Correct user if ncores is > nfiles
############################################################
if number_of_cores > number_of_files:
    number_of_cores = number_of_files
print "Splitting job into " + str(number_of_cores) + " subjobs"


############################################################  
### Do not change njobs if using batch 
############################################################                                                                                                                                                                                

############################################################
### set number of files per job
############################################################
nfilesperjobs= 0
for i in range(1,number_of_files):
    if not i%number_of_cores:
        nfilesperjobs+=1

if number_of_cores == 1:
    nfilesperjobs = number_of_files

if nfilesperjobs == 0:
    nfilesperjobs=1
    
files_torun = (nfilesperjobs*number_of_cores)
remainder = number_of_files - (nfilesperjobs*number_of_cores)

if DEBUG == "True":
    print "Each job will process  " + str(nfilesperjobs) + "/" + str(nfilesperjobs+1) + " files"


###################################################
## counters
###################################################
nfiles=0
count=1
total_nsamples=0
filesprocessed=0
nfiles_file=0
n_remainder_files=0
check_array = []

###################################################
# Setup work area on var tmp
###################################################

if not (os.path.exists(output_mounted+"/LQ_SKTreeOutput/")):
    os.system("mkdir /data7/DATA/LQ_SKTreeOutput/")

workspace = output_mounted+"/LQ_SKTreeOutput/"+ getpass.getuser() + "/"
if not (os.path.exists(workspace)):
        os.system("mkdir " + workspace)
out_end=sample

output=workspace + sample + "_" + now() + "_" + os.getenv("HOSTNAME")  + "/"
if not mc:
    output=workspace + new_channel+ "_"+ sample + "_" + now() + "_" + os.getenv("HOSTNAME") + "/"
        
        
outputdir= output+ "output/"
outputdir_tmp= output+ "output_tmp/"
if not (os.path.exists(output)):
    os.system("mkdir " + output)
    print "Making tmp working directory to run Job  : " + output

if(os.path.exists(outputdir)):
    number_of_outputfiles = sum(1 for item in os.listdir(outputdir) if isfile(join(outputdir, item)))
    if  not number_of_outputfiles ==0:
       os.system("rm " + outputdir + "/*.root")
       print "Emptying output directory as this should be empty for new job"
              
if not (os.path.exists(outputdir)):
    os.system("mkdir " + outputdir)
    os.system("mkdir " + outputdir_tmp)

###################################################
## Make subjob directories
###################################################
printedworkdir =  output + "Job_[" + str(1) + "-" + str(number_of_cores) + "]/"
for i in range(1,number_of_cores+1):
    workdir =  output + "Job_" + str(i) + "/"    
    if not (os.path.exists(workdir)):
            os.system("mkdir " + workdir)
            if i==1:
                if DEBUG == "True":
                    print "making sub work directories " + printedworkdir


####################################################
## Creat separate input lists/macros for each subjob
####################################################

### read inputlist.txt which contains all input files
fr = open(local_sub_dir + '/inputlist.txt', 'r')

outsamplename = sample
if runnp == "True":
    outsamplename = "nonprompt_" + outsamplename
    print "sample --> " + outsamplename
if runcf == "True":
    outsamplename = "chargeflip_" + outsamplename
    print "sample --> " + outsamplename
if not mc:
    outsamplename = outsamplename +  "_" + new_channel
    outsamplename = outsamplename + "_5_3_20"
else:
    outsamplename = outsamplename + "_5_3_20"

        
### specify the location of the macro for the subjob     
printedrunscript = output+ "Job_[1-" + str(number_of_cores)  + "]/runJob_[1-" + str(number_of_cores)  + "].C"

for line in fr:
    if nfiles < files_torun:
        if nfiles == 0 :
            runscript = output+ "Job_" + str(count) + "/runJob_" + str(count) + ".C"
            filelist = output+ "Job_" + str(count) + "/" + sample + "_%s" % (count) + ".txt"
            fwrite = open(filelist, 'w')
            configfile=open(runscript,'w')
            configfile.write(makeConfigFile(loglevel, outsamplename, filelist, tree, cycle, count, outputdir_tmp, outputdir, number_of_events_per_job, logstep, skipev, datatype, original_channel, data_lumi, totalev, xsec, tar_lumi, eff_lumi, useskinput, runevent, list_of_extra_lib, runnp,runcf)) #job, input, sample, ver, output
            configfile.close()
            if str(DEBUG) == "True":
                print "Making file : " + printedrunscript
            fwrite.write(line)
            filesprocessed+=1
            nfiles_file+=1            
            nfiles+=1
            if files_torun == 1:
                fwrite.close()
            continue

        #End of file
        if not nfiles % nfilesperjobs:
            if not nfiles == number_of_files :
                # set counters
                nfiles_file=0
                count+=1        
                # close files
                fwrite.close()
                ### Make next set of scripts
                runscript = output+ "Job_" + str(count) + "/runJob_" + str(count) + ".C"
                filelist = output+ "Job_" + str(count) + "/" + sample + "_%s" % (count) + ".txt"
                fwrite = open(filelist, 'w')
                configfile=open(runscript,'w')
                configfile.write(makeConfigFile(loglevel,outsamplename, filelist, tree, cycle, count, outputdir_tmp,outputdir, number_of_events_per_job, logstep, skipev, datatype , original_channel, data_lumi, totalev, xsec, tar_lumi, eff_lumi, useskinput, runevent,list_of_extra_lib, runnp, runcf))
                configfile.close()
                fwrite.write(line)
                filesprocessed+=1
                nfiles_file+=1
            else:
                fwrite.write(line)
                filesprocessed+=1
                nfiles_file+=1
                if DEBUG == "True":
                    print "File " + filelist + " contains " + str(nfiles_file) + " files"            
                
        else:
            fwrite.write(line)
            filesprocessed+=1
            nfiles_file+=1

        if nfiles == number_of_files-1 :
            fwrite.close()

    else:
        n_remainder_files+=1
        filelist = output+ "Job_" + str(n_remainder_files) + "/" + sample + "_%s" % (n_remainder_files) + ".txt"
        #runscript = output+ "Job_" + str(count) + "/runJob_" + str(count) + ".C"
        fwrite = open(filelist, 'a')
        fwrite.write(line)
        #configfile=open(runscript,'w')
        #configfile.write(makeConfigFile(loglevel,sample, filelist, tree, cycle, count, outputdir_tmp,outputdir, number_of_events_per_job, logstep, skipev, datatype , original_channel, data_lumi, totalev, xsec, tar_lumi, eff_lumi, useskinput, runevent,list_of_extra_lib, runnp, runcf))
        #configfile.close()
        filesprocessed+=1
        fwrite.close()        
    nfiles+=1        
fr.close()

#################################################################### 
### Check Final input files have no duplicates
#################################################################### 
no_duplicate=False
for check in range(1, number_of_cores+1):
    filelist = output+ "Job_" + str(check) + "/" + sample + "_%s" % (check) + ".txt"
    fcheck = open(filelist, 'r')
    nsamples=0
    for line in fcheck:
        nsamples+=1
        total_nsamples+=1
        no_duplicate= True
        for s in check_array:
            if s == line :
                print "DUPLICATE file : " + s
                no_duplicate=False
                sys.exit()
        check_array.append(line)
    if DEBUG == "True":
        print  "File " + filelist + " contains " + str(nsamples) + " files"
    fcheck.close()
if DEBUG == "True":
    print "Total Number of input files = " + str(total_nsamples)     

if no_duplicate:
    #print "Checking for duplicates: "
    #print "Checking for duplicates:...... "
    if DEBUG == "True":
        print "Checking for duplicates: NONE found"
else:
     #print "Checking for duplicates: "
     #print "Checking for duplicates:...... "
     print "Checking for duplicates: Duplicate files found. Check script "
            
if DEBUG == "True":
    print "Total number of files processed = " + str(filesprocessed)

###################################################
### Run each .C file in background
###################################################
import thread,time
start_time = time.time()

wait_sub = 1

if number_of_cores < 10:
    wait_sub = 5

if DEBUG == "True":
    print "Running LQAnalyzer jobs for: " + getpass.getuser()
array_batchjobs = []
for i in range(1,number_of_cores+1):

    batchscript =  output+ "Job_" + str(i) + "/runJob_" + str(i) + ".sh"
    batchfile=open(batchscript,'w')
    batchfile.write(make_batch_script(output+ "Job_" + str(i) , outsamplename+ "_Job_" + str(i),str(os.getenv("LQANALYZER_DIR")),"runJob_" + str(i) + ".C"))
    batchfile.close()
    os.chmod(batchscript,0775)

    script = output+ "Job_" + str(i) + "/runJob_" + str(i) + ".C"
    log = output+ "Job_" + str(i) + "/runJob_" + str(i) + ".log"
    logbatch = output+ "Job_" + str(i) + "/"+outsamplename+"_Job_" + str(i) + ".out"
    
    runcommand = "nohup root.exe -l -q -b " +  script + "&>" + log + "&"
    if running_batch:
        if queue == "":
            runcommand = "qsub -V " + batchscript   + "&>" + log
        else:
            runcommand = "qsub " + queue_command +" -V " + batchscript   + "&>" + log


    
    jobID=0
    
    if singlejob:
        print "Running single job " + script 
        runcommand = "root.exe -l -q -b " +  script 
        os.system(runcommand)
    else:
        if i==1:
            if running_batch:
                print "Running " + script + " . Log file --->  " + logbatch
            else:
                print "Running " + script + " . Log file --->  " + log 
        elif i== number_of_cores:
            if running_batch:
                print "Running " + script + " . Log file --->  " + logbatch
            else:
                print "Running " + script + " . Log file --->  " + log
        elif i==2:
            print "......"
        if not running_batch:
            os.system(runcommand)

if running_batch: 
    with open(output+"condor.jds","w") as f:
        f.write('''
Index = $(Process)+1
executable = Job_$INT(Index)/runJob_$INT(Index).sh
output = Job_$INT(Index)/{0}_Job_$INT(Index).out
error = Job_$INT(Index)/{0}_Job_$INT(Index).err
log = condor.log
getenv = True
queue {1}
'''.format(outsamplename,str(number_of_cores)))

    clusterid=os.popen("cd "+output+"; condor_submit condor.jds -batch-name "+outsamplename+" |grep -o 'cluster [0-9]*'|grep -o '[0-9]*'").read().strip()

    k_batch_script =  output+ "JobKill.sh"
    with open(k_batch_script,'w') as f:
        f.write("condor_rm "+clusterid)
    array_batchjobs=[clusterid+"."+x for x in os.popen("condor_q "+clusterid+" -af procid").read().split()]

    print "@@@@@@@@@@@@@@@@@@@@@@@@@"
    for ijob in array_batchjobs:
        print "Job ["+str(ijob)+"] added to list......."
    print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    print "In case user wants to kill job do : source " + output+ "JobKill.sh"
    print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

##########################################################
## wait and do merging (also remove old log file/rootfiles
##########################################################
#check_log= os.getenv("LQANALYZER_LOG_PATH") + "/" + outsamplename + "/runJob_1.log"
check_log= os.getenv("LQANALYZER_LOG_PATH") + "/" + outsamplename + "/runJob_1.log"
if (os.path.exists(check_log)):
    os.system("rm " + os.getenv("LQANALYZER_LOG_PATH") + "/" + outsamplename + "/*.log")

if DEBUG == "True":
    print "Waiting for all jobs to finish before Merging."

ncomplete_files=0
JobSuccess=False
JobOutput=True
CompletedJobs=[]
doMerge=False

print "Checking Job status:"

if singlejob:    
    check_outfile = outputdir + outsamplename +  "_1.root"
    if (os.path.exists(check_outfile)):
        JobSuccess=True;
else:        
    if running_batch :
        sys.stdout.write('\r'+ 'Submitting jobs to batch queue...')
        sys.stdout.flush()
    else:
        sys.stdout.write('\r'+ '0% of events processed...' )
        sys.stdout.flush()
low_cpu=0
ncycle=0
file_iterator=0
files_done= []
clear_line='                                                                          '
failed_macro=""
failed_log=""
print ""
while not JobSuccess:
    
    if running_batch == False:
        os.system("ps ux &> " + local_sub_dir + "/log")
        filename = local_sub_dir +'/log'
    running = False
    
    if running_batch == False:

        for line in open(filename, 'r'):
            if "root.exe" in line:
                running = True            
                splitline  = line.split()
                if splitline[2] < 0.1:
                    low_cpu+=1
        if low_cpu > 3:
            running = False

    else:
        array_unfinished=[clusterid+"."+x for x in os.popen("condor_q "+clusterid+" -af procid").read().split()]
        array_running=[clusterid+"."+x for x in os.popen("condor_q "+clusterid+" -run -af procid").read().split()]
        array_hold=[clusterid+"."+x for x in os.popen("condor_q "+clusterid+" -hold -af procid").read().split()]
        running = True
        if len(array_unfinished) == 0:
            running = False
        if len(array_hold) > 0 :
            print "Job " + ", ".join(array_hold) + " is in held state: killing all jobs"
            os.system("source " + output+ "JobKill.sh")
            running = False

    if not running:
        check_outfile = outputdir + outsamplename +  "_1.root"
        if not (os.path.exists(check_outfile)):
            JobSuccess=True
            JobOutput=False
            
    for i in range(1,number_of_cores+1):
        skipcheck=False
        for check in CompletedJobs:
            if i== check: skipcheck=True
        while not skipcheck:
            skipcheck=True
            check_outfile = outputdir + outsamplename +  "_" +  str(i) + ".root"   
            if (os.path.exists(check_outfile)):
                CompletedJobs.append(i)
                ncomplete_files+=1
                files_done.append("Job [" + str(i) + "] completed. Output ="  + check_outfile)
            
    if ncomplete_files== number_of_cores :
        sys.stdout.write('\r' + clear_line)
        sys.stdout.flush()
        sys.stdout.write('\r'+ '100% of events processed. \n' )
        sys.stdout.flush()
        print "Job finished"
        doMerge=True
        if ncycle == 0:
            print "Job ran in less than 10 seconds. Assumed bug:"
            if number_of_cores == 1:
                JobOutput=True
            else:
                JobOutput=False
        JobSuccess=True
                                    
    else:
        nevents_total=0.
        nevent_processed=0.

        if running_batch:
            ### print jobs running/in queue .... once all running print % completeion
            sys.stdout.write('\r' + clear_line)
            sys.stdout.flush()
            sys.stdout.write('\r'+ 'Current jobs running : [' + str(number_of_cores) + '/' + str(number_of_cores) + ']... ')
            sys.stdout.flush()
            time.sleep(30)
            #### check job is running. Halted or suspended and if not running is output file missing?
            for i in range(1,number_of_cores+1):
                if not JobOutput:
                    break
                job_id_c=array_batchjobs[i-1]
                job_finished=True
                if job_id_c in array_unfinished:
                    job_finished=False
                                
                if job_finished:
                    ### job id not in qstat output. Check if rootfile is missing. If so kill job
                    check_outfile = outputdir + outsamplename +  "_" + str(i)+".root"
                    if not (os.path.exists(check_outfile)):
                        failed_macro= output+ "Job_" + str(i) + "/runJob_" + str(i) + ".C"
                        failed_log= "runJob_" + str(i) + "log"
                        JobSuccess=True
                        JobOutput=False
                        print "Job " + str(job_id_c) + " is not running or in queue. Output " + str(check_outfile)+ " is missing."
                        print "Most likely a crash occurred.  So killing all jobs." 
                        os.system("source " + output+ "JobKill.sh")

                        check_error_outfile = output + "/Job" +  "_" +  str(i) + "/"+ outsamplename+ "_Job_"+ str(i) +".err"
                        print "Error file for job ["+str(job_id_c)+"] shows:"
                        for line in open(check_error_outfile, 'r'):
                            print line
                        print "Run in non-batch mode by setting njobs = 1 in submit.sh file and retry" 

            
        ##### Run over log to get % completion                    
        for i in range(1,number_of_cores+1):
            check_outfile = output + "/Job" +  "_" +  str(i) + "/runJob_"+ str(i) +".log"
            if running_batch == True:
                check_outfile = output + "/Job" +  "_" +  str(i) + "/" + outsamplename + "_Job_"+ str(i) +".out"
            nevent_processed_i=0.
            nevents_total_i=0.
            line=os.popen('tail -100 ' + check_outfile +'|grep "Processing entry"|grep -v LQCycleController|tail -n1').read().strip()
            entries = line.split()
            if len(entries)> 6:                        
                num = entries[7]
                s = num.replace("/", " ")
                event_split = s.split()
                nevent_processed_i = float(event_split[0])
                nevents_total_i= float(event_split[1])
            nevent_processed+=nevent_processed_i                
            nevents_total+=nevents_total_i

        ## calculate time left to run jobs    
        end_time = time.time()
        remaining = (end_time - start_time)
        if nevent_processed !=0:
            remaining*= (1./nevent_processed)
            remaining*= ( nevents_total  - nevent_processed)
            b = str(round(float(100.*nevent_processed/nevents_total), 2)) + "% of events processed. Estimated cpu time remaining =  " + str(round(remaining,2)) + "[s]" 
            sys.stdout.write('\r' + clear_line)
            sys.stdout.flush()
            sys.stdout.write('\r'+b)            
            sys.stdout.flush()
        else:
            mess="Job Initialising 0% of events processed."
            if JobOutput:
                sys.stdout.write('\r' + clear_line)
                sys.stdout.flush()
                sys.stdout.write('\r'+mess)
                sys.stdout.flush()
                time.sleep(2.)
        if ncomplete_files > file_iterator:
            #print str(ncomplete_files) + "/" + str(number_of_cores) + " jobs completed.  " #Wait " + str(timeWait) + " second..."
            #print ""
            file_iterator=ncomplete_files
        time.sleep(30)
        ncycle+=1
     


if not JobOutput:

    if not running_batch:
        failed_macro= output+ "Job_1/runJob_1.C"
        failed_log= "runJob_1.log"

    print ""
    print "Job Failed...."
    if not os.path.exists(os.getenv("LQANALYZER_LOG_PATH")+ "/" + outsamplename):
        os.system("mkdir -p " + os.getenv("LQANALYZER_LOG_PATH")+ "/" + outsamplename)
        
    if not number_of_cores == 1:
        os.system("mv "+ output + "/*/*.o* " + os.getenv("LQANALYZER_LOG_PATH") + "/" + outsamplename)    
    print "###########################################################################################################"
    print "Check crash by running root -q -b " + failed_macro 
    print "Logfile of failed job is can be found at " + os.getenv("LQANALYZER_LOG_PATH") + "/" + outsamplename   + failed_log 
    print "###########################################################################################################"
    #os.system("rm -r " + output)    
    #os.system("rm -r " + local_sub_dir)    
    #os.system("rm -r " + timestamp_dir)
    
else:

    for line in files_done:
        if DEBUG == "True":
            print line


    SKTreeOutput = "/data7/DATA/LocalNtuples/SKTrees8TeV/Tag27_CMSSW_5_3_20/SKTrees/"
   
    #do not merge the output when using tree maker code
    if str(cycle) == "SKTreeMaker":
        if not os.path.exists(SKTreeOutput):
            os.system("mkdir  " + SKTreeOutput)
        doMerge=False
        if not mc:
            Finaloutputdir = SKTreeOutput + "Data/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
                
            if str(original_channel) =="egamma":
                Finaloutputdir += "DoubleElectron/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="muon":
                Finaloutputdir += "DoubleMuon/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="emu":
                Finaloutputdir += "ElectronMuon/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="singlemuon":
                Finaloutputdir += "SingleMuon/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="singlemuon_chs":
                Finaloutputdir += "SingleMuonCHS/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)

            if str(original_channel) =="singleelectron":
                Finaloutputdir += "SingleElectron/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="singleelectron_chs":
                Finaloutputdir += "SingleElectronCHS/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="muon_lowpt":
                Finaloutputdir += "DoubleMuParked/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)


            Finaloutputdir += "period" + original_sample + "/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
        else:
            Finaloutputdir = SKTreeOutput + "MC/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
                                                                                            
            Finaloutputdir +=  original_sample + "/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
                
    if cycle == "SKTreeMakerNoCut":
        doMerge=False
        if not os.path.exists(SKTreeOutput):
            os.system("mkdir " + SKTreeOutput)
        if not mc:
            Finaloutputdir = SKTreeOutput + "DataNoCut/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="egamma":
                Finaloutputdir += "DoubleElectron/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="muon":
                Finaloutputdir += "DoubleMuon/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="emu":
                Finaloutputdir += "ElectronMuon/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
            Finaloutputdir += "period" + original_sample + "/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="muon_lowpt":
                Finaloutputdir += "DoubleMuParked/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
        else:
            Finaloutputdir = SKTreeOutput + "MCNoCut/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
            Finaloutputdir += original_sample + "/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)

    if cycle == "SKTreeMakerDiLep":
        doMerge=False
        if not os.path.exists(SKTreeOutput):
            os.system("mkdir " + SKTreeOutput)
        if not mc:
            Finaloutputdir = SKTreeOutput + "DataDiLep1510/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="egamma":
                Finaloutputdir += "DoubleElectron/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="muon":
                Finaloutputdir += "DoubleMuon/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            if str(original_channel) =="emu":
                Finaloutputdir += "ElectronMuon/"
                if not os.path.exists(Finaloutputdir):
                    os.system("mkdir " + Finaloutputdir)
            Finaloutputdir += "period" + original_sample + "/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
        else:
            Finaloutputdir = SKTreeOutput + "MCDiLep1510/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
            Finaloutputdir +=  original_sample + "/"
            if not os.path.exists(Finaloutputdir):
                os.system("mkdir " + Finaloutputdir)
                
    if not os.path.exists(Finaloutputdir):
        os.system("mkdir " + Finaloutputdir)
    outfile = cycle + "_" + filechannel + outsamplename + ".root"
    if doMerge:
        if not mc:
            outfile = cycle + "_" + outsamplename + ".root"
        if os.path.exists(Finaloutputdir + outfile):
            os.system("rm  "  +  Finaloutputdir + "/"  + outfile)
        os.system("hadd " + Finaloutputdir +  outfile  + " "+ outputdir + "*.root")
        print "Merged output :" + Finaloutputdir + outfile
    else:
        if not mc:
            outfile = cycle + "_" + outsamplename + ".root"
        if number_of_cores == 1:
            os.system("rm " + Finaloutputdir + "/" +outfile)
            os.system("mv " + outputdir + outsamplename + "_1.root " + Finaloutputdir + outfile )
        else:
            if  "SKTreeMaker" in cycle:
                os.system("rm -r " + Finaloutputdir)
                os.system("mkdir " + Finaloutputdir)

            os.system("mv " + outputdir + "*.root " + Finaloutputdir )

            
        if DEBUG == "True":
            print "Non merged output :" +Finaloutputdir

    if remove_workspace == "True":
        if not os.path.exists(os.getenv("LQANALYZER_LOG_PATH")+ "/" + outsamplename):
            os.system("mkdir -p " + os.getenv("LQANALYZER_LOG_PATH")+ "/" + outsamplename)
        
        if not number_of_cores == 1:    
            os.system("mv "+ output + "/*/*.out " + os.getenv("LQANALYZER_LOG_PATH") + "/" + outsamplename)
        os.system("rm -r " + output)
        os.system("rm -r " + local_sub_dir)
        os.system("rm -r " + timestamp_dir)
                
        print "Log files are sent to  --> "  + os.getenv("LQANALYZER_LOG_PATH")+ "/" + outsamplename
        if doMerge:
            print "All sampless finished: OutFile:"  + cycle + "_" + filechannel + outsamplename + ".root -->" + Finaloutputdir
        else:
            if number_of_cores == 1:
                print "All sampless finished: OutFiles "+ outsamplename + "_1.root -->" + Finaloutputdir + outfile
            else:
                print "All sampless finished: OutFiles "+ outsamplename + "*.root -->" + Finaloutputdir
            
    else:
        print "TMP directory " + output + "is not removed. "
        os.system("rm -r " + local_sub_dir)
        
if os.path.exists(local_sub_dir):
    os.system("rm -r " + local_sub_dir)
    os.system("rm -r " + timestamp_dir)
        

end_time = time.time()
total_time=end_time- start_time
print "Using " + str(number_of_cores) + " cores: Job time = " + str(total_time) +  " s"
print ""
