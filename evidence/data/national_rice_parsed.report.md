# national_rice_parsed.csv — parsing report

- rows: 7883
- 国审 rows: 2396, 省审 rows: 4780, no approval no.: 707
- Winall-affiliated rows (荃银 in source/applicant): 205 (国审 139)

## Field coverage (% non-missing, all rows)
variety                      100.0
approval_no                  100.0
approval_year                 91.0
level                        100.0
province                     100.0
is_hybrid                    100.0
three_line                   100.0
two_line                     100.0
subspecies                   100.0
season_hint                  100.0
region_group                 100.0
yield_2yr_kg_mu               47.8
yield_gain_pct                42.9
ck                           100.0
yield_prod_kg_mu              61.5
gain_prod_pct                 65.6
duration_d                    69.7
duration_diff_d               25.1
plant_height_cm               79.3
panicles_10k_mu               72.5
panicle_len_cm                62.0
grains_per_panicle            64.4
seed_setting_pct              85.9
tgw_g                         83.0
blast_index_mean               6.7
blast_index_max                6.7
neck_blast_loss_max_grade     19.7
blast_text                   100.0
blb_grade                     25.6
blb_text                     100.0
bph_grade                     21.4
heat_text                    100.0
cold_text                    100.0
head_rice_pct                 71.9
chalkiness_deg_pct            70.2
chalky_grain_pct              44.5
amylose_pct                   68.6
gel_mm                        70.9
lw_ratio                      70.7
alkali                        28.5
quality_grade                 35.8
quality_std                  100.0
is_winall                    100.0
applicant                    100.0
source_text_len              100.0

## Field coverage (% non-missing, 国审 rows with approval year >= 2005)
variety                      100.0
approval_no                  100.0
approval_year                100.0
level                        100.0
province                     100.0
is_hybrid                    100.0
three_line                   100.0
two_line                     100.0
subspecies                   100.0
season_hint                  100.0
region_group                 100.0
yield_2yr_kg_mu               95.6
yield_gain_pct                79.1
ck                           100.0
yield_prod_kg_mu              84.6
gain_prod_pct                 91.4
duration_d                    99.3
duration_diff_d               33.1
plant_height_cm               99.2
panicles_10k_mu               94.6
panicle_len_cm                99.4
grains_per_panicle            93.3
seed_setting_pct              99.3
tgw_g                         99.5
blast_index_mean              14.7
blast_index_max               14.7
neck_blast_loss_max_grade     65.7
blast_text                   100.0
blb_grade                     59.7
blb_text                     100.0
bph_grade                     72.0
heat_text                    100.0
cold_text                    100.0
head_rice_pct                 99.0
chalkiness_deg_pct            97.7
chalky_grain_pct              50.4
amylose_pct                   96.8
gel_mm                        98.2
lw_ratio                      92.3
alkali                        45.0
quality_grade                 69.6
quality_std                  100.0
is_winall                    100.0
applicant                    100.0
source_text_len              100.0

## 国审 rows by year
approval_year
2001.0     18
2003.0     58
2004.0     63
2005.0     59
2006.0     85
2007.0     56
2008.0     21
2009.0     51
2010.0     55
2011.0     29
2012.0     44
2013.0     43
2014.0     46
2015.0     53
2016.0     66
2017.0    175
2018.0    234
2019.0    223
2020.0    306
2021.0    431
2022.0    132
2023.0     85
2024.0     61
2025.0      2

## Winall rows by year (all levels)
approval_year
2004.0     1
2006.0     3
2007.0     2
2008.0     3
2010.0     5
2012.0     2
2013.0     3
2014.0     1
2015.0     6
2016.0     6
2017.0    11
2018.0     6
2019.0    16
2020.0    60
2021.0    11
2022.0    34
2023.0    19
2024.0    15

## Notes
- Parsed by regex from announcement text (品种来源/特征特性/产量表现); no imputation.
- Source: he-zhui/Rice_QA (GitHub), jw/qa_data.json, derived from rice_extracted_fields.csv (approval announcements).
- Coverage of 2023–2025 approvals is thin in the source; supplement Winall 2023–2025 varieties from MARA announcements via WebSearch.