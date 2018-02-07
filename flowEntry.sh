curl -X PUT http://localhost:8080/firewall/module/enable/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.1","nw_dst": "192.168.0.2"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.1","nw_dst": "192.168.0.3"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.1","nw_dst": "192.168.0.4"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.2","nw_dst": "192.168.0.3"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.2","nw_dst": "192.168.0.4"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.3","nw_dst": "192.168.0.4"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.2","nw_dst": "192.168.0.1"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.3","nw_dst": "192.168.0.1"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.4","nw_dst": "192.168.0.1"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.3","nw_dst": "192.168.0.2"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.4","nw_dst": "192.168.0.2"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "192.168.0.4","nw_dst": "192.168.0.3"}' http://localhost:8080/firewall/rules/0000000000000001
