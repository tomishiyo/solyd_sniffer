import socket

from epackages import EthernetPacket, IpV4Packet


def main():
    agent = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, source = agent.recvfrom(65535)
        packet = EthernetPacket(raw_data)
        ipv4packet = IpV4Packet(packet)

        print(f'Source MAC {packet.src_mac}')
        print(f'Destination MAC {packet.dst_mac}')
        print(f'Ethernet type:{packet.type}')
        print(ipv4packet.ip_dst)
        print(ipv4packet.data)


if __name__ == '__main__':
    main()

