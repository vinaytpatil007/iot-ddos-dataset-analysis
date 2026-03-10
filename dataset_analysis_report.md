# DDoS Dataset Analysis Report

## Dataset: CIC_IOT_Dataset2023
- Path: `D:\ddos dataset\CIC_IOT_Dataset2023`
- Total files: 183
- Total subfolders: 13
- File types:
- .csv: 182
- .docx: 1

### Folder Structure
```text
CIC_IOT_Dataset2023
|-- Benign_Final
|   |-- BenignTraffic.pcap.csv
|   |-- BenignTraffic1.pcap.csv
|   |-- BenignTraffic2.pcap.csv
|   `-- BenignTraffic3.pcap.csv
|-- DDoS-ACK_Fragmentation
|   |-- DDoS-ACK_Fragmentation.pcap.csv
|   |-- DDoS-ACK_Fragmentation1.pcap.csv
|   |-- DDoS-ACK_Fragmentation10.pcap.csv
|   |-- DDoS-ACK_Fragmentation11.pcap.csv
|   |-- DDoS-ACK_Fragmentation12.pcap.csv
|   |-- DDoS-ACK_Fragmentation2.pcap.csv
|   |-- DDoS-ACK_Fragmentation3.pcap.csv
|   |-- DDoS-ACK_Fragmentation4.pcap.csv
|   |-- DDoS-ACK_Fragmentation5.pcap.csv
|   |-- DDoS-ACK_Fragmentation6.pcap.csv
|   |-- DDoS-ACK_Fragmentation7.pcap.csv
|   |-- DDoS-ACK_Fragmentation8.pcap.csv
|   `-- DDoS-ACK_Fragmentation9.pcap.csv
|-- DDoS-HTTP_Flood
|   `-- DDoS-HTTP_Flood-.pcap.csv
|-- DDoS-ICMP_Flood
|   |-- DDoS-ICMP_Flood.pcap.csv
|   |-- DDoS-ICMP_Flood1.pcap.csv
|   |-- DDoS-ICMP_Flood10.pcap.csv
|   |-- DDoS-ICMP_Flood11.pcap.csv
|   |-- DDoS-ICMP_Flood12.pcap.csv
|   |-- DDoS-ICMP_Flood13.pcap.csv
|   |-- DDoS-ICMP_Flood14.pcap.csv
|   |-- DDoS-ICMP_Flood15.pcap.csv
|   |-- DDoS-ICMP_Flood16.pcap.csv
|   |-- DDoS-ICMP_Flood17.pcap.csv
|   |-- DDoS-ICMP_Flood18.pcap.csv
|   |-- DDoS-ICMP_Flood19.pcap.csv
|   |-- DDoS-ICMP_Flood2.pcap.csv
|   |-- DDoS-ICMP_Flood20.pcap.csv
|   |-- DDoS-ICMP_Flood21.pcap.csv
|   |-- DDoS-ICMP_Flood22.pcap.csv
|   |-- DDoS-ICMP_Flood23.pcap.csv
|   |-- DDoS-ICMP_Flood24.pcap.csv
|   |-- DDoS-ICMP_Flood25.pcap.csv
|   |-- DDoS-ICMP_Flood26.pcap.csv
|   |-- DDoS-ICMP_Flood3.pcap.csv
|   |-- DDoS-ICMP_Flood4.pcap.csv
|   |-- DDoS-ICMP_Flood5.pcap.csv
|   |-- DDoS-ICMP_Flood6.pcap.csv
|   |-- DDoS-ICMP_Flood7.pcap.csv
|   |-- DDoS-ICMP_Flood8.pcap.csv
|   `-- DDoS-ICMP_Flood9.pcap.csv
|-- DDoS-ICMP_Fragmentation
|   |-- DDoS-ICMP_Fragmentation.pcap.csv
|   |-- DDoS-ICMP_Fragmentation1.pcap.csv
|   |-- DDoS-ICMP_Fragmentation10.pcap.csv
|   |-- DDoS-ICMP_Fragmentation11.pcap.csv
|   |-- DDoS-ICMP_Fragmentation12.pcap.csv
|   |-- DDoS-ICMP_Fragmentation13.pcap.csv
|   |-- DDoS-ICMP_Fragmentation14.pcap.csv
|   |-- DDoS-ICMP_Fragmentation15.pcap.csv
|   |-- DDoS-ICMP_Fragmentation16.pcap.csv
|   |-- DDoS-ICMP_Fragmentation17.pcap.csv
|   |-- DDoS-ICMP_Fragmentation18.pcap.csv
|   |-- DDoS-ICMP_Fragmentation19.pcap.csv
|   |-- DDoS-ICMP_Fragmentation2.pcap.csv
|   |-- DDoS-ICMP_Fragmentation3.pcap.csv
|   |-- DDoS-ICMP_Fragmentation4.pcap.csv
|   |-- DDoS-ICMP_Fragmentation5.pcap.csv
|   |-- DDoS-ICMP_Fragmentation6.pcap.csv
|   |-- DDoS-ICMP_Fragmentation7.pcap.csv
|   |-- DDoS-ICMP_Fragmentation8.pcap.csv
|   `-- DDoS-ICMP_Fragmentation9.pcap.csv
|-- DDoS-PSHACK_FLOOD
|   |-- DDoS-PSHACK_Flood.pcap.csv
|   |-- DDoS-PSHACK_Flood1.pcap.csv
|   |-- DDoS-PSHACK_Flood10.pcap.csv
|   |-- DDoS-PSHACK_Flood11.pcap.csv
|   |-- DDoS-PSHACK_Flood12.pcap.csv
|   |-- DDoS-PSHACK_Flood13.pcap.csv
|   |-- DDoS-PSHACK_Flood14.pcap.csv
|   |-- DDoS-PSHACK_Flood15.pcap.csv
|   |-- DDoS-PSHACK_Flood2.pcap.csv
|   |-- DDoS-PSHACK_Flood3.pcap.csv
|   |-- DDoS-PSHACK_Flood4.pcap.csv
|   |-- DDoS-PSHACK_Flood5.pcap.csv
|   |-- DDoS-PSHACK_Flood6.pcap.csv
|   |-- DDoS-PSHACK_Flood7.pcap.csv
|   |-- DDoS-PSHACK_Flood8.pcap.csv
|   `-- DDoS-PSHACK_Flood9.pcap.csv
|-- DDoS-RSTFINFLOOD
|   |-- DDoS-RSTFINFlood.pcap.csv
|   |-- DDoS-RSTFINFlood1.pcap.csv
|   |-- DDoS-RSTFINFlood10.pcap.csv
|   |-- DDoS-RSTFINFlood11.pcap.csv
|   |-- DDoS-RSTFINFlood12.pcap.csv
|   |-- DDoS-RSTFINFlood13.pcap.csv
|   |-- DDoS-RSTFINFlood14.pcap.csv
|   |-- DDoS-RSTFINFlood15.pcap.csv
|   |-- DDoS-RSTFINFlood2.pcap.csv
|   |-- DDoS-RSTFINFlood3.pcap.csv
|   |-- DDoS-RSTFINFlood4.pcap.csv
|   |-- DDoS-RSTFINFlood5.pcap.csv
|   |-- DDoS-RSTFINFlood6.pcap.csv
|   |-- DDoS-RSTFINFlood7.pcap.csv
|   |-- DDoS-RSTFINFlood8.pcap.csv
|   `-- DDoS-RSTFINFlood9.pcap.csv
|-- DDoS-SlowLoris
|   `-- DDoS-SlowLoris.pcap.csv
|-- DDoS-SYN_Flood
|   |-- DDoS-SYN_Flood.pcap (1).csv
|   |-- DDoS-SYN_Flood.pcap.csv
|   |-- DDoS-SYN_Flood1.pcap (1).csv
|   |-- DDoS-SYN_Flood1.pcap.csv
|   |-- DDoS-SYN_Flood10.pcap.csv
|   |-- DDoS-SYN_Flood11.pcap.csv
|   |-- DDoS-SYN_Flood12.pcap.csv
|   |-- DDoS-SYN_Flood13.pcap.csv
|   |-- DDoS-SYN_Flood14.pcap.csv
|   |-- DDoS-SYN_Flood15.pcap.csv
|   |-- DDoS-SYN_Flood2.pcap.csv
|   |-- DDoS-SYN_Flood3.pcap.csv
|   |-- DDoS-SYN_Flood4.pcap.csv
|   |-- DDoS-SYN_Flood5.pcap.csv
|   |-- DDoS-SYN_Flood6.pcap.csv
|   |-- DDoS-SYN_Flood7.pcap.csv
|   |-- DDoS-SYN_Flood8.pcap.csv
|   `-- DDoS-SYN_Flood9.pcap.csv
|-- DDoS-SynonymousIP_Flood
|   |-- DDoS-SynonymousIP_Flood.pcap.csv
|   |-- DDoS-SynonymousIP_Flood1.pcap.csv
|   |-- DDoS-SynonymousIP_Flood10.pcap.csv
|   |-- DDoS-SynonymousIP_Flood11.pcap.csv
|   |-- DDoS-SynonymousIP_Flood12.pcap.csv
|   |-- DDoS-SynonymousIP_Flood13.pcap.csv
|   |-- DDoS-SynonymousIP_Flood2.pcap.csv
|   |-- DDoS-SynonymousIP_Flood3.pcap.csv
|   |-- DDoS-SynonymousIP_Flood4.pcap.csv
|   |-- DDoS-SynonymousIP_Flood5.pcap.csv
|   |-- DDoS-SynonymousIP_Flood6.pcap.csv
|   |-- DDoS-SynonymousIP_Flood7.pcap.csv
|   |-- DDoS-SynonymousIP_Flood8.pcap.csv
|   `-- DDoS-SynonymousIP_Flood9.pcap.csv
|-- DDoS-TCP_Flood
|   |-- DDoS-TCP_Flood.pcap.csv
|   |-- DDoS-TCP_Flood1.pcap.csv
|   |-- DDoS-TCP_Flood10.pcap.csv
|   |-- DDoS-TCP_Flood11.pcap.csv
|   |-- DDoS-TCP_Flood12.pcap.csv
|   |-- DDoS-TCP_Flood13.pcap.csv
|   |-- DDoS-TCP_Flood14.pcap.csv
|   |-- DDoS-TCP_Flood15.pcap.csv
|   |-- DDoS-TCP_Flood16.pcap.csv
|   |-- DDoS-TCP_Flood17.pcap.csv
|   |-- DDoS-TCP_Flood2.pcap.csv
|   |-- DDoS-TCP_Flood3.pcap.csv
|   |-- DDoS-TCP_Flood4.pcap.csv
|   |-- DDoS-TCP_Flood5.pcap.csv
|   |-- DDoS-TCP_Flood6.pcap.csv
|   |-- DDoS-TCP_Flood7.pcap.csv
|   |-- DDoS-TCP_Flood8.pcap.csv
|   `-- DDoS-TCP_Flood9.pcap.csv
|-- DDoS-UDP_Flood
|   |-- DDoS-UDP_Flood.pcap.csv
|   |-- DDoS-UDP_Flood1.pcap.csv
|   |-- DDoS-UDP_Flood10.pcap.csv
|   |-- DDoS-UDP_Flood11.pcap.csv
|   |-- DDoS-UDP_Flood12.pcap.csv
|   |-- DDoS-UDP_Flood13.pcap.csv
|   |-- DDoS-UDP_Flood14.pcap.csv
|   |-- DDoS-UDP_Flood15.pcap.csv
|   |-- DDoS-UDP_Flood16.pcap.csv
|   |-- DDoS-UDP_Flood17.pcap.csv
|   |-- DDoS-UDP_Flood18.pcap.csv
|   |-- DDoS-UDP_Flood19.pcap.csv
|   |-- DDoS-UDP_Flood2.pcap.csv
|   |-- DDoS-UDP_Flood20.pcap.csv
|   |-- DDoS-UDP_Flood3.pcap.csv
|   |-- DDoS-UDP_Flood4.pcap.csv
|   |-- DDoS-UDP_Flood5.pcap.csv
|   |-- DDoS-UDP_Flood6.pcap.csv
|   |-- DDoS-UDP_Flood7.pcap.csv
|   |-- DDoS-UDP_Flood8.pcap.csv
|   `-- DDoS-UDP_Flood9.pcap.csv
|-- DDoS-UDP_Fragmentation
|   |-- DDoS-UDP_Fragmentation.pcap.csv
|   |-- DDoS-UDP_Fragmentation1.pcap.csv
|   |-- DDoS-UDP_Fragmentation10.pcap.csv
|   |-- DDoS-UDP_Fragmentation11.pcap.csv
|   |-- DDoS-UDP_Fragmentation12.pcap.csv
|   |-- DDoS-UDP_Fragmentation2.pcap.csv
|   |-- DDoS-UDP_Fragmentation3.pcap.csv
|   |-- DDoS-UDP_Fragmentation4.pcap.csv
|   |-- DDoS-UDP_Fragmentation5.pcap.csv
|   |-- DDoS-UDP_Fragmentation6.pcap.csv
|   |-- DDoS-UDP_Fragmentation7.pcap.csv
|   |-- DDoS-UDP_Fragmentation8.pcap.csv
|   `-- DDoS-UDP_Fragmentation9.pcap.csv
`-- CICIOT2023_Dataset Details.docx
```

### Schema Inspection
#### Sample File: `D:\ddos dataset\CIC_IOT_Dataset2023\DDoS-HTTP_Flood\DDoS-HTTP_Flood-.pcap.csv`
- Delimiter: `,`
- Estimated rows: 28790
- Number of features: 39
- Label column: not detected
- Numeric features: 39
- Categorical features: 0
- Columns:
  - Header_Length
  - Protocol Type
  - Time_To_Live
  - Rate
  - fin_flag_number
  - syn_flag_number
  - rst_flag_number
  - psh_flag_number
  - ack_flag_number
  - ece_flag_number
  - cwr_flag_number
  - ack_count
  - syn_count
  - fin_count
  - rst_count
  - HTTP
  - HTTPS
  - DNS
  - Telnet
  - SMTP
  - SSH
  - IRC
  - TCP
  - UDP
  - DHCP
  - ARP
  - ICMP
  - IGMP
  - IPv
  - LLC
  - Tot sum
  - Min
  - Max
  - AVG
  - Std
  - Tot size
  - IAT
  - Number
  - Variance
- Sample rows:
 Header_Length  Protocol Type  Time_To_Live        Rate  fin_flag_number  syn_flag_number  rst_flag_number  psh_flag_number  ack_flag_number  ece_flag_number  cwr_flag_number  ack_count  syn_count  fin_count  rst_count  HTTP  HTTPS  DNS  Telnet  SMTP  SSH  IRC  TCP  UDP  DHCP  ARP  ICMP  IGMP  IPv  LLC  Tot sum  Min  Max    AVG        Std  Tot size      IAT  Number     Variance
         33.76              6         67.82  497.069706             0.04             0.13             0.11             0.05             0.84              0.0              0.0         84         13          4         11  0.94   0.01 0.00     0.0   0.0  0.0  0.0 0.95 0.05  0.00  0.0  0.00   0.0  1.0  1.0     9821   60  559  98.21 109.491413     98.21 0.002012     100 11988.369596
         34.32              6         65.91  300.155291             0.21             0.38             0.08             0.11             0.83              0.0              0.0         83         38         21          8  0.86   0.03 0.01     0.0   0.0  0.0  0.0 0.91 0.03  0.01  0.0  0.06   0.0  1.0  1.0    13080   60  559 130.80 146.430526    130.80 0.003332     100 21441.898990
         36.00              6         64.00 1768.032711             0.08             0.34             0.04             0.08             0.93              0.0              0.0         93         34          8          4  0.93   0.00 0.00     0.0   0.0  0.0  0.0 0.97 0.01  0.00  0.0  0.02   0.0  1.0  1.0    12785   60 1350 127.85 209.633898    127.85 0.000567     100 43946.371212
         37.72              6         65.91  985.075566             0.25             0.04             0.01             0.15             0.98              0.0              0.0         98          4         25          1  0.98   0.00 0.00     0.0   0.0  0.0  0.0 0.99 0.01  0.00  0.0  0.00   0.0  1.0  1.0    14617   60  583 146.17 173.032843    146.17 0.001015     100 29940.364747
         38.28              6         65.91 1074.735051             0.12             0.41             0.02             0.09             0.96              0.0              0.0         96         41         12          2  0.97   0.01 0.01     0.0   0.0  0.0  0.0 0.98 0.02  0.00  0.0  0.00   0.0  1.0  1.0    11410   60  559 114.10 130.468116    114.10 0.000930     100 17021.929293
- Missing values in sample:
- None in sampled rows
- Basic statistics for numeric features:
                   count         mean          std        min            max
Header_Length    10000.0    33.924209     3.860597  10.680000      41.920000
Protocol Type    10000.0     6.055000     0.775909   6.000000      17.000000
Time_To_Live     10000.0    66.278359     5.604410  40.010000     172.560000
Rate             10000.0  2684.943338  8068.605540   0.165804  224775.133976
fin_flag_number  10000.0     0.091041     0.101156   0.000000       0.920000
syn_flag_number  10000.0     0.325027     0.223881   0.000000       1.000000
rst_flag_number  10000.0     0.117565     0.152829   0.000000       1.000000
psh_flag_number  10000.0     0.138004     0.101663   0.000000       0.640000
ack_flag_number  10000.0     0.752703     0.234149   0.000000       1.000000
ece_flag_number  10000.0     0.000057     0.001961   0.000000       0.170000

#### Sample File: `D:\ddos dataset\CIC_IOT_Dataset2023\DDoS-ICMP_Flood\DDoS-ICMP_Flood.pcap.csv`
- Delimiter: `,`
- Estimated rows: 268010
- Number of features: 39
- Label column: not detected
- Numeric features: 39
- Categorical features: 0
- Columns:
  - Header_Length
  - Protocol Type
  - Time_To_Live
  - Rate
  - fin_flag_number
  - syn_flag_number
  - rst_flag_number
  - psh_flag_number
  - ack_flag_number
  - ece_flag_number
  - cwr_flag_number
  - ack_count
  - syn_count
  - fin_count
  - rst_count
  - HTTP
  - HTTPS
  - DNS
  - Telnet
  - SMTP
  - SSH
  - IRC
  - TCP
  - UDP
  - DHCP
  - ARP
  - ICMP
  - IGMP
  - IPv
  - LLC
  - Tot sum
  - Min
  - Max
  - AVG
  - Std
  - Tot size
  - IAT
  - Number
  - Variance
- Sample rows:
 Header_Length  Protocol Type  Time_To_Live         Rate  fin_flag_number  syn_flag_number  rst_flag_number  psh_flag_number  ack_flag_number  ece_flag_number  cwr_flag_number  ack_count  syn_count  fin_count  rst_count  HTTP  HTTPS  DNS  Telnet  SMTP  SSH  IRC  TCP  UDP  DHCP  ARP  ICMP  IGMP  IPv  LLC  Tot sum  Min  Max   AVG       Std  Tot size      IAT  Number   Variance
          0.00              1         64.00  7849.797874             0.00              0.0              0.0             0.00             0.00              0.0              0.0          0          0          0          0   0.0   0.00  0.0     0.0   0.0  0.0  0.0 0.00 0.00   0.0 0.00  1.00   0.0 1.00 1.00     6000   60   60 60.00  0.000000     60.00 0.000127     100   0.000000
          0.00              1         64.00 96243.781551             0.00              0.0              0.0             0.00             0.00              0.0              0.0          0          0          0          0   0.0   0.00  0.0     0.0   0.0  0.0  0.0 0.00 0.00   0.0 0.00  1.00   0.0 1.00 1.00     6000   60   60 60.00  0.000000     60.00 0.000010     100   0.000000
          0.96              1         63.57 26336.204948             0.01              0.0              0.0             0.01             0.03              0.0              0.0          3          0          1          0   0.0   0.03  0.0     0.0   0.0  0.0  0.0 0.03 0.00   0.0 0.00  0.97   0.0 1.00 1.00     6025   60   73 60.25  1.539874     60.25 0.000038     100   2.371212
          0.56              1         69.09  1436.513710             0.01              0.0              0.0             0.00             0.02              0.0              0.0          2          0          1          0   0.0   0.00  0.0     0.0   0.0  0.0  0.0 0.02 0.02   0.0 0.01  0.95   0.0 0.99 0.99     6170   60  230 61.70 17.000000     61.70 0.000696     100 289.000000
          0.00              1         64.00 33067.675812             0.00              0.0              0.0             0.00             0.00              0.0              0.0          0          0          0          0   0.0   0.00  0.0     0.0   0.0  0.0  0.0 0.00 0.00   0.0 0.00  1.00   0.0 1.00 1.00     6000   60   60 60.00  0.000000     60.00 0.000030     100   0.000000
- Missing values in sample:
- Std: 1
- Variance: 1
- Basic statistics for numeric features:
                   count       mean       std         min    max
Header_Length    10000.0   0.054288  0.174763    0.000000   2.60
Protocol Type    10000.0   1.000000  0.000000    1.000000   1.00
Time_To_Live     10000.0  64.038010  0.583464   42.240000  72.94
Rate             10000.0        inf       NaN  761.086856    inf
fin_flag_number  10000.0   0.000216  0.001521    0.000000   0.02
syn_flag_number  10000.0   0.000435  0.002245    0.000000   0.03
rst_flag_number  10000.0   0.000040  0.000677    0.000000   0.03
psh_flag_number  10000.0   0.000395  0.002180    0.000000   0.04
ack_flag_number  10000.0   0.001330  0.004965    0.000000   0.07
ece_flag_number  10000.0   0.000000  0.000000    0.000000   0.00

### Attack Type Analysis
- DDoS present: Yes
- DDoS-related labels: DDoS-ACK_Fragmentation, DDoS-HTTP_Flood, DDoS-ICMP_Flood, DDoS-ICMP_Fragmentation, DDoS-PSHACK_FLOOD, DDoS-RSTFINFLOOD, DDoS-SYN_Flood, DDoS-SlowLoris, DDoS-SynonymousIP_Flood, DDoS-TCP_Flood, DDoS-UDP_Flood, DDoS-UDP_Fragmentation
- Class distribution:
- DDoS-ICMP_Flood: 7200501
- DDoS-UDP_Flood: 5412231
- DDoS-SYN_Flood: 4592400
- DDoS-TCP_Flood: 4497649
- DDoS-PSHACK_FLOOD: 4094772
- DDoS-RSTFINFLOOD: 4045279
- DDoS-SynonymousIP_Flood: 3598133
- Benign_Final: 1098191
- DDoS-ICMP_Fragmentation: 452490
- DDoS-UDP_Fragmentation: 286925
- DDoS-ACK_Fragmentation: 285075
- DDoS-HTTP_Flood: 28790
- DDoS-SlowLoris: 23426

### Feature Analysis
- Representative file: `D:\ddos dataset\CIC_IOT_Dataset2023\DDoS-HTTP_Flood\DDoS-HTTP_Flood-.pcap.csv`
- Number of features: 39
- Numeric feature count: 39
- Categorical feature count: 0
- Numeric features:
  - Header_Length
  - Protocol Type
  - Time_To_Live
  - Rate
  - fin_flag_number
  - syn_flag_number
  - rst_flag_number
  - psh_flag_number
  - ack_flag_number
  - ece_flag_number
  - cwr_flag_number
  - ack_count
  - syn_count
  - fin_count
  - rst_count
  - HTTP
  - HTTPS
  - DNS
  - Telnet
  - SMTP
  - SSH
  - IRC
  - TCP
  - UDP
  - DHCP
  - ARP
  - ICMP
  - IGMP
  - IPv
  - LLC
  - Tot sum
  - Min
  - Max
  - AVG
  - Std
  - Tot size
  - IAT
  - Number
  - Variance
- Categorical features:
  - None

## Dataset: CICDDoS2019
- Path: `D:\ddos dataset\CICDDoS2019`
- Total files: 20
- Total subfolders: 4
- File types:
- .csv: 18
- .docx: 1
- .csv#: 1

### Folder Structure
```text
CICDDoS2019
|-- CSV-01-12
|   `-- 01-12
|       |-- DrDoS_DNS.csv
|       |-- DrDoS_LDAP.csv
|       |-- DrDoS_MSSQL.csv
|       |-- DrDoS_NetBIOS.csv
|       |-- DrDoS_NTP.csv
|       |-- DrDoS_SNMP.csv
|       |-- DrDoS_SSDP.csv
|       |-- DrDoS_UDP.csv
|       |-- Syn.csv
|       |-- TFTP.csv
|       `-- UDPLag.csv
|-- CSV-03-11
|   `-- 03-11
|       |-- .~lock.UDPLag.csv#
|       |-- LDAP.csv
|       |-- MSSQL.csv
|       |-- NetBIOS.csv
|       |-- Portmap.csv
|       |-- Syn.csv
|       |-- UDP.csv
|       `-- UDPLag.csv
`-- CICDDoS2019_Dataset Details.docx
```

### Schema Inspection
#### Sample File: `D:\ddos dataset\CICDDoS2019\CSV-01-12\01-12\DrDoS_DNS.csv`
- Delimiter: `,`
- Estimated rows: 5074413
- Number of features: 87
- Label column: ` Label`
- Numeric features: 81
- Categorical features: 6
- Columns:
  - Flow ID
  -  Source IP
  -  Source Port
  -  Destination IP
  -  Destination Port
  -  Protocol
  -  Timestamp
  -  Flow Duration
  -  Total Fwd Packets
  -  Total Backward Packets
  - Total Length of Fwd Packets
  -  Total Length of Bwd Packets
  -  Fwd Packet Length Max
  -  Fwd Packet Length Min
  -  Fwd Packet Length Mean
  -  Fwd Packet Length Std
  - Bwd Packet Length Max
  -  Bwd Packet Length Min
  -  Bwd Packet Length Mean
  -  Bwd Packet Length Std
  - Flow Bytes/s
  -  Flow Packets/s
  -  Flow IAT Mean
  -  Flow IAT Std
  -  Flow IAT Max
  -  Flow IAT Min
  - Fwd IAT Total
  -  Fwd IAT Mean
  -  Fwd IAT Std
  -  Fwd IAT Max
  -  Fwd IAT Min
  - Bwd IAT Total
  -  Bwd IAT Mean
  -  Bwd IAT Std
  -  Bwd IAT Max
  -  Bwd IAT Min
  - Fwd PSH Flags
  -  Bwd PSH Flags
  -  Fwd URG Flags
  -  Bwd URG Flags
  -  Fwd Header Length
  -  Bwd Header Length
  - Fwd Packets/s
  -  Bwd Packets/s
  -  Min Packet Length
  -  Max Packet Length
  -  Packet Length Mean
  -  Packet Length Std
  -  Packet Length Variance
  - FIN Flag Count
  -  SYN Flag Count
  -  RST Flag Count
  -  PSH Flag Count
  -  ACK Flag Count
  -  URG Flag Count
  -  CWE Flag Count
  -  ECE Flag Count
  -  Down/Up Ratio
  -  Average Packet Size
  -  Avg Fwd Segment Size
  -  Avg Bwd Segment Size
  -  Fwd Header Length.1
  - Fwd Avg Bytes/Bulk
  -  Fwd Avg Packets/Bulk
  -  Fwd Avg Bulk Rate
  -  Bwd Avg Bytes/Bulk
  -  Bwd Avg Packets/Bulk
  - Bwd Avg Bulk Rate
  - Subflow Fwd Packets
  -  Subflow Fwd Bytes
  -  Subflow Bwd Packets
  -  Subflow Bwd Bytes
  - Init_Win_bytes_forward
  -  Init_Win_bytes_backward
  -  act_data_pkt_fwd
  -  min_seg_size_forward
  - Active Mean
  -  Active Std
  -  Active Max
  -  Active Min
  - Idle Mean
  -  Idle Std
  -  Idle Max
  -  Idle Min
  - SimillarHTTP
  -  Inbound
  -  Label
- Sample attack categories:
  - DrDoS_DNS
- Sample rows:
                             Flow ID    Source IP   Source Port  Destination IP   Destination Port   Protocol                  Timestamp   Flow Duration   Total Fwd Packets   Total Backward Packets  Total Length of Fwd Packets   Total Length of Bwd Packets   Fwd Packet Length Max   Fwd Packet Length Min   Fwd Packet Length Mean   Fwd Packet Length Std  Bwd Packet Length Max   Bwd Packet Length Min   Bwd Packet Length Mean   Bwd Packet Length Std  Flow Bytes/s   Flow Packets/s   Flow IAT Mean   Flow IAT Std   Flow IAT Max   Flow IAT Min  Fwd IAT Total   Fwd IAT Mean   Fwd IAT Std   Fwd IAT Max   Fwd IAT Min  Bwd IAT Total   Bwd IAT Mean   Bwd IAT Std   Bwd IAT Max   Bwd IAT Min  Fwd PSH Flags   Bwd PSH Flags   Fwd URG Flags   Bwd URG Flags   Fwd Header Length   Bwd Header Length  Fwd Packets/s   Bwd Packets/s   Min Packet Length   Max Packet Length   Packet Length Mean   Packet Length Std   Packet Length Variance  FIN Flag Count   SYN Flag Count   RST Flag Count   PSH Flag Count   ACK Flag Count   URG Flag Count   CWE Flag Count   ECE Flag Count   Down/Up Ratio   Average Packet Size   Avg Fwd Segment Size   Avg Bwd Segment Size   Fwd Header Length.1  Fwd Avg Bytes/Bulk   Fwd Avg Packets/Bulk   Fwd Avg Bulk Rate   Bwd Avg Bytes/Bulk   Bwd Avg Packets/Bulk  Bwd Avg Bulk Rate  Subflow Fwd Packets   Subflow Fwd Bytes   Subflow Bwd Packets   Subflow Bwd Bytes  Init_Win_bytes_forward   Init_Win_bytes_backward   act_data_pkt_fwd   min_seg_size_forward  Active Mean   Active Std   Active Max   Active Min  Idle Mean   Idle Std   Idle Max   Idle Min  SimillarHTTP   Inbound     Label
172.16.0.5-192.168.50.1-634-60495-17   172.16.0.5           634    192.168.50.1              60495         17 2018-12-01 10:51:39.813448           28415                  97                        0                      42680.0                           0.0                   440.0                   440.0                    440.0                     0.0                    0.0                     0.0                      0.0                     0.0  1.502024e+06      3413.689952      295.989583     500.959301         3596.0            1.0        28415.0     295.989583    500.959301        3596.0           1.0            0.0            0.0           0.0           0.0           0.0              0               0               0               0                 -97                   0    3413.689952             0.0               440.0               440.0                440.0                 0.0                      0.0               0                0                0                0                0                0                0                0             0.0            444.536082                  440.0                    0.0                   -97                   0                      0                   0                    0                      0                  0                   97               42680                     0                   0                      -1                        -1                 96                     -1          0.0          0.0          0.0          0.0        0.0        0.0        0.0        0.0             0         1 DrDoS_DNS
172.16.0.5-192.168.50.1-60495-634-17 192.168.50.1           634      172.16.0.5              60495         17 2018-12-01 10:51:39.820842               2                   2                        0                        880.0                           0.0                   440.0                   440.0                    440.0                     0.0                    0.0                     0.0                      0.0                     0.0  4.400000e+08   1000000.000000        2.000000       0.000000            2.0            2.0            2.0       2.000000      0.000000           2.0           2.0            0.0            0.0           0.0           0.0           0.0              0               0               0               0                  -2                   0 1000000.000000             0.0               440.0               440.0                440.0                 0.0                      0.0               0                0                0                0                0                0                0                0             0.0            660.000000                  440.0                    0.0                    -2                   0                      0                   0                    0                      0                  0                    2                 880                     0                   0                      -1                        -1                  1                     -1          0.0          0.0          0.0          0.0        0.0        0.0        0.0        0.0             0         0 DrDoS_DNS
172.16.0.5-192.168.50.1-634-46391-17   172.16.0.5           634    192.168.50.1              46391         17 2018-12-01 10:51:39.852499           48549                 200                        0                      88000.0                           0.0                   440.0                   440.0                    440.0                     0.0                    0.0                     0.0                      0.0                     0.0  1.812602e+06      4119.549321      243.964824     578.101371         5418.0            1.0        48549.0     243.964824    578.101371        5418.0           1.0            0.0            0.0           0.0           0.0           0.0              0               0               0               0                -200                   0    4119.549321             0.0               440.0               440.0                440.0                 0.0                      0.0               0                0                0                0                0                0                0                0             0.0            442.200000                  440.0                    0.0                  -200                   0                      0                   0                    0                      0                  0                  200               88000                     0                   0                      -1                        -1                199                     -1          0.0          0.0          0.0          0.0        0.0        0.0        0.0        0.0             0         1 DrDoS_DNS
172.16.0.5-192.168.50.1-634-11894-17   172.16.0.5           634    192.168.50.1              11894         17 2018-12-01 10:51:39.890213           48337                 200                        0                      88000.0                           0.0                   440.0                   440.0                    440.0                     0.0                    0.0                     0.0                      0.0                     0.0  1.820552e+06      4137.617146      242.899497     485.292695         3337.0            1.0        48337.0     242.899497    485.292695        3337.0           1.0            0.0            0.0           0.0           0.0           0.0              0               0               0               0                -200                   0    4137.617146             0.0               440.0               440.0                440.0                 0.0                      0.0               0                0                0                0                0                0                0                0             0.0            442.200000                  440.0                    0.0                  -200                   0                      0                   0                    0                      0                  0                  200               88000                     0                   0                      -1                        -1                199                     -1          0.0          0.0          0.0          0.0        0.0        0.0        0.0        0.0             0         1 DrDoS_DNS
172.16.0.5-192.168.50.1-634-27878-17   172.16.0.5           634    192.168.50.1              27878         17 2018-12-01 10:51:39.941151           32026                 200                        0                      88000.0                           0.0                   440.0                   440.0                    440.0                     0.0                    0.0                     0.0                      0.0                     0.0  2.747767e+06      6244.925998      160.934673     196.891271         1236.0            0.0        32026.0     160.934673    196.891271        1236.0           0.0            0.0            0.0           0.0           0.0           0.0              0               0               0               0                -200                   0    6244.925998             0.0               440.0               440.0                440.0                 0.0                      0.0               0                0                0                0                0                0                0                0             0.0            442.200000                  440.0                    0.0                  -200                   0                      0                   0                    0                      0                  0                  200               88000                     0                   0                      -1                        -1                199                     -1          0.0          0.0          0.0          0.0        0.0        0.0        0.0        0.0             0         1 DrDoS_DNS
- Missing values in sample:
- Flow Bytes/s: 1
- Basic statistics for numeric features:
                                count          mean           std  min          max
 Source Port                  10000.0  1.009548e+04  2.128647e+04  0.0      65378.0
 Destination Port             10000.0  3.036197e+04  2.048006e+04  0.0      65532.0
 Protocol                     10000.0  1.602330e+01  3.161448e+00  0.0         17.0
 Flow Duration                10000.0  1.623976e+06  1.179004e+07  0.0  119819608.0
 Total Fwd Packets            10000.0  1.252058e+02  1.003519e+02  1.0       2840.0
 Total Backward Packets       10000.0  9.374000e-01  6.927458e+00  0.0        261.0
Total Length of Fwd Packets   10000.0  5.461222e+04  3.945204e+04  0.0     176000.0
 Total Length of Bwd Packets  10000.0  2.126069e+02  4.018739e+03  0.0     272724.0
 Fwd Packet Length Max        10000.0  5.588294e+02  4.136912e+02  0.0       3174.0
 Fwd Packet Length Min        10000.0  5.017219e+02  4.338922e+02  0.0       1472.0

#### Sample File: `D:\ddos dataset\CICDDoS2019\CSV-01-12\01-12\DrDoS_LDAP.csv`
- Delimiter: `,`
- Estimated rows: 2181542
- Number of features: 87
- Label column: ` Label`
- Numeric features: 82
- Categorical features: 5
- Columns:
  - Flow ID
  -  Source IP
  -  Source Port
  -  Destination IP
  -  Destination Port
  -  Protocol
  -  Timestamp
  -  Flow Duration
  -  Total Fwd Packets
  -  Total Backward Packets
  - Total Length of Fwd Packets
  -  Total Length of Bwd Packets
  -  Fwd Packet Length Max
  -  Fwd Packet Length Min
  -  Fwd Packet Length Mean
  -  Fwd Packet Length Std
  - Bwd Packet Length Max
  -  Bwd Packet Length Min
  -  Bwd Packet Length Mean
  -  Bwd Packet Length Std
  - Flow Bytes/s
  -  Flow Packets/s
  -  Flow IAT Mean
  -  Flow IAT Std
  -  Flow IAT Max
  -  Flow IAT Min
  - Fwd IAT Total
  -  Fwd IAT Mean
  -  Fwd IAT Std
  -  Fwd IAT Max
  -  Fwd IAT Min
  - Bwd IAT Total
  -  Bwd IAT Mean
  -  Bwd IAT Std
  -  Bwd IAT Max
  -  Bwd IAT Min
  - Fwd PSH Flags
  -  Bwd PSH Flags
  -  Fwd URG Flags
  -  Bwd URG Flags
  -  Fwd Header Length
  -  Bwd Header Length
  - Fwd Packets/s
  -  Bwd Packets/s
  -  Min Packet Length
  -  Max Packet Length
  -  Packet Length Mean
  -  Packet Length Std
  -  Packet Length Variance
  - FIN Flag Count
  -  SYN Flag Count
  -  RST Flag Count
  -  PSH Flag Count
  -  ACK Flag Count
  -  URG Flag Count
  -  CWE Flag Count
  -  ECE Flag Count
  -  Down/Up Ratio
  -  Average Packet Size
  -  Avg Fwd Segment Size
  -  Avg Bwd Segment Size
  -  Fwd Header Length.1
  - Fwd Avg Bytes/Bulk
  -  Fwd Avg Packets/Bulk
  -  Fwd Avg Bulk Rate
  -  Bwd Avg Bytes/Bulk
  -  Bwd Avg Packets/Bulk
  - Bwd Avg Bulk Rate
  - Subflow Fwd Packets
  -  Subflow Fwd Bytes
  -  Subflow Bwd Packets
  -  Subflow Bwd Bytes
  - Init_Win_bytes_forward
  -  Init_Win_bytes_backward
  -  act_data_pkt_fwd
  -  min_seg_size_forward
  - Active Mean
  -  Active Std
  -  Active Max
  -  Active Min
  - Idle Mean
  -  Idle Std
  -  Idle Max
  -  Idle Min
  - SimillarHTTP
  -  Inbound
  -  Label
- Sample attack categories:
  - DrDoS_LDAP
- Sample rows:
                             Flow ID  Source IP   Source Port  Destination IP   Destination Port   Protocol                  Timestamp   Flow Duration   Total Fwd Packets   Total Backward Packets  Total Length of Fwd Packets   Total Length of Bwd Packets   Fwd Packet Length Max   Fwd Packet Length Min   Fwd Packet Length Mean   Fwd Packet Length Std  Bwd Packet Length Max   Bwd Packet Length Min   Bwd Packet Length Mean   Bwd Packet Length Std  Flow Bytes/s   Flow Packets/s   Flow IAT Mean   Flow IAT Std   Flow IAT Max   Flow IAT Min  Fwd IAT Total   Fwd IAT Mean   Fwd IAT Std   Fwd IAT Max   Fwd IAT Min  Bwd IAT Total   Bwd IAT Mean   Bwd IAT Std   Bwd IAT Max   Bwd IAT Min  Fwd PSH Flags   Bwd PSH Flags   Fwd URG Flags   Bwd URG Flags   Fwd Header Length   Bwd Header Length  Fwd Packets/s   Bwd Packets/s   Min Packet Length   Max Packet Length   Packet Length Mean   Packet Length Std   Packet Length Variance  FIN Flag Count   SYN Flag Count   RST Flag Count   PSH Flag Count   ACK Flag Count   URG Flag Count   CWE Flag Count   ECE Flag Count   Down/Up Ratio   Average Packet Size   Avg Fwd Segment Size   Avg Bwd Segment Size   Fwd Header Length.1  Fwd Avg Bytes/Bulk   Fwd Avg Packets/Bulk   Fwd Avg Bulk Rate   Bwd Avg Bytes/Bulk   Bwd Avg Packets/Bulk  Bwd Avg Bulk Rate  Subflow Fwd Packets   Subflow Fwd Bytes   Subflow Bwd Packets   Subflow Bwd Bytes  Init_Win_bytes_forward   Init_Win_bytes_backward   act_data_pkt_fwd   min_seg_size_forward  Active Mean   Active Std   Active Max   Active Min  Idle Mean   Idle Std   Idle Max   Idle Min  SimillarHTTP   Inbound      Label
       172.16.0.5-192.168.50.1-0-0-0 172.16.0.5             0    192.168.50.1                  0          0 2018-12-01 11:22:40.254769         9141643               85894                       28                          0.0                           0.0                     0.0                     0.0                      0.0                     0.0                    0.0                     0.0                      0.0                     0.0           0.0     9.398967e+03       106.39591     209.905159         2968.0            0.0      9141643.0     106.430594     209.94653        2968.0           0.0      8487477.0       314351.0  1147262.6944     5975703.0           0.0              0               0               0               0                   0                   0   9.395904e+03        3.062907                 0.0                 0.0                  0.0                 0.0                      0.0               0                0                0                0                0                0                0                0             0.0                   0.0                    0.0                    0.0                     0                   0                      0                   0                    0                      0                  0                85894                   0                    28                   0                      -1                        -1                  0                      0          0.0          0.0          0.0          0.0        0.0        0.0        0.0        0.0             0         1 DrDoS_LDAP
 172.16.0.5-192.168.50.1-900-1808-17 172.16.0.5           900    192.168.50.1               1808         17 2018-12-01 11:22:40.255361               1                   2                        0                       2944.0                           0.0                  1472.0                  1472.0                   1472.0                     0.0                    0.0                     0.0                      0.0                     0.0  2944000000.0     2.000000e+06         1.00000       0.000000            1.0            1.0            1.0       1.000000       0.00000           1.0           1.0            0.0            0.0        0.0000           0.0           0.0              0               0               0               0                  -2                   0   2.000000e+06        0.000000              1472.0              1472.0               1472.0                 0.0                      0.0               0                0                0                0                0                0                0                0             0.0                2208.0                 1472.0                    0.0                    -2                   0                      0                   0                    0                      0                  0                    2                2944                     0                   0                      -1                        -1                  1                     -1          0.0          0.0          0.0          0.0        0.0        0.0        0.0        0.0             0         1 DrDoS_LDAP
172.16.0.5-192.168.50.1-900-58766-17 172.16.0.5           900    192.168.50.1              58766         17 2018-12-01 11:22:40.255568               2                   2                        0                       2944.0                           0.0                  1472.0                  1472.0                   1472.0                     0.0                    0.0                     0.0                      0.0                     0.0  1472000000.0     1.000000e+06         2.00000       0.000000            2.0            2.0            2.0       2.000000       0.00000           2.0           2.0            0.0            0.0        0.0000           0.0           0.0              0               0               0               0                  -2                   0   1.000000e+06        0.000000              1472.0              1472.0               1472.0                 0.0                      0.0               0                0                0                0                0                0                0                0             0.0                2208.0                 1472.0                    0.0                    -2                   0                      0                   0                    0                      0                  0                    2                2944                     0                   0                      -1                        -1                  1                     -1          0.0          0.0          0.0          0.0        0.0        0.0        0.0        0.0             0         1 DrDoS_LDAP
172.16.0.5-192.168.50.1-900-35228-17 172.16.0.5           900    192.168.50.1              35228         17 2018-12-01 11:22:40.256113               1                   2                        0                       2944.0                           0.0                  1472.0                  1472.0                   1472.0                     0.0                    0.0                     0.0                      0.0                     0.0  2944000000.0     2.000000e+06         1.00000       0.000000            1.0            1.0            1.0       1.000000       0.00000           1.0           1.0            0.0            0.0        0.0000           0.0           0.0              0               0               0               0                  -2                   0   2.000000e+06        0.000000              1472.0              1472.0               1472.0                 0.0                      0.0               0                0                0                0                0                0                0                0             0.0                2208.0                 1472.0                    0.0                    -2                   0                      0                   0                    0                      0                  0                    2                2944                     0                   0                      -1                        -1                  1                     -1          0.0          0.0          0.0          0.0        0.0        0.0        0.0        0.0             0         1 DrDoS_LDAP
172.16.0.5-192.168.50.1-900-44969-17 172.16.0.5           900    192.168.50.1              44969         17 2018-12-01 11:22:40.256285               2                   2                        0                       2944.0                           0.0                  1472.0                  1472.0                   1472.0                     0.0                    0.0                     0.0                      0.0                     0.0  1472000000.0     1.000000e+06         2.00000       0.000000            2.0            2.0            2.0       2.000000       0.00000           2.0           2.0            0.0            0.0        0.0000           0.0           0.0              0               0               0               0                  -2                   0   1.000000e+06        0.000000              1472.0              1472.0               1472.0                 0.0                      0.0               0                0                0                0                0                0                0                0             0.0                2208.0                 1472.0                    0.0                    -2                   0                      0                   0                    0                      0                  0                    2                2944                     0                   0                      -1                        -1                  1                     -1          0.0          0.0          0.0          0.0        0.0        0.0        0.0        0.0             0         1 DrDoS_LDAP
- Missing values in sample:
- None in sampled rows
- Basic statistics for numeric features:
                                count        mean           std  min        max
 Source Port                  10000.0    899.9604    764.200219  0.0    57215.0
 Destination Port             10000.0  32903.4133  18939.241399  0.0    65530.0
 Protocol                     10000.0     16.9900      0.360989  0.0       17.0
 Flow Duration                10000.0   1329.4399  96126.634051  0.0  9141643.0
 Total Fwd Packets            10000.0     10.5920    858.919980  2.0    85894.0
 Total Backward Packets       10000.0      0.0039      0.287912  0.0       28.0
Total Length of Fwd Packets   10000.0   2929.3718    196.862085  0.0    14720.0
 Total Length of Bwd Packets  10000.0      0.0304      3.040000  0.0      304.0
 Fwd Packet Length Max        10000.0   1463.3543     61.928571  0.0     1472.0
 Fwd Packet Length Min        10000.0   1463.3475     62.085336  0.0     1472.0

### Attack Type Analysis
- DDoS present: Yes
- DDoS-related labels: DrDoS_DNS, DrDoS_LDAP, DrDoS_MSSQL, DrDoS_NTP, DrDoS_NetBIOS, DrDoS_SNMP, DrDoS_SSDP, DrDoS_UDP, LDAP, MSSQL, NetBIOS, Portmap, Syn, TFTP, UDP, UDP-lag, UDPLag, WebDDoS
- Class distribution:
- TFTP: 20082580
- Syn: 6473789
- MSSQL: 5787453
- DrDoS_SNMP: 5159870
- DrDoS_DNS: 5071011
- DrDoS_MSSQL: 4522492
- DrDoS_NetBIOS: 4093279
- UDP: 3867155
- NetBIOS: 3657497
- DrDoS_UDP: 3134645
- DrDoS_SSDP: 2610611
- DrDoS_LDAP: 2179930
- LDAP: 1915122
- DrDoS_NTP: 1202642
- UDP-lag: 366461
- Portmap: 186960
- BENIGN: 113828
- UDPLag: 1873
- WebDDoS: 439

### Feature Analysis
- Representative file: `D:\ddos dataset\CICDDoS2019\CSV-01-12\01-12\DrDoS_DNS.csv`
- Number of features: 87
- Numeric feature count: 81
- Categorical feature count: 6
- Numeric features:
  -  Source Port
  -  Destination Port
  -  Protocol
  -  Flow Duration
  -  Total Fwd Packets
  -  Total Backward Packets
  - Total Length of Fwd Packets
  -  Total Length of Bwd Packets
  -  Fwd Packet Length Max
  -  Fwd Packet Length Min
  -  Fwd Packet Length Mean
  -  Fwd Packet Length Std
  - Bwd Packet Length Max
  -  Bwd Packet Length Min
  -  Bwd Packet Length Mean
  -  Bwd Packet Length Std
  - Flow Bytes/s
  -  Flow Packets/s
  -  Flow IAT Mean
  -  Flow IAT Std
  -  Flow IAT Max
  -  Flow IAT Min
  - Fwd IAT Total
  -  Fwd IAT Mean
  -  Fwd IAT Std
  -  Fwd IAT Max
  -  Fwd IAT Min
  - Bwd IAT Total
  -  Bwd IAT Mean
  -  Bwd IAT Std
  -  Bwd IAT Max
  -  Bwd IAT Min
  - Fwd PSH Flags
  -  Bwd PSH Flags
  -  Fwd URG Flags
  -  Bwd URG Flags
  -  Fwd Header Length
  -  Bwd Header Length
  - Fwd Packets/s
  -  Bwd Packets/s
  -  Min Packet Length
  -  Max Packet Length
  -  Packet Length Mean
  -  Packet Length Std
  -  Packet Length Variance
  - FIN Flag Count
  -  SYN Flag Count
  -  RST Flag Count
  -  PSH Flag Count
  -  ACK Flag Count
- Categorical features:
  - Flow ID
  -  Source IP
  -  Destination IP
  -  Timestamp
  - SimillarHTTP
  -  Label

## Dataset: TON_IoT Dataset
- Path: `D:\ddos dataset\TON_IoT Dataset`
- Total files: 89
- Total subfolders: 17
- File types:
- .csv: 52
- .docx: 14
- .pdf: 12
- .xlsx: 10
- .vsdx: 1

### Folder Structure
```text
TON_IoT Dataset
|-- Description_stats_datasets
|   `-- Description_stats_datasets
|       |-- Description_stats_IoT_dataset
|       |   |-- IoT Features- Description.xlsx
|       |   |-- IoT Features-Description.docx
|       |   |-- IoT Features-Description.pdf
|       |   |-- Statistics of IoT Records.docx
|       |   |-- Statistics of IoT Records.pdf
|       |   `-- Statistics of IoT Records.xlsx
|       |-- Description_stats_Linux_dataset
|       |   |-- Linux Features-Description-old.docx
|       |   |-- Linux Features-Description.docx
|       |   |-- Linux Features-Description.pdf
|       |   |-- Linux Features-Description.xlsx
|       |   |-- New Microsoft Visio Drawing.vsdx
|       |   |-- New Microsoft Word Document.docx
|       |   |-- Statistics of Linux Records.docx
|       |   |-- Statistics of Linux Records.pdf
|       |   `-- Statistics of Linux Records.xlsx
|       |-- Description_stats_Network_dataset
|       |   |-- bro_log_vars.pdf
|       |   |-- Network Features-Description.docx
|       |   |-- Network Features-Description.pdf
|       |   |-- Network Features-Description.xlsx
|       |   |-- Statistics of Network Records.docx
|       |   |-- Statistics of Network Records.pdf
|       |   `-- Statistics of Network Records.xlsx
|       `-- Description_stats_Windows_dataset
|           |-- Statistics of Windows Records.docx
|           |-- Statistics of Windows Records.pdf
|           |-- Statistics of Windows Records.xlsx
|           |-- Windows 10 Features.docx
|           |-- Windows 10 Features.pdf
|           |-- Windows 7 Features.docx
|           |-- Windows 7 Features.pdf
|           `-- Windows Features.xlsx
|-- Description_stats_IoT_dataset
|   |-- IoT Features- Description.xlsx
|   |-- IoT Features-Description.docx
|   |-- IoT Features-Description.pdf
|   |-- Statistics of IoT Records.docx
|   |-- Statistics of IoT Records.pdf
|   `-- Statistics of IoT Records.xlsx
|-- Processed_datasets
|   `-- Processed_datasets
|       |-- Processed_IoT_dataset
|       |   |-- IoT_Fridge.csv
|       |   |-- IoT_Garage_Door.csv
|       |   |-- IoT_GPS_Tracker.csv
|       |   |-- IoT_Modbus.csv
|       |   |-- IoT_Motion_Light.csv
|       |   |-- IoT_Thermostat.csv
|       |   `-- IoT_Weather.csv
|       |-- Processed_Linux_dataset
|       |   |-- linux_disk_1.csv
|       |   |-- linux_disk_2.csv
|       |   |-- linux_memory1.csv
|       |   |-- linux_memory2.csv
|       |   |-- Linux_process_1.csv
|       |   `-- Linux_process_2.csv
|       |-- Processed_Network_dataset
|       |   |-- Network_dataset_1.csv
|       |   |-- Network_dataset_10.csv
|       |   |-- Network_dataset_11.csv
|       |   |-- Network_dataset_12.csv
|       |   |-- Network_dataset_13.csv
|       |   |-- Network_dataset_14.csv
|       |   |-- Network_dataset_15.csv
|       |   |-- Network_dataset_16.csv
|       |   |-- Network_dataset_17.csv
|       |   |-- Network_dataset_18.csv
|       |   |-- Network_dataset_19.csv
|       |   |-- Network_dataset_2.csv
|       |   |-- Network_dataset_20.csv
|       |   |-- Network_dataset_21.csv
|       |   |-- Network_dataset_22.csv
|       |   |-- Network_dataset_23.csv
|       |   |-- Network_dataset_3.csv
|       |   |-- Network_dataset_4.csv
|       |   |-- Network_dataset_5.csv
|       |   |-- Network_dataset_6.csv
|       |   |-- Network_dataset_7.csv
|       |   |-- Network_dataset_8.csv
|       |   `-- Network_dataset_9.csv
|       `-- Processed_Windows_dataset
|           |-- windows10_dataset.csv
|           `-- windows7_dataset.csv
|-- SecurityEvents_IoT_datasets
|   `-- SecurityEvents_IoT_datasets
|       |-- GroundTruth_IoT_Fridge.csv
|       |-- GroundTruth_IoT_Garage_Door.csv
|       |-- GroundTruth_IoT_GPS_Tracker.csv
|       |-- GroundTruth_IoT_Modbus.csv
|       |-- GroundTruth_IoT_Motion_Light.csv
|       |-- GroundTruth_IoT_Thermostat.csv
|       `-- GroundTruth_IoT_Weather.csv
|-- Train_Test_IoT_dataset
|   `-- Train_Test_IoT_dataset
|       |-- Train_Test_IoT_Fridge.csv
|       |-- Train_Test_IoT_Garage_Door.csv
|       |-- Train_Test_IoT_GPS_Tracker.csv
|       |-- Train_Test_IoT_Modbus.csv
|       |-- Train_Test_IoT_Motion_Light.csv
|       |-- Train_Test_IoT_Thermostat.csv
|       `-- Train_Test_IoT_Weather.csv
`-- TON_IOT_Dataset Details.docx
```

### Schema Inspection
#### Sample File: `D:\ddos dataset\TON_IoT Dataset\Processed_datasets\Processed_datasets\Processed_Network_dataset\Network_dataset_1.csv`
- Delimiter: `,`
- Estimated rows: 1000000
- Number of features: 46
- Label column: `type`
- Numeric features: 18
- Categorical features: 28
- Columns:
  - ts
  - src_ip
  - src_port
  - dst_ip
  - dst_port
  - proto
  - service
  - duration
  - src_bytes
  - dst_bytes
  - conn_state
  - missed_bytes
  - src_pkts
  - src_ip_bytes
  - dst_pkts
  - dst_ip_bytes
  - dns_query
  - dns_qclass
  - dns_qtype
  - dns_rcode
  - dns_AA
  - dns_RD
  - dns_RA
  - dns_rejected
  - ssl_version
  - ssl_cipher
  - ssl_resumed
  - ssl_established
  - ssl_subject
  - ssl_issuer
  - http_trans_depth
  - http_method
  - http_uri
  - http_referrer
  - http_version
  - http_request_body_len
  - http_response_body_len
  - http_status_code
  - http_user_agent
  - http_orig_mime_types
  - http_resp_mime_types
  - weird_name
  - weird_addl
  - weird_notice
  - label
  - type
- Sample attack categories:
  - normal
- Sample rows:
        ts        src_ip  src_port        dst_ip  dst_port proto service     duration  src_bytes  dst_bytes conn_state  missed_bytes  src_pkts  src_ip_bytes  dst_pkts  dst_ip_bytes dns_query  dns_qclass  dns_qtype  dns_rcode dns_AA dns_RD dns_RA dns_rejected ssl_version ssl_cipher ssl_resumed ssl_established ssl_subject ssl_issuer http_trans_depth http_method http_uri http_referrer http_version  http_request_body_len  http_response_body_len  http_status_code http_user_agent http_orig_mime_types http_resp_mime_types       weird_name weird_addl weird_notice  label   type
1554198358   3.122.49.24      1883 192.168.1.152     52976   tcp       - 80549.530260    1762852   41933215        OTH             0    252181      14911156         2           236         -           0          0          0      -      -      -            -           -          -           -               -           -          -                -           -        -             -            -                      0                       0                 0               -                    -                    - bad_TCP_checksum          -            F      0 normal
1554198358  192.168.1.79     47260 192.168.1.255     15600   udp       -     0.000000          0          0         S0             0         1            63         0             0         -           0          0          0      -      -      -            -           -          -           -               -           -          -                -           -        -             -            -                      0                       0                 0               -                    -                    -                -          -            -      0 normal
1554198359 192.168.1.152      1880 192.168.1.152     51782   tcp       -     0.000000          0          0        OTH             0         0             0         0             0         -           0          0          0      -      -      -            -           -          -           -               -           -          -                -           -        -             -            -                      0                       0                 0               -                    -                    - bad_TCP_checksum          -            F      0 normal
1554198359 192.168.1.152     34296 192.168.1.152     10502   tcp       -     0.000000          0          0        OTH             0         0             0         0             0         -           0          0          0      -      -      -            -           -          -           -               -           -          -                -           -        -             -            -                      0                       0                 0               -                    -                    -                -          -            -      0 normal
1554198362 192.168.1.152     46608 192.168.1.190        53   udp     dns     0.000549          0        298        SHR             0         0             0         2           354         -           0          0          0      -      -      -            -           -          -           -               -           -          -                -           -        -             -            -                      0                       0                 0               -                    -                    - bad_UDP_checksum          -            F      0 normal
- Missing values in sample:
- None in sampled rows
- Basic statistics for numeric features:
                count          mean            std           min           max
ts            10000.0  1.554206e+09    4895.096489  1.554198e+09  1.554216e+09
src_port      10000.0  2.591813e+04   19657.840909  3.000000e+00  6.099600e+04
dst_port      10000.0  2.370609e+04   20829.170648  0.000000e+00  5.762800e+04
duration      10000.0  1.798023e+01     959.652211  0.000000e+00  8.054953e+04
src_bytes     10000.0  1.020667e+04  744011.561420  0.000000e+00  6.636572e+07
dst_bytes     10000.0  4.437864e+03  419461.152174  0.000000e+00  4.193322e+07
missed_bytes  10000.0  0.000000e+00       0.000000  0.000000e+00  0.000000e+00
src_pkts      10000.0  2.595380e+01    2521.814873  0.000000e+00  2.521810e+05
src_ip_bytes  10000.0  1.565326e+03  149112.511746  0.000000e+00  1.491116e+07
dst_pkts      10000.0  2.234720e+01    1348.837640  0.000000e+00  1.219420e+05

#### Sample File: `D:\ddos dataset\TON_IoT Dataset\Processed_datasets\Processed_datasets\Processed_Network_dataset\Network_dataset_10.csv`
- Delimiter: `,`
- Estimated rows: 1000000
- Number of features: 46
- Label column: `type`
- Numeric features: 18
- Categorical features: 28
- Columns:
  - ts
  - src_ip
  - src_port
  - dst_ip
  - dst_port
  - proto
  - service
  - duration
  - src_bytes
  - dst_bytes
  - conn_state
  - missed_bytes
  - src_pkts
  - src_ip_bytes
  - dst_pkts
  - dst_ip_bytes
  - dns_query
  - dns_qclass
  - dns_qtype
  - dns_rcode
  - dns_AA
  - dns_RD
  - dns_RA
  - dns_rejected
  - ssl_version
  - ssl_cipher
  - ssl_resumed
  - ssl_established
  - ssl_subject
  - ssl_issuer
  - http_trans_depth
  - http_method
  - http_uri
  - http_referrer
  - http_version
  - http_request_body_len
  - http_response_body_len
  - http_status_code
  - http_user_agent
  - http_orig_mime_types
  - http_resp_mime_types
  - weird_name
  - weird_addl
  - weird_notice
  - label
  - type
- Sample attack categories:
  - dos
- Sample rows:
        ts       src_ip  src_port        dst_ip  dst_port proto service  duration  src_bytes  dst_bytes conn_state  missed_bytes  src_pkts  src_ip_bytes  dst_pkts  dst_ip_bytes dns_query  dns_qclass  dns_qtype  dns_rcode dns_AA dns_RD dns_RA dns_rejected ssl_version ssl_cipher ssl_resumed ssl_established ssl_subject ssl_issuer http_trans_depth http_method http_uri http_referrer http_version  http_request_body_len  http_response_body_len  http_status_code http_user_agent http_orig_mime_types http_resp_mime_types weird_name weird_addl weird_notice  label type
1556145104 192.168.1.30      3050 192.168.1.194      3050   tcp       -  0.000074          0          0        REJ             0         1            40         1            40         -           0          0          0      -      -      -            -           -          -           -               -           -          -                -           -        -             -            -                      0                       0                 0               -                    -                    -          -          -            -      1  dos
1556145104 192.168.1.30      3050 192.168.1.194      3050   tcp       -  0.000010          0          0        REJ             0         1            40         1            40         -           0          0          0      -      -      -            -           -          -           -               -           -          -                -           -        -             -            -                      0                       0                 0               -                    -                    -          -          -            -      1  dos
1556145104 192.168.1.30      3050 192.168.1.194      3050   tcp       -  0.000014          0          0        REJ             0         1            40         1            40         -           0          0          0      -      -      -            -           -          -           -               -           -          -                -           -        -             -            -                      0                       0                 0               -                    -                    -          -          -            -      1  dos
1556145104 192.168.1.30      3050 192.168.1.193      3050   tcp       -  0.000014          0          0        REJ             0         1            40         1            40         -           0          0          0      -      -      -            -           -          -           -               -           -          -                -           -        -             -            -                      0                       0                 0               -                    -                    -          -          -            -      1  dos
1556145104 192.168.1.30      3050 192.168.1.194      3050   tcp       -  0.000018          0          0        REJ             0         1            40         1            40         -           0          0          0      -      -      -            -           -          -           -               -           -          -                -           -        -             -            -                      0                       0                 0               -                    -                    -          -          -            -      1  dos
- Missing values in sample:
- None in sampled rows
- Basic statistics for numeric features:
                count          mean          std           min           max
ts            10000.0  1.556145e+09    22.525272  1.556145e+09  1.556145e+09
src_port      10000.0  4.207148e+03  7270.275595  8.000000e+01  6.274300e+04
dst_port      10000.0  3.062135e+03  1915.517552  5.300000e+01  6.274300e+04
duration      10000.0  4.734732e-02     3.029006  1.000000e-06  2.935032e+02
src_bytes     10000.0  3.844800e+00    95.371757  0.000000e+00  5.116000e+03
dst_bytes     10000.0  5.577800e+00   121.259527  0.000000e+00  3.978000e+03
missed_bytes  10000.0  0.000000e+00     0.000000  0.000000e+00  0.000000e+00
src_pkts      10000.0  6.468200e+00    26.665496  1.000000e+00  2.000000e+02
src_ip_bytes  10000.0  2.622028e+02  1071.792482  4.000000e+01  8.000000e+03
dst_pkts      10000.0  9.710000e-01     0.507725  0.000000e+00  3.800000e+01

### Attack Type Analysis
- DDoS present: Yes
- DDoS-related labels: ddos
- Class distribution:
- normal: 9077316
- scanning: 7254932
- ddos: 6473604
- dos: 3592545
- xss: 2161528
- password: 2126433
- backdoor: 1013367
- injection: 711369
- ransomware: 118485
- mitm: 1403

### Feature Analysis
- Representative file: `D:\ddos dataset\TON_IoT Dataset\Processed_datasets\Processed_datasets\Processed_Network_dataset\Network_dataset_1.csv`
- Number of features: 46
- Numeric feature count: 18
- Categorical feature count: 28
- Numeric features:
  - ts
  - src_port
  - dst_port
  - duration
  - src_bytes
  - dst_bytes
  - missed_bytes
  - src_pkts
  - src_ip_bytes
  - dst_pkts
  - dst_ip_bytes
  - dns_qclass
  - dns_qtype
  - dns_rcode
  - http_request_body_len
  - http_response_body_len
  - http_status_code
  - label
- Categorical features:
  - src_ip
  - dst_ip
  - proto
  - service
  - conn_state
  - dns_query
  - dns_AA
  - dns_RD
  - dns_RA
  - dns_rejected
  - ssl_version
  - ssl_cipher
  - ssl_resumed
  - ssl_established
  - ssl_subject
  - ssl_issuer
  - http_trans_depth
  - http_method
  - http_uri
  - http_referrer
  - http_version
  - http_user_agent
  - http_orig_mime_types
  - http_resp_mime_types
  - weird_name
  - weird_addl
  - weird_notice
  - type

## Dataset: BoT-IOT
- Path: `D:\ddos dataset\BoT-IOT`
- Total files: 84
- Total subfolders: 6
- File types:
- .csv: 82
- .docx: 1
- .xlsx: 1

### Folder Structure
```text
BoT-IOT
|-- 5%
|   |-- 10-best features
|   |   |-- 10-best Training-Testing split
|   |   |   |-- UNSW_2018_IoT_Botnet_Final_10_best_Testing.csv
|   |   |   `-- UNSW_2018_IoT_Botnet_Final_10_best_Training.csv
|   |   `-- UNSW_2018_IoT_Botnet_Final_10_Best.csv
|   `-- All features
|       |-- UNSW_2018_IoT_Botnet_Full5pc_1.csv
|       |-- UNSW_2018_IoT_Botnet_Full5pc_2.csv
|       |-- UNSW_2018_IoT_Botnet_Full5pc_3.csv
|       `-- UNSW_2018_IoT_Botnet_Full5pc_4.csv
|-- Entire Dataset
|   |-- UNSW_2018_IoT_Botnet_Dataset_1.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_10.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_11.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_12.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_13.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_14.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_15.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_16.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_17.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_18.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_19.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_2.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_20.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_21.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_22.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_23.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_24.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_25.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_26.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_27.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_28.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_29.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_3.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_30.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_31.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_32.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_33.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_34.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_35.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_36.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_37.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_38.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_39.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_4.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_40.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_41.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_42.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_43.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_44.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_45.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_46.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_47.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_48.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_49.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_5.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_50.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_51.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_52.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_53.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_54.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_55.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_56.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_57.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_58.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_59.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_6.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_60.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_61.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_62.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_63.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_64.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_65.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_66.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_67.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_68.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_69.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_7.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_70.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_71.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_72.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_73.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_74.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_8.csv
|   |-- UNSW_2018_IoT_Botnet_Dataset_9.csv
|   `-- UNSW_2018_IoT_Botnet_Dataset_Feature_Names.csv
|-- Features Explanation
|   `-- Total Feature Description.xlsx
`-- BOT_IOT_Dataset Details.docx
```

### Schema Inspection
#### Sample File: `D:\ddos dataset\BoT-IOT\5%\10-best features\10-best Training-Testing split\UNSW_2018_IoT_Botnet_Final_10_best_Testing.csv`
- Delimiter: `,`
- Estimated rows: 733705
- Number of features: 19
- Label column: `subcategory`
- Numeric features: 12
- Categorical features: 7
- Columns:
  - pkSeqID
  - proto
  - saddr
  - sport
  - daddr
  - dport
  - seq
  - stddev
  - N_IN_Conn_P_SrcIP
  - min
  - state_number
  - mean
  - N_IN_Conn_P_DstIP
  - drate
  - srate
  - max
  - attack
  - category
  - subcategory
- Sample attack categories:
  - TCP
  - UDP
- Sample rows:
 pkSeqID proto           saddr  sport         daddr  dport    seq   stddev  N_IN_Conn_P_SrcIP      min  state_number     mean  N_IN_Conn_P_DstIP    drate    srate      max  attack category subcategory
  792371   udp 192.168.100.150  48516 192.168.100.3     80 175094 0.226784                100 4.100436             4 4.457383                100 0.000000 0.404711 4.719438       1      DoS         UDP
 2056418   tcp 192.168.100.148  22267 192.168.100.3     80 143024 0.451998                100 3.439257             1 3.806172                100 0.225077 0.401397 4.442930       1     DDoS         TCP
 2795650   udp 192.168.100.149  28629 192.168.100.3     80 167033 1.931553                 73 0.000000             4 2.731204                100 0.000000 0.407287 4.138455       1     DDoS         UDP
 2118009   tcp 192.168.100.148  42142 192.168.100.3     80 204615 0.428798                 56 3.271411             1 3.626428                100 0.000000 0.343654 4.229700       1     DDoS         TCP
  303688   tcp 192.168.100.149   1645 192.168.100.5     80  40058 2.058381                100 0.000000             3 1.188407                100 0.000000 0.135842 4.753628       1      DoS         TCP
- Missing values in sample:
- None in sampled rows
- Basic statistics for numeric features:
                     count          mean           std    min           max
pkSeqID            10000.0  1.838504e+06  1.054068e+06  947.0  3.668506e+06
seq                10000.0  1.215411e+05  7.542232e+04   26.0  2.620320e+05
stddev             10000.0  8.987575e-01  8.046018e-01    0.0  2.489439e+00
N_IN_Conn_P_SrcIP  10000.0  8.240700e+01  2.445447e+01    1.0  1.000000e+02
min                10000.0  1.010300e+00  1.479796e+00    0.0  4.946456e+00
state_number       10000.0  3.142700e+00  1.180371e+00    1.0  7.000000e+00
mean               10000.0  2.244272e+00  1.511693e+00    0.0  4.964979e+00
N_IN_Conn_P_DstIP  10000.0  9.254640e+01  1.803576e+01    2.0  1.000000e+02
drate              10000.0  3.686265e-01  1.570408e+01    0.0  1.376463e+03
srate              10000.0  1.015432e+00  2.139716e+01    0.0  1.424501e+03

#### Sample File: `D:\ddos dataset\BoT-IOT\5%\10-best features\10-best Training-Testing split\UNSW_2018_IoT_Botnet_Final_10_best_Training.csv`
- Delimiter: `,`
- Estimated rows: 2934817
- Number of features: 19
- Label column: `subcategory`
- Numeric features: 12
- Categorical features: 7
- Columns:
  - pkSeqID
  - proto
  - saddr
  - sport
  - daddr
  - dport
  - seq
  - stddev
  - N_IN_Conn_P_SrcIP
  - min
  - state_number
  - mean
  - N_IN_Conn_P_DstIP
  - drate
  - srate
  - max
  - attack
  - category
  - subcategory
- Sample attack categories:
  - TCP
  - UDP
- Sample rows:
 pkSeqID proto           saddr  sport         daddr  dport    seq   stddev  N_IN_Conn_P_SrcIP      min  state_number     mean  N_IN_Conn_P_DstIP  drate    srate      max  attack category subcategory
 3142762   udp 192.168.100.150   6551 192.168.100.3     80 251984 1.900363                100 0.000000             4 2.687519                100    0.0 0.494549 4.031619       1     DDoS         UDP
 2432264   tcp 192.168.100.150   5532 192.168.100.3     80 256724 0.078003                 38 3.856930             3 3.934927                100    0.0 0.256493 4.012924       1     DDoS         TCP
 1976315   tcp 192.168.100.147  27165 192.168.100.3     80  62921 0.268666                100 2.974100             3 3.341429                100    0.0 0.294880 3.609205       1     DDoS         TCP
 1240757   udp 192.168.100.150  48719 192.168.100.3     80  99168 1.823185                 63 0.000000             4 3.222832                 63    0.0 0.461435 4.942302       1      DoS         UDP
 3257991   udp 192.168.100.147  22461 192.168.100.3     80 105063 0.822418                100 2.979995             4 3.983222                100    0.0 1.002999 4.994452       1     DDoS         UDP
- Missing values in sample:
- None in sampled rows
- Basic statistics for numeric features:
                     count          mean           std    min           max
pkSeqID            10000.0  1.829377e+06  1.062178e+06  339.0  3.667656e+06
seq                10000.0  1.196000e+05  7.548453e+04    1.0  2.621150e+05
stddev             10000.0  8.780141e-01  8.039522e-01    0.0  2.429816e+00
N_IN_Conn_P_SrcIP  10000.0  8.268180e+01  2.423241e+01    1.0  1.000000e+02
min                10000.0  1.007699e+00  1.480967e+00    0.0  4.787175e+00
state_number       10000.0  3.133900e+00  1.195121e+00    1.0  7.000000e+00
mean               10000.0  2.213598e+00  1.522207e+00    0.0  4.947914e+00
N_IN_Conn_P_DstIP  10000.0  9.248680e+01  1.817973e+01    1.0  1.000000e+02
drate              10000.0  6.858314e-01  4.352832e+01    0.0  4.291846e+03
srate              10000.0  2.901126e+00  1.262940e+02    0.0  8.333334e+03

### Attack Type Analysis
- DDoS present: No
- DDoS-related labels: None detected
- Class distribution:
- UDP: 5943690
- TCP: 4779540
- Service_Scan: 219504
- OS_Fingerprint: 53742
- HTTP: 7422
- Normal: 1431
- Keylogging: 219
- Data_Exfiltration: 18
- Notes:
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_1.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_10.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_11.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_12.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_13.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_14.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_15.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_16.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_17.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_18.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_19.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_2.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_20.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_21.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_22.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_23.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_24.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_25.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_26.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_27.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_28.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_29.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_3.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_30.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_31.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_32.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_33.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_34.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_35.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_36.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_37.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_38.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_39.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_4.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_40.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_41.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_42.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_43.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_44.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_45.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_46.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_47.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_48.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_49.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_5.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_50.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_51.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_52.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_53.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_54.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_55.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_56.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_57.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_58.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_59.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_6.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_60.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_61.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_62.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_63.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_64.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_65.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_66.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_67.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_68.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_69.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_7.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_70.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_71.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_72.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_73.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_74.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_8.csv
  - No label-like column detected in UNSW_2018_IoT_Botnet_Dataset_9.csv

### Feature Analysis
- Representative file: `D:\ddos dataset\BoT-IOT\5%\10-best features\10-best Training-Testing split\UNSW_2018_IoT_Botnet_Final_10_best_Testing.csv`
- Number of features: 19
- Numeric feature count: 12
- Categorical feature count: 7
- Numeric features:
  - pkSeqID
  - seq
  - stddev
  - N_IN_Conn_P_SrcIP
  - min
  - state_number
  - mean
  - N_IN_Conn_P_DstIP
  - drate
  - srate
  - max
  - attack
- Categorical features:
  - proto
  - saddr
  - sport
  - daddr
  - dport
  - category
  - subcategory

## Strategy Recommendation
1. Extract DDoS traffic by dataset-specific rules:
   - CIC_IOT_Dataset2023: derive the label from the parent folder name and keep folders starting with `DDoS-`.
   - CICDDoS2019: keep rows whose `Label` contains DDoS families such as `DrDoS_*`, `UDP`, `Syn`, `TFTP`, `Portmap`, and `UDPLag` based on your protocol scope.
   - TON_IoT Dataset: keep rows where `type == ddos`; discard or separately archive other attack classes.
   - BoT-IOT: treat `category == DoS` as related traffic, but validate whether it matches your DDoS definition before mixing it with reflection/flood datasets.

2. Unify labels to a common schema such as:
   - `binary_label`: `ddos` or `benign`
   - `attack_family`: original dataset family name such as `DrDoS_DNS`, `DDoS-SYN_Flood`, or `ddos`
   - `source_dataset`: dataset identifier

3. Handle non-DDoS attack types by removing them for binary DDoS detection or storing them as a third `other_attack` class if you want open-set evaluation.

4. Preprocessing strategy:
   - remove obvious index columns such as `Unnamed: 0`
   - normalize column names to lowercase snake_case
   - cast labels consistently
   - impute or flag missing values before scaling
   - split by source file or capture session to reduce leakage

5. Feature alignment strategy:
   - keep dataset-specific models if feature overlap is low
   - otherwise intersect shared flow features across datasets
   - document delimiter, units, and feature meaning before merging
   - avoid naive concatenation of unrelated schemas such as TON-IoT network logs and CIC flow statistics
