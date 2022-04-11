from scapy.utils import rdpcap
from .PtpStream import PtpStream


def PcapToPtpStream(logger, filename):
    return PtpStream(logger, open_pcap_get_ptp(filename))


def open_pcap_get_ptp(filename):
    try:
        pcap = rdpcap(filename)
    except FileNotFoundError:
        print('Provided file is invalid!')
        quit()
    raw_ptp_list = [p for p in pcap if p.haslayer('PTPv2')]
    return raw_ptp_list
