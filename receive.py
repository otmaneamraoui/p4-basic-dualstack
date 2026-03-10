#!/usr/bin/env python3
import os
import sys

from scapy.all import IP, IPv6, TCP, sniff


def handle_pkt(pkt):
    if TCP in pkt and pkt[TCP].dport == 1234:
        if IP in pkt:
            print("got an IPv4 packet")
        elif IPv6 in pkt:
            print("got an IPv6 packet")
        else:
            return

        pkt.show2()
        sys.stdout.flush()


def main():
    ifaces = [i for i in os.listdir('/sys/class/net/') if 'eth' in i]
    iface = ifaces[0]
    print(f"sniffing on {iface}")
    sys.stdout.flush()

    sniff(iface=iface, prn=lambda x: handle_pkt(x))


if __name__ == "__main__":
    main()
