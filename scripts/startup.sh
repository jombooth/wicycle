#!/usr/bin/env bash
# run with root level privileges

# reroute all incoming requests to localhost:

sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to 127.0.0.1:80
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to 127.0.0.1:80

# allow outgoing traffic from localhost by sysctl:

sudo sysctl -w net.ipv4.conf.wlan0.route_localnet=1
