#! /bin/sh
# $Id: setup.sh 1 01/12/2013 jalmond $
###################################################################################
# @Project: LQAnalyzer/SKTree - ROOT-based analysis framework for Korea CMS group #
#                                                                                 #
# @author John Almond       <jalmond@cern.ch>           - SNU                     #
#                                                                                 #
# Script that has to be sourced before compiling/running SFrame.                  #
#                                                                                 #
##################################################################################

# Greet the user

echo "Setting up environment for compiling/running CATAnalzer with SKTree"

export SKFLATVERSION="v9-4-9v2"


source bin/setup_timezone.sh

if [ $LQANALYZER_DIR ]; then
    echo LQANALYZER_DIR is already defined, use a clean shell
    return 1
fi


###  setup any user aliases
source bin/setup_user.sh

##### setup root enviroment
export sktreemaker_version="False"
if [[ $1 == "sktreemaker" ]];
then
    export sktreemaker_version="True"
fi
source bin/setup_root.sh $sktreemaker_version

# speficy the LQANALYZER_DIR base directory, i.e., the directory in which this file lives
export LQANALYZER_DIR=${PWD}

#### admin setup for analyzer
source bin/setup_admin.sh

python ${LQANALYZER_DIR}/scripts/CheckEmailIsSetup.py
cat_email="NULL"
while read line
do
    prefix="email = "
    if [[ $line == $prefix* ]];
    then
        line=${line:${#prefix}}
        cat_email=$line
    fi
done < ${LQANALYZER_DIR}/bin/catconfig
if [[ $cat_email  == "NULL" ]];
then
    echo "Email not setup. run setup.sh again"
    export LQANALYZER_DIR=""
    return 1
fi

###  print git tag info
source bin/check_tag.sh

##### setup CMSSW version of analyzer
export yeartag="80X/"

### setup alias for using analyzer

if [[ $sktreemaker_version  == "False" ]];
then
    alias make_80x_fullclean="make distclean -f ${LQANALYZER_DIR}/bin/Make/Makefile80X"
    alias make_80x_clean="make clean -f ${LQANALYZER_DIR}/bin/Make/Makefile80X"
    alias make_80x="make -f ${LQANALYZER_DIR}/bin/Make/Makefile80X"
    alias make_94x_fullclean="make distclean -f ${LQANALYZER_DIR}/bin/Make/Makefile94X"
    alias make_94x_clean="make clean -f ${LQANALYZER_DIR}/bin/Make/Makefile94X"
    alias make_94x="make -f ${LQANALYZER_DIR}/bin/Make/Makefile94X"
else
    
    alias make_80x_fullclean="make distclean -f ${LQANALYZER_DIR}/bin/Make/Makefile80X_root5"
    alias make_80x_clean="make clean -f ${LQANALYZER_DIR}/bin/Make/Makefile80X_root5"
    alias make_80x="make -f ${LQANALYZER_DIR}/bin/Make/Makefile80X_root5"
    alias make_94x_fullclean="make distclean -f ${LQANALYZER_DIR}/bin/Make/Makefile94X_root5"
    alias make_94x_clean="make clean -f ${LQANALYZER_DIR}/bin/Make/Makefile94X_root5"
    alias make_94x="make -f ${LQANALYZER_DIR}/bin/Make/Makefile94X_root5"
fi


alias cathistcounter="source scripts/Counter.sh "
alias catcutflowcounter="source scripts/CutFlow.sh "
alias sktree_80X="bash submitSKTree80X.sh"
alias sktree_94X="bash submitSKTree94X.sh"
alias sktreemaker_80X="bash submitSKTree80X.sh -M True "
alias sktreemaker_90X="bash submitSKTree94X.sh -M True "
alias sktree_val="bash submitSKTree.sh -V True "
alias sktree_bkg="nohup bash submitSKTree.sh -b True "
alias new_git_tag="bash "$LQANALYZER_DIR"/scripts/setup/git_newtag.sh"
alias git_commit_lq="bash scripts/setup/git_commit.sh"
alias sktree_bkg_log="python python/PrintBkgJob.py"

#### make all env variables used in alayzer
source bin/setup_analysis_aliases.sh
#### setup lib dir for new user/tag
source bin/setup_lib.sh

### Load cleaup functions
source ${LQANALYZER_BIN_PATH}/cleanup.sh 

### setup workspace
python ${LQANALYZER_DIR}/python/SetUpWorkSpace.py
### make backup for important files
python ${LQANALYZER_DIR}/python/BackUpDirectory.py
### setup email list 
python ${LQANALYZER_DIR}/python/SetupEmailList.py


if [ -z ${ROOTSYS} ] ; then
    echo "Warning: ROOT environment doesn't seem to be configured!"
    echo "Add these lines to your ~/.bashrc file to remove this warning in future."
    echo ""
    echo "source /usr/local/bin/thisroot.sh"
    echo ""
    export ROOTSYS=/usr/local
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ROOTSYS/lib/root:
    if [ -z ${ROOTSYS} ] ; then
	echo "Error: ROOT environment cannot be configured!"
    else echo "Setup root enviroment for user."
    fi
fi

export LD_TMP_LIBRARY_PATH=${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=${LQANALYZER_LIB_PATH}:${LD_LIBRARY_PATH}

export PATH=${LQANALYZER_BIN_PATH}:${PATH}
export PYTHONPATH=${LQANALYZER_DIR}/python:${PYTHONPATH}
export PAR_PATH=./:${LQANALYZER_LIB_PATH}


python ${LQANALYZER_DIR}/python/local_check.py

if [ ! -d ${LQANALYZER_LOG_PATH} ]; then
    echo Directory ${LQANALYZER_LOG_PATH} does not exist ... creating it
    mkdir ${LQANALYZER_LOG_PATH}
fi

echo "Running analysis from" $HOSTNAME " in directory: " $PWD