#!/bin/bash

src=$1
dst=$2
x_frk=$3
x_anc=$4
doFuzzy=$5

if [[ $doFuzzy == true ]]; then
	durasi="$(python -c "import main; main.doFuzzy('$x_frk','$x_anc')")"
else
	durasi=600
fi

echo "Durasi Blokir   : "$durasi" seconds"

curl -s -X POST -d '{"nw_src":"'$src'","nw_dst":"'$dst'","actions":"DENY","priority": "2"}' http://localhost:8080/firewall/rules/0000000000000001
rule1=`curl -s http://localhost:8080/firewall/rules/0000000000000001 | jq ' .[] | .access_control_list | .[] | .rules | max_by(.rule_id) | .rule_id '`

curl -s -X POST -d '{"nw_src":"'$dst'","nw_dst":"'$src'","actions":"DENY","priority": "2"}' http://localhost:8080/firewall/rules/0000000000000001
rule2=`curl -s http://localhost:8080/firewall/rules/0000000000000001 | jq ' .[] | .access_control_list | .[] | .rules | max_by(.rule_id) | .rule_id '`

durasi=$durasi
sleep $durasi
./unblock.sh $rule1 $rule2
