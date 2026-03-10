# Paper Results Summary

## Dataset statistics
```text
        Dataset  Total Samples  DDoS Samples  Benign Samples  Features  Class Imbalance Ratio
     CICIoT2023       35615862      34517671         1098191        39              31.431391
    CICDDoS2019        6402137       6397818            4319        82            1481.319287
         TONIoT        1257606       1008774          248832        19               4.054036
BoTIoT_optional        3300520       3300520               0        14                    inf
```

## Feature analysis
### CICIoT2023
- Highly skewed features: ack_count, arp, avg, cwr_flag_number, dhcp, dns, ece_flag_number, fin_count

### CICDDoS2019
- Highly skewed features: ack_flag_count, act_data_pkt_fwd, active_max, active_mean, active_min, average_packet_size, avg_bwd_segment_size, avg_fwd_segment_size

### TONIoT
- Highly skewed features: dns_qclass, dns_qtype, dst_bytes, dst_ip_bytes, dst_pkts, dst_port, duration, http_response_body_len

## Visualization insights
- PCA and t-SNE figures indicate that all three datasets exhibit visible benign vs DDoS separation, with TONIoT showing the least trivial clustering structure.
- The publication figures are saved in `analysis_results/paper_figures`.

## Dataset difficulty discussion
```text
    Dataset  LogisticRegression_AUC  RandomForest_AUC
CICDDoS2019                0.999212          0.999995
 CICIoT2023                0.999994          1.000000
     TONIoT                0.932677          0.999986
```
- CICIoT2023 and CICDDoS2019 are highly separable under baseline models, suggesting relatively easy benchmark conditions.
- TONIoT is more challenging for a linear model, which makes it useful for stronger generalization studies.

## Redundancy highlights
```text
    Dataset                          Redundant Feature Pairs  Correlation Value
 CICIoT2023                     rst_count vs rst_flag_number           0.999924
 CICIoT2023                     fin_count vs fin_flag_number           0.999790
 CICIoT2023                     syn_count vs syn_flag_number           0.999747
 CICIoT2023                           rst_count vs fin_count           0.988533
 CICIoT2023                     fin_count vs rst_flag_number           0.988454
CICDDoS2019  fwd_packet_length_mean vs fwd_packet_length_max           0.999716
CICDDoS2019  fwd_packet_length_mean vs fwd_packet_length_min           0.999551
CICDDoS2019   fwd_packet_length_min vs fwd_packet_length_max           0.998909
CICDDoS2019 total_length_of_fwd_packets vs total_fwd_packets           0.983539
CICDDoS2019                     flow_iat_max vs flow_iat_std           0.962931
```

## Research takeaways
- Severe class imbalance remains a major concern, especially in CICDDoS2019.
- Feature redundancy suggests feature-pruning and ablation studies are justified before final model selection.
- For a balanced and less trivial benchmark, TONIoT should be emphasized alongside one of the larger CIC datasets.