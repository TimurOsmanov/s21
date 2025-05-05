ip1: str = '178.101.89.7'
ip2: str = '201.57.153.161'

for ip in (ip1, ip2):
    ip_list: list =[f'{int(x):08b}' for x  in ip.split('.')]
    print('with dots:', '.'.join(ip_list))
    print('without dots:', ''.join(ip_list))

