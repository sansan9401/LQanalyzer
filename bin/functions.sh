#!/bin/sh

function makeParseVariable() {
    if ! [ -z ${2} ] 
        then
        local myresult="-"${1}" "${2}
        echo "${myresult}"
    fi
}

function checkDir() {
    ls ${1} > /dev/null
    if [ $? -ne 0 ]
        then
        echo "ERROR:   "${1}" not found!"
    fi
}

function checkAndMakeDir() {
    echo -ne "Checking for directory "${1}
    ls ${1} > /dev/null
    if [ $? -ne 0 ]
        then
        mkdir ${1}
        echo "Made directory "${1}
        echo ""
    else
        echo "... found."
    fi  
}

function setupLQanalyzer() {
    if [ -z "$LQANALYZER_DIR" ]; then
	cd ../
	source setup.sh
	cd -
    fi
}