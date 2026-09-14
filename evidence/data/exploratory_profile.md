# Exploratory profile: 国审 rice varieties 2005–2022 (parsed from announcements)

## Counts by year: Winall vs others (国审)
grp            Others  Winall  Winall_share_%
approval_year                                
2005.0             59       0             0.0
2006.0             84       1             1.2
2007.0             54       2             3.6
2008.0             20       1             4.8
2009.0             51       0             0.0
2010.0             52       3             5.5
2011.0             29       0             0.0
2012.0             42       2             4.5
2013.0             40       3             7.0
2014.0             46       0             0.0
2015.0             51       2             3.8
2016.0             66       0             0.0
2017.0            175       0             0.0
2018.0            233       1             0.4
2019.0            207      16             7.2
2020.0            257      49            16.0
2021.0            431       0             0.0
2022.0            106      26            19.7

## Trait means by period and group (indica only, hybrid only)
                  n  yield_kg_mu  gain_pct  duration_d  head_rice  chalk_deg  amylose    gel    lw q_le2_share neck_le5_share  two_line_share
period  grp                                                                                                                                  
2005-10 Others  201       552.29      4.30      134.12      59.49       6.43    20.43  64.61  2.91    0.384615            NaN            0.23
        Winall    7       546.26      5.76      122.21      59.47       4.54    18.74  64.57  3.03    0.333333            NaN            0.71
2011-16 Others  216       580.37      5.35      136.66      58.17       6.17    18.48  71.78  2.95    0.247059            0.0            0.46
        Winall    7       571.50       NaN      128.71      56.46       6.86    17.59  70.43  3.03         0.0            NaN            0.86
2017-19 Others  542       628.35      4.51      136.62      60.96       3.96    16.09  72.08  3.16    0.428954       0.478261            0.62
        Winall   17       615.51      4.05      133.90      63.58       2.33    15.22  75.28  3.14    0.533333            0.6            0.29
2020-22 Others  671       636.26      4.28      135.22      62.44       2.78    16.44  68.46  3.32    0.647597       0.658385            0.55
        Winall   74       636.55      4.11      135.74      63.34       2.25    16.29  71.37  3.13    0.659091       0.790323            0.43

## Winall 国审 varieties: two-line vs three-line by period
col_0    three_line  two_line
period                       
2005-10           2         5
2011-16           1         6
2017-19          12         5
2020-22          42        32

## Region groups of Winall 国审 varieties (top 10)
region_group
长江中下游中籼迟熟组     48
长江上游中籼迟熟组      26
长江中下游晚籼早熟组     11
华南感光晚籼组         5
长江中下游麦茬籼稻组      3
华南早籼组           3
长江中下游晚籼中迟熟组     2
长江中下游早熟晚籼组      1

## Applicant/breeder strings for Winall rows (top 8)
applicant
安徽荃银高科种业股份有限公司    41
安徽荃银超大种业有限公司       7
湖北荃银高科种业有限公司       6
江苏中江种业股份有限公司       5
中国种子集团有限公司         4
安徽荃银欣隆种业有限公司       4
安徽喜多收种业科技有限公司      3
江西天涯种业有限公司         3
## ⚠ Coverage caveats (must be addressed before any inference)
- The source compilation is incomplete by year: Winall has 0 国审 rows in 2016, 2017 and 2021 and only 1 in 2018, although company disclosures report national approvals in those years (e.g., 2021 was a peak approval year nationally: 431 rows here but no Winall rows). Missingness is therefore not random with respect to applicant/year.
- 2023–2025 approvals are almost absent (105/82/10 rows overall). Winall's 2023–2025 国审 varieties (52 hybrid rice in 2025 alone per the 2025 annual report) must be supplemented from MARA approval announcements via WebSearch (variety name → 审定公告 → 区试 fields).
- `blast_index_mean` is available for only ~15% of 国审 rows; `neck_blast_loss_max_grade` (~66%) is the more usable resistance variable. Quality grade text is heterogeneous; parsed `quality_grade` covers ~57% and needs spot-checking.
- Applicant attribution: "荃银" in 品种来源/选育单位/申请者; joint applications (e.g., 江苏中江种业, 中国种子集团) are counted as Winall-affiliated — decide a rule (lead applicant vs any) before analysis.
