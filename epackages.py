import struct
import socket


def translate_mac_data(field):
    return ":".join(map("{:02x}".format, field)).upper()


def translate_ip_header(data):
    header = struct.unpack('!BBHHHBBH4s4s', data[:20])
    return header


class EthernetPacket:
    def __init__(self, raw_data):
        dst_mac, src_mac, self.type = struct.unpack('! 6s 6s H', raw_data[0:14])

        self.dst_mac = translate_mac_data(dst_mac)
        self.src_mac = translate_mac_data(src_mac)
        self.data = raw_data[14:]


class IpV4Packet:
    def __init__(self, eth_packet):
        header = translate_ip_header(eth_packet.data)
        self.ip_version = header[0] >> 4
        self.ttl = header[5]
        self.proto = header[6]
        self.ip_src = socket.inet_ntoa(header[8])
        self.ip_dst = socket.inet_ntoa(header[9])
        self.data = eth_packet.data[20:].decode('latin-1')







