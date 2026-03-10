# Dataset Cleaning Report

## Processing Summary
- Objective: create cleaned DDoS-vs-benign research datasets without training any models.
- Label standardization: `label = 0` for benign/normal, `label = 1` for DDoS.
- Feature cleaning: removed identifier columns, dropped non-numeric columns, coerced retained features to numeric, imputed missing numeric values with per-chunk medians then `0` fallback.

## Filtering Rules
- CIC_IOT_Dataset2023: folder-derived labels, keep `DDoS-*` folders plus `Benign_Final`.
- CICDDoS2019: keep rows with `label == BENIGN` or labels matching known DDoS families from the audit (`DrDoS_*`, `Syn`, `UDP`, `UDPLag`, `Portmap`, `TFTP`, `LDAP`, `MSSQL`, `NetBIOS`, `WebDDoS`).
- TON_IoT Dataset: keep only `type == ddos` or `type == normal` from processed IoT and processed network CSVs.
- BoT-IOT: excluded from the main unified dataset; saved separately as optional `DoS`-only data because the audit did not establish it as a clean DDoS benchmark.

## Dataset Statistics
### CIC_IOT_Dataset2023
- Output file: `D:\ddos dataset\processed_outputs\processed_CICIoT2023_ddos.csv`
- Source files used: summarized from existing processed output
- Total samples: 35615862
- DDoS samples: 34517671
- Benign samples: 1098191
- Number of cleaned numeric features: 39

### CICDDoS2019
- Output file: `D:\ddos dataset\processed_outputs\processed_CICDDoS2019_ddos.csv`
- Source files used: summarized from existing processed output
- Total samples: 6402137
- DDoS samples: 6397818
- Benign samples: 4319
- Number of cleaned numeric features: 82

### TON_IoT Dataset
- Output file: `D:\ddos dataset\processed_outputs\processed_TONIoT_ddos.csv`
- Source files used: summarized from existing processed output
- Total samples: 1257606
- DDoS samples: 1008774
- Benign samples: 248832
- Number of cleaned numeric features: 19

### BoT-IOT
- Output file: `D:\ddos dataset\processed_outputs\processed_BoTIoT_dos_optional.csv`
- Source files used: summarized from existing processed output
- Total samples: 3300520
- DDoS samples: 3300520
- Benign samples: 0
- Number of cleaned numeric features: 14

## Feature Alignment Report
- Shared features across `CIC_IOT_Dataset2023`, `CICDDoS2019`, and `TON_IoT Dataset` after strict numeric cleaning:
- None

- Pairwise shared features:
### CIC_IOT_Dataset2023 and CICDDoS2019
- None

### CICDDoS2019 and TON_IoT Dataset
- None

### CIC_IOT_Dataset2023 and TON_IoT Dataset
- None

## Constraint
- No robust exact-name numeric feature intersection exists across all three main datasets after strict identifier removal.
- Result: the saved processed CSVs are clean per-dataset research tables, but a single merged aligned table is intentionally not created in this step.
- Next step for true cross-dataset fusion would require explicit semantic feature mapping or learned representation alignment.
