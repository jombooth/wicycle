#!/usr/bin/env bash

sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to 127.0.0.1:80
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to 127.0.0.1:80

sudo sysctl -w net.ipv4.conf.wlan0.route_localnet=1

