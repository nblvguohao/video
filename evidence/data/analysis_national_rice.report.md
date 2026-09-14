# analysis_national_rice.csv — build report

- source rows: 7883 → 国审 rows: 2396 → after dedup by approval number: 2386
- approval years: 2001–2025 (0 rows without a parsable year)
- Winall-affiliated records: 139 by applicant field, 238 after adding the pedigree/name rule
- flagged yield outliers: 0; duration outliers: 0

## Records per year by applicant type
applicant_type  Enterprise  Joint  Public  Unknown
approval_year                                     
2001                     0      0      17        1
2003                     2      3      50        2
2004                     7      7      43        4
2005                     8      9      38        4
2006                    20      7      51        5
2007                     8      7      32        5
2008                     5      4      10        1
2009                     9      4      34        4
2010                    11     12      30        2
2011                    10      3      14        2
2012                    10      3      27        4
2013                    18      2      23        0
2014                    13      5      27        1
2015                    22      9      20        2
2016                     0      0       0       66
2017                     1      0       0      174
2018                     1      0       0      233
2019                   178     10      28        7
2020                   252     11      37        6
2021                     0      0       0      431
2022                   102      4      23        3
2023                    70      3      10        2
2024                    53      1       6        1
2025                     2      0       0        0

## Records by region
region
Middle-Lower Yangtze    1240
Upper Yangtze            515
Other/Unspecified        256
North/Huanghuai          191
South China              146
Wuling Mountains          38

## Records by season
season
Single/Mid     1670
Late            408
Early           194
Unspecified     114

## Records by breeding system
breeding_system
Three-line hybrid    1066
Two-line hybrid       971
Inbred/Other          339
Hybrid (unclear)       10

## Key variable coverage (% non-missing)
yield_2yr_kg_mu               92.8
yield_gain_pct                77.2
duration_d                    98.0
plant_height_cm               98.6
panicles_10k_mu               92.8
grains_per_panicle            92.8
seed_setting_pct              98.7
tgw_g                         98.8
head_rice_pct                 98.0
chalkiness_deg_pct            96.7
amylose_pct                   96.0
gel_mm                        97.6
lw_ratio                      90.9
quality_grade                 65.8
quality_stated               100.0
neck_blast_loss_max_grade     62.1
blast_index_mean              13.9
blb_grade                     59.8
bph_grade                     70.8

## Winall records per year (extended rule)
winall_source  applicant  applicant+pedigree  pedigree
approval_year                                         
2006                   0                   1         0
2007                   1                   1         0
2008                   0                   1         0
2010                   0                   3         0
2012                   0                   2         0
2013                   1                   2         0
2015                   0                   2         0
2016                   0                   0         1
2017                   0                   0        15
2018                   0                   1        23
2019                   4                  12         0
2020                  11                  38         0
2021                   0                   0        60
2022                   8                  18         0
2023                   4                  14         0
2024                   3                  12         0

## Caveats
- Applicant fields are absent from the source compilation for 2016, 2017, 2018 and 2021; those years appear entirely as applicant_type = Unknown. Winall records in those years are recovered by the pedigree/name rule (precision 1.000, recall 0.770 on labelled records), so counts there are lower bounds.
- Each row is one approval (variety x ecological region), not one variety: a variety approved for several regions contributes several rows, each with its own regional-trial data.
- All values are parsed verbatim from announcement text; missing values are left empty.