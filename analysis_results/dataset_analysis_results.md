# Dataset Analysis Results

## Dataset Comparison
```text
        Dataset  Samples     DDoS  Benign  Features
     CICIoT2023 35615862 34517671 1098191        39
    CICDDoS2019  6402137  6397818    4319        82
         TONIoT  1257606  1008774  248832        19
BoTIoT_optional  3300520  3300520       0        14
```

## Class Imbalance Discussion
- CICIoT2023: DDoS/Benign ratio = 31.43
- CICDDoS2019: DDoS/Benign ratio = 1481.32
- TONIoT: DDoS/Benign ratio = 4.05

## Feature Statistics
### CICIoT2023
- Top skewed features:
  - ack_count
  - arp
  - avg
  - cwr_flag_number
  - dhcp
  - dns
  - ece_flag_number
  - fin_count
  - fin_flag_number
  - header_length
- Summary statistics preview:
```text
                       mean         std       min        max       skew
ack_count         48.012280    6.063616   3.00000    93.0000  -1.827722
ack_flag_number    0.482421    0.054950   0.09000     0.9400  -0.929095
arp                0.011227    0.019202   0.00000     0.1900   3.714731
avg              889.423822  106.876679  80.88993  1082.8906  -4.170875
cwr_flag_number    0.000026    0.000510   0.00000     0.0100  19.489884
dhcp               0.000357    0.002669   0.00000     0.0400   9.855740
dns                0.005065    0.012271   0.00000     0.1300   4.293176
ece_flag_number    0.000058    0.000761   0.00000     0.0100  12.988887
fin_count          0.098088    0.406364   0.00000     5.0000   6.005137
fin_flag_number    0.000984    0.004080   0.00000     0.0500   6.013326
```
- Top feature importance preview:
```text
        feature  importance
      ack_count    0.200080
         number    0.166740
        tot_sum    0.133016
  header_length    0.113117
          https    0.104432
            tcp    0.044587
ack_flag_number    0.035338
psh_flag_number    0.034785
   time_to_live    0.030570
           rate    0.025303
```

### CICDDoS2019
- Top skewed features:
  - ack_flag_count
  - act_data_pkt_fwd
  - active_max
  - active_mean
  - active_min
  - average_packet_size
  - avg_bwd_segment_size
  - avg_fwd_segment_size
  - bwd_header_length
  - bwd_iat_max
- Summary statistics preview:
```text
                             mean         std  min           max       skew
ack_flag_count           0.001980    0.044453  0.0      1.000000  22.406662
act_data_pkt_fwd         9.518356   39.135715  0.0    199.000000   4.425845
active_max              31.686836  940.710968  0.0  28442.064000  29.816912
active_mean             31.185051  925.948281  0.0  27988.524000  29.807029
active_min              28.837901  864.138661  0.0  26418.017000  30.088725
active_std               0.000000    0.000000  0.0      0.000000   0.000000
average_packet_size   1985.468298  568.181470  0.0   2208.000000  -2.418644
avg_bwd_segment_size     0.489114    8.054865  0.0    185.286429  18.815887
avg_fwd_segment_size  1330.699988  361.843886  0.0   1472.000000  -2.454703
bwd_avg_bulk_rate        0.000000    0.000000  0.0      0.000000   0.000000
```
- Top feature importance preview:
```text
                    feature  importance
          min_packet_length    0.129196
      fwd_packet_length_min    0.104283
     fwd_packet_length_mean    0.099063
               flow_bytes/s    0.066499
         packet_length_mean    0.066011
       avg_fwd_segment_size    0.065343
          subflow_fwd_bytes    0.055807
      fwd_packet_length_max    0.051725
        average_packet_size    0.047633
total_length_of_fwd_packets    0.042131
```

### TONIoT
- Top skewed features:
  - dns_qclass
  - dns_qtype
  - dst_bytes
  - dst_ip_bytes
  - dst_pkts
  - dst_port
  - duration
  - http_response_body_len
  - missed_bytes
  - src_bytes
- Summary statistics preview:
```text
                                mean           std  min          max       skew
dns_qclass                279.012440   3010.032915  0.0  32769.00000  10.701360
dns_qtype                   5.029225     27.764522  0.0    255.00000   8.339755
dns_rcode                   0.000000      0.000000  0.0      0.00000   0.000000
dst_bytes                 107.157240   1082.232889  0.0  28022.00000  21.635648
dst_ip_bytes               78.333810    472.684458  0.0  11391.00000  17.036096
dst_pkts                    0.315891      1.481198  0.0     27.00100  11.266505
dst_port                11974.920210  14098.118541  0.0  51782.00000   1.521127
duration                    6.214229     85.081974  0.0   2117.24609  20.344054
http_request_body_len       0.000000      0.000000  0.0      0.00000   0.000000
http_response_body_len      0.002360      0.068662  0.0      2.00000  29.059791
```
- Top feature importance preview:
```text
     feature  importance
dst_ip_bytes    0.267617
    dst_pkts    0.183071
    dst_port    0.168446
src_ip_bytes    0.103623
    duration    0.082018
    src_pkts    0.066577
    src_port    0.042756
   dst_bytes    0.035583
   src_bytes    0.019537
   dns_qtype    0.013928
```

## Strengths and Weaknesses
- CICIoT2023: very large IoT-focused DDoS corpus with many DDoS families, but highly imbalanced and feature schema is specific to this dataset.
- CICDDoS2019: strong network-flow benchmark with rich features, but the benign class is extremely small in the processed output and may limit fair evaluation.
- TONIoT: contains both normal and DDoS samples with a more balanced cleaned subset than CICDDoS2019, but fewer numeric features after strict cleaning.
- BoTIoT optional: useful for auxiliary DoS/botnet behavior analysis, but it remains unsuitable as a primary benign-vs-DDoS benchmark because the optional output has no benign class.

## Output Notes
- Summary CSV: `D:\ddos dataset\analysis_results\dataset_summary.csv`
- Figures directory: `D:\ddos dataset\analysis_results\figures`
- Feature distribution figures: `D:\ddos dataset\analysis_results\figures\feature_distribution`