#!/usr/bin/env bash

PATH=/home/asd/.local/bin:/home/asd/go/bin:/usr/bin/vendor_perl:/usr/local/bin:/usr/bin

selected_entered=`cd ~/Dropbox/; find . -maxdepth 2 -not -name '.*' | grep -v index.md | cut -c 3- | sed 's/\.md$//' | sort | rofi -p asddoc: -dmenu -format 's F'`
[[ $? != 0 ]] && exit
read -r selected entered <<< $selected_entered
entered=$(echo $entered | tr -d "'") # убрать кавычки

re_lastspace='\s$'
if [[ $entered =~ $re_lastspace ]] # если последний символ пробел, то создать новую страницу
then
    asddoc $entered
else
    asddoc $selected
fi
