# Advanced Dataset Analysis

## 1 Dataset visualization results
- PCA and t-SNE figures were generated for all three datasets after standardizing numeric features.
- Visualization sampling was capped for tractability, with t-SNE using a smaller subset due its computational cost.

## 2 Dataset separability comparison
```text
    Dataset              Model  accuracy  precision   recall  f1_score  roc_auc
 CICIoT2023 LogisticRegression  0.999917   1.000000 0.999914  0.999957 0.999994
CICDDoS2019 LogisticRegression  0.994221   0.999972 0.994245  0.997100 0.999212
     TONIoT LogisticRegression  0.951972   0.953852 0.987870  0.970563 0.932677
```

## 3 Feature entropy insights
```text
    Dataset                Feature  Entropy
 CICIoT2023                   rate 2.829638
 CICIoT2023          header_length 1.908826
 CICIoT2023          protocol_type 1.327684
 CICIoT2023                    tcp 1.252110
 CICIoT2023        ack_flag_number 0.993001
 CICIoT2023              ack_count 0.986231
 CICIoT2023                    udp 0.912270
 CICIoT2023        syn_flag_number 0.894969
 CICIoT2023              syn_count 0.855207
 CICIoT2023                   icmp 0.846372
CICDDoS2019       destination_port 4.321715
CICDDoS2019           flow_bytes/s 1.741359
CICDDoS2019          fwd_packets/s 1.372326
CICDDoS2019         flow_packets/s 1.301957
CICDDoS2019    average_packet_size 0.764769
CICDDoS2019  fwd_packet_length_min 0.758353
CICDDoS2019      min_packet_length 0.758353
CICDDoS2019     packet_length_mean 0.758329
CICDDoS2019 fwd_packet_length_mean 0.758296
CICDDoS2019   avg_fwd_segment_size 0.758296
     TONIoT               src_port 3.438557
     TONIoT               dst_pkts 2.259579
     TONIoT               duration 1.224946
     TONIoT               dst_port 0.773687
     TONIoT           dst_ip_bytes 0.493600
     TONIoT              dns_rcode 0.320177
     TONIoT              dns_qtype 0.159346
     TONIoT              src_bytes 0.082673
     TONIoT           src_ip_bytes 0.041146
     TONIoT             dns_qclass 0.014895
```

## 4 Feature redundancy discussion
```text
    Dataset                    Feature1              Feature2  Correlation
 CICIoT2023                   rst_count       rst_flag_number     0.999924
 CICIoT2023                   fin_count       fin_flag_number     0.999790
 CICIoT2023                   syn_count       syn_flag_number     0.999747
 CICIoT2023                   rst_count             fin_count     0.988533
 CICIoT2023                   fin_count       rst_flag_number     0.988454
 CICIoT2023             rst_flag_number       fin_flag_number     0.988275
 CICIoT2023                   rst_count       fin_flag_number     0.988270
 CICIoT2023                   ack_count       psh_flag_number     0.976307
CICDDoS2019      fwd_packet_length_mean fwd_packet_length_max     0.999716
CICDDoS2019      fwd_packet_length_mean fwd_packet_length_min     0.999551
CICDDoS2019       fwd_packet_length_min fwd_packet_length_max     0.998909
CICDDoS2019 total_length_of_fwd_packets     total_fwd_packets     0.983539
CICDDoS2019                flow_iat_max          flow_iat_std     0.962931
```

## 5 Dataset difficulty comparison
```text
    Dataset                  Model  accuracy  precision   recall  f1_score  roc_auc
 CICIoT2023     LogisticRegression  0.999917   1.000000 0.999914  0.999957 0.999994
 CICIoT2023 RandomForestClassifier  0.999972   0.999971 1.000000  0.999986 1.000000
CICDDoS2019     LogisticRegression  0.994221   0.999972 0.994245  0.997100 0.999212
CICDDoS2019 RandomForestClassifier  0.999944   0.999972 0.999972  0.999972 0.999995
     TONIoT     LogisticRegression  0.951972   0.953852 0.987870  0.970563 0.932677
     TONIoT RandomForestClassifier  0.998667   0.999272 0.999064  0.999168 0.999986
```

## 6 Implications for DDoS detection research
- Higher separability scores indicate that a linear or tree-based baseline can already distinguish benign and DDoS traffic well in that dataset.
- Strong redundancy suggests opportunities for feature pruning before downstream model training.
- Entropy highlights features with richer variability, which can be useful for interpreting discriminative network behavior.
- Differences between LogisticRegression and RandomForest performance indicate whether the decision boundary is closer to linear or nonlinear for each dataset.