#!/bin/bash

# traverse recursively to get relative paths for all files in the repo
# exclude file patterns via piping to grep -v
# adjust the command below if, for example, the name of your virtual
# environment is not `venv`
readonly FILES="$(find . | grep -v venv | grep -v node_modules | grep -v __pycache__ | grep -v \\.git/ | grep -i -v \\.png | grep -i -v \\.pdf | grep -i -v \\.css | grep -i -v \\.gif | grep -i -v \\.jpg | grep -i -v \\.svg | grep -i -v files\\.sh)"

echo "The following files were updated:" 
for FILE in $FILES
do
    # echo $FILE
    # continue
    if [ ! -d "$PWD/$FILE" ]; then
	# skip running sed on a file that doesn't need it
	if [ ! -n "$(cat $FILE | grep -i getting-started)" ]; then
	    continue
	fi
	echo $FILE
	# use an absolute path here
	sed -i '' "s#/getting-started#/layout#g" "$PWD/$FILE"
    fi
done

echo "The following files still have instances of plot.ly:"

# edit this line too if your virtual environment has a different name
# grep -r go.plot.ly/dash-docs . | grep -v venv/ | grep -v .git/ | grep -v files.sh

echo "If a file shows up above that you would like to change, try
checking if it has accidentally been excluded by the script."
