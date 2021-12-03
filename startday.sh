#! /bin/bash
# inits a day

TEMPLATE_FILEPATH="base/_template.py"

if [ -z $1 ]; then
  echo "ERR: Please provide a day number to initialize the directoy."
  exit 1
fi

DAY_NR=$1
DIR_NAME="day${DAY_NR}"

echo "___ Initialising day '$DAY_NR'"
echo "___ Checking if '${DIR_NAME}' directory exists"

if ! [ -d $DIR_NAME ]; then
  mkdir $DIR_NAME
  echo "___ Copying template into the directory '${DIR_NAME}' "
  cp $TEMPLATE_FILEPATH   ${DIR_NAME}/${DIR_NAME}.py
  sed -i '' s/##DAY##/$DAY_NR/g   ${DIR_NAME}/${DIR_NAME}.py

  echo "___ Executing the new '${DIR_NAME}/${DIR_NAME}.py' for the first time (downloads inputs)"
  (cd $DIR_NAME && python ${DIR_NAME}.py)
fi

echo "___ Done."
