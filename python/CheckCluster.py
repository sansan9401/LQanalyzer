import os,sys,getpass

if not os.path.exists("/data7/DATA/LQAnalyzer_rootfiles_for_analysis/CATAnalyzerStatistics/" + getpass.getuser()):
    os.system("mkdir  /data7/DATA/LQAnalyzer_rootfiles_for_analysis/CATAnalyzerStatistics/" + getpass.getuser())

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-x", "--x", dest="x", default="123",help="tag")

(options, args) = parser.parse_args()
filetag=options.x
    
path_job="/data7/DATA/LQAnalyzer_rootfiles_for_analysis/CATAnalyzerStatistics/" + getpass.getuser() + "/Cluster_" + filetag + ".txt"


file_job=open(path_job,"w")

njobs=int(os.popen("condor_q -al -af requestcpus|paste -sd+|bc").read().strip() or 0)
njobs_1=0
njobs_2=0
njobs_3=0
njobs_4=0
njobs_5=0
njobs_6=0
njobs_user=int(os.popen("condor_q -af requestcpus|paste -sd+|bc").read().strip() or 0)
njobs_error=0
njobs_held=int(os.popen("condor_q -al -hold -af requestcpus|paste -sd+|bc").read().strip() or 0)

file_job.write(getpass.getuser() + " njobs= " + str(njobs_user) + " njobs_1= " + str(njobs_1) + " njobs_2= " + str(njobs_2) + " njobs_3= " + str(njobs_3) + " njobs_4= " + str(njobs_4) + " njobs_5= " + str(njobs_5) + " njobs_6= " + str(njobs_6) + " error_jobs= " + str(njobs_error) + " held_jobs=  " + str(njobs_held) + "  total_jobs= " + str(njobs) + " \n")
file_job.close()
