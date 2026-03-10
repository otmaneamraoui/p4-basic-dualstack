#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-only
import random
import sys

from scapy.all import Ether, IPv6, TCP, get_if_hwaddr, get_if_list, sendp


def get_if():
    iface = None
    for i in get_if_list():
        if "eth0" in i:
            iface = i
            break
    if iface is None:
        print("Cannot find eth0 interface")
        sys.exit(1)
    return iface


def main():
    if len(sys.argv) < 3:
        print('Usage: ./send_ipv6.py <destination-ipv6> "<message>"')
        sys.exit(1)

    addr = sys.argv[1]
    iface = get_if()

    print(f"sending on interface {iface} to {addr}")
    pkt = Ether(src=get_if_hwaddr(iface), dst="ff:ff:ff:ff:ff:ff")
    pkt = pkt / IPv6(dst=addr) / TCP(
        dport=1234,
        sport=random.randint(49152, 65535)
    ) / sys.argv[2]

    pkt.show2()
    sendp(pkt, iface=iface, verbose=False)


if __name__ == "__main__":
    main()
