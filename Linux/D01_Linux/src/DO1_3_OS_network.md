## 1. Set the machine name as user-1: 
1. sudo hostnamectl set-hostname user-1

## 2. Set the time zone corresponding to your current location: 
1. timedatectl set-timezone Europe/Moscow

## 3. Output the names of the network interfaces using a console command:
1. ip link show

2. lo interface - Интерфейс Loopback (он же интерфейс обратной петли) - это виртуальный сетевой интерфейс, который используется для  
тестирования и управления сетевым оборудованием, а также в 
качестве источника адреса для некоторых сетевых протоколов.

## 4. Use the console command to get the ip address of the device you are working on from the DHCP server.
1. ip r

2. В VirtualBox сетевая настройка NAT по умолчанию использует 10.0.2.2 
в качестве IP-адреса хоста и 10.0.2.x (где 2<"x"<255) для IP-адресов виртуальных машин. Таким образом, 
всякий раз, когда запускаются виртуальные, можено использовать 10.0.2.2 
для обозначения «моя машина».

## 5.Define and display the external ip address of the gateway (ip) and the internal IP address of the gateway, aka default ip address (gw).

1. the external ip address of the gateway 
curl ifconfig.co 
83.221.16.202

2. default ip address (gw)
hostname -I
10.0.2.15

## 6. Set static (manually set, not received from DHCP server) ip, gw, dns settings (use public DNS servers, e.g. 1.1.1.1 or 8.8.8.8).

1. Make a copy of the existing 00-installer-config.yaml file before making any changes. 
sudo cp /etc/netplan/00-installer-config.yaml /etc/netplan/00-installer-config.yaml.bak

2. edit config 
sudo nano /etc/netplan/00-installer-config.yaml

```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: false
      dhcp6: false
      addresses: 
        - 10.0.2.20/24
      gateway4: 10.0.2.2
      nameservers:
        addresses: [1.1.1.1, 8.8.8.8]
```

3. выключить ipv6
   1. sudo nano /etc/sysctl.d/99-sysctl.conf

   2. добавить
        1. net.ipv6.conf.all.disable_ipv6 = 1
        2. net.ipv6.conf.default.disable_ipv6 = 1

   3. проверить sudo sysctl -p
