#!/bin/bash

rule1=$1
rule2=$2

curl -X DELETE -d '{"rule_id":"'$rule1'"}' http://localhost:8080/firewall/rules/0000000000000001

printf "\n"

curl -X DELETE -d '{"rule_id":"'$rule2'"}' http://localhost:8080/firewall/rules/0000000000000001

printf "\n"
