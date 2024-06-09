#!/bin/bash
# generate HTML from markdown,
#  then replace all lines between START_CONTENT and END_CONTENT with this HTML
#  in the file INDEX_FILE
# usage:
#  ./build.sh content.md

if [ -z $1 ]; then
  echo "need file to transform"
  echo "usage: ./build.sh content.md"
  exit 1
fi

INDEX_FILE="index.html"
TEMP_FILE="index.html.temp"
START_CONTENT="<!-- !!start content!! -->"
END_CONTENT="<!-- !!end content!! -->"

original_html=$(cat $INDEX_FILE)

html=$(marked -i $1)

# get line numbers of START_CONTENT and END_CONTENT
start=$(echo "${original_html}" | grep -n "${START_CONTENT}" | cut -d : -f1)
end=$(echo "${original_html}" | grep -n "${END_CONTENT}" | cut -d : -f1)

if [ -z $start ] || [ -z $end ]; then
  echo "could not find start/end content tags"
  echo "start: <$start>, end: <$end>"
  exit 1
fi

rm -f $TEMP_FILE
echo "${original_html}" | awk 'NR <= '"${start}"'' >> $TEMP_FILE
echo "${html}" >> $TEMP_FILE
echo "${original_html}" | awk 'NR >= '"${end}"'' >> $TEMP_FILE

cat $TEMP_FILE > $INDEX_FILE
rm -f $TEMP_FILE
