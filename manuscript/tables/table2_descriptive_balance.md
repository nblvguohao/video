# Table 2. Descriptive statistics and balance, main analysis stratum

Sample: national approvals (国审), two dominant mid-season indica trial groups (middle-and-lower-Yangtze; upper-Yangtze), 2017 and 2019-2022. n = 878 (Unified 406 / Consortium 405 / Green 67). Computed directly from `analysis_rice_channel.pkl` by `scripts/analysis/build_table2_descriptive.py`; means and SDs are reported on the non-missing observations for each cell, and the non-missing rate is reported separately so a reader can see where an arm's mean is based on a materially smaller effective sample (cf. Section 3.3 and Table 3's n columns).

| Outcome | Unified mean (SD) | Consortium mean (SD) | Green mean (SD) | Unified % non-missing | Consortium % non-missing | Green % non-missing |
|---|---|---|---|---|---|---|
| Head-rice percentage (%) | 63.130 (4.956) | 61.690 (5.577) | 60.989 (4.187) | 98.8 | 99.3 | 91.0 |
| Chalkiness degree (%) | 2.211 (1.925) | 3.246 (3.022) | 5.521 (3.334) | 98.8 | 98.3 | 97.0 |
| Quality grade stated (0/1) | 0.874 (0.332) | 0.770 (0.421) | 0.463 (0.502) | 100.0 | 100.0 | 100.0 |
| Top-two quality grade (0/1) | 0.665 (0.473) | 0.635 (0.482) | 0.290 (0.461) | 87.4 | 77.0 | 46.3 |
| Amylose content (%) | 16.250 (2.054) | 16.120 (2.186) | 15.798 (2.486) | 97.8 | 95.8 | 97.0 |
| Gel consistency (mm) | 72.181 (8.561) | 69.095 (9.823) | 71.264 (12.493) | 97.5 | 97.0 | 100.0 |
| Grain length-width ratio | 3.212 (0.304) | 3.274 (0.356) | 3.112 (0.146) | 98.8 | 98.5 | 100.0 |
| Neck-blast tolerance OK (0/1) | 0.625 (0.485) | 0.608 (0.489) | -- | 82.8 | 94.6 | 0.0 |
| Bacterial-blight grade | 6.307 (1.379) | 6.057 (1.520) | 5.653 (1.751) | 69.7 | 69.6 | 73.1 |
| Regional-trial yield gain over check (pp) | 4.182 (2.443) | 4.646 (1.848) | 4.439 (1.971) | 77.1 | 99.8 | 40.3 |
| Production-trial yield gain over check (pp) | 4.462 (2.127) | 5.031 (2.089) | 5.075 (2.961) | 82.3 | 75.1 | 100.0 |
| Two-year regional-trial yield (kg/mu) | 645.771 (23.299) | 645.573 (20.065) | 657.860 (24.328) | 91.6 | 100.0 | 100.0 |
| Growth duration (days) | 140.554 (9.312) | 139.696 (9.465) | 141.166 (7.484) | 99.0 | 99.3 | 100.0 |
| Plant height (cm) | 117.693 (6.602) | 118.620 (6.675) | 118.793 (6.389) | 99.0 | 99.3 | 100.0 |
| Seed-setting percentage (%) | 83.883 (2.708) | 84.125 (2.991) | 84.319 (2.087) | 98.8 | 99.3 | 100.0 |
| Thousand-grain weight (g) | 25.591 (2.161) | 25.665 (2.264) | 26.961 (2.434) | 99.0 | 99.3 | 100.0 |
| Grains per panicle | 203.873 (18.950) | 198.817 (18.139) | 197.985 (16.714) | 96.6 | 97.3 | 98.5 |

Notes: `quality_stated` and `neck_blast_ok` and `quality_top2` are 0/1 indicators; their "mean" is the proportion coded 1. `quality_stated` is non-missing by construction (100% in every arm) because it is defined as the union of two underlying fields (Section 3.3). Non-missing-rate imbalances of 8 percentage points or more between Unified and Consortium are the same three flagged in Section 3.3/6.7 (Manski bounds, R7): `quality_top2`, `yield_gain_pct`, and `yield_2yr_kg_mu`. `bsys` (breeding-system fixed effect) and `trial_group` distributions by channel are reported in Table 1 and `table1_channel_by_year.csv`; they are not repeated here to avoid duplicating that table.
