# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 9:35
# @Author  : shilinw
# @File    : pcapAnalyse.py.py
import scapy
import dpkt
pcap_file = r'F:\py\pcapAnalyse\data\in.pcap'
f = open(pcap_file, 'rb')
udppcap = dpkt.pcap.Reader(f)
i = 0
for ts,buf in udppcap:
   i += 1
   udpdata = dpkt.ethernet.Ethernet(buf)
   data = udpdata.data

#   print(data)
   print(len(data))
   if i == 10:
      break










