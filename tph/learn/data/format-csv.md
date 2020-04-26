# 気象庁の過去の気象データ

## カラム名の説明
ダウンロードした CSVファイルの先頭の何行かにカラム情報が記述されているのだが、標準のCSVと異なるので、次の表の通り略称を決めた。

| カラム名 | 説明 | 単位 | 備考 |
|:-- |:-- |:-- |:-- |
| date | 日付 | yyyy/m/d | 年月日 |
| mean_t | 平均気温 | °C | mean temperature |
| mean_t_qi | 品質情報 | - | quality information |
| mean_t_hn | 均質番号 | - | homogeneity number |
| max_t | 最高気温 | °C | maximum temperature |
| max_t_qi | 品質情報 | - |  |
| max_t_hn | 均質番号 | - |  |
| min_t | 最低気温 | °C | minimum temperature |
| min_t_qi | 品質情報 | - |  |
| min_t_hn | 均質番号 | - |  |
| sum_rf | 降水量の合計 | mm | sum of rainfall |
| sum_rf_ni | 現象なし情報 | - |  |
| sum_rf_qi | 品質情報 | - |  |
| sum_rf_hn | 均質番号 | - |  |
| dh | 日照時間 | 時間 | the daylight hours |
| dh_ni | 現象なし情報 | - |  |
| dh_qi | 品質情報 | - |  |
| dh_hn | 均質番号 | - |  |
| sum_sf | 降雪量合計 | cm | sum of snowfall |
| sum_sf_ni | 現象なし情報 | - |  |
| sum_sf_qi | 品質情報 | - |  |
| sum_sf_hn | 均質番号 | - |  |
| mean_ws | 平均風速 | m/s | mean wind speed |
| mean_ws_qi | 品質情報 | - |  |
| mean_ws_hn | 均質番号 | - |  |
| most_wd | 最多風向 | 16方位 | most wind direction |
| most_wd_qi | 品質情報 | - |  |
| most_wd_hn | 均質番号 | - |  |
| mean_h | 平均湿度 | ％ | mean humidity |
| mean_h_qi | 品質情報 | - |  |
| mean_h_hn | 均質番号 | - |  |
| mean_p | 平均現地気圧 | hPa | mean pressure |
| mean_p_qi | 品質情報 | - |  |
| mean_p_hn | 均質番号 | - |  |
| mean_cc | 平均雲量 | 10分比 | mean cloud cover |
| mean_cc_qi | 品質情報 | - |  |
| mean_cc_hn | 均質番号 | - |  |
| gwc_day | 天気概況 | 昼：06時～18時 | general weather conditions |
| gwc_day_qi | 品質情報 | - |  |
| gwc_day_hn | 均質番号 | - |  |
| gwc_night | 天気概況 | 夜：18時～翌日06時 | general weather conditions |
| gwc_night_qi | 品質情報 | - |  |
| gwc_night_hn | 均質番号 | - |  |


## 品質情報の値と意味
| 値 | 記号 | 意味 |
|:--:|:--:|:-- |
| 8 | 値 | 統計のもととなるデータに欠損がない（正常値） |
| 5 | 値) | 統計を行う対象資料が許容範囲で欠けている（準正常値） |
| 4 | 値] | 統計を行う対象資料が許容範囲を超えて欠けている（資料不足値） |
| 2 | # | 値がかなり疑わしい（時別値のみが対象）（疑問値） |
| 1 | /// | 統計値がない（欠測） |
| 0 | 空 | 観測・統計項目ではない |

## 現象なし情報の値
| 値 | 記号 | 意味 |
|:--:|:--:|:-- |
| 1 | -- | 現象なし |
| 0 | 値 | 現象あり |


## タイトルカラム
コピーして利用する。
```csv
date,mean_t,mean_t_qi,mean_t_hn,max_t,max_t_qi,max_t_hn,min_t,min_t_qi,min_t_hn,sum_rf,sum_rf_ni,sum_rf_qi,sum_rf_hn,dh,dh_ni,dh_qi,dh_hn,sum_sf,sum_sf_ni,sum_sf_qi,sum_sf_hn,mean_ws,mean_ws_qi,mean_ws_hn,most_wd,most_wd_qi,most_wd_hn,mean_h,mean_h_qi,mean_h_hn,mean_p,mean_p_qi,mean_p_hn,mean_cc,mean_cc_qi,mean_cc_hn,gwc_day,gwc_day_qi,gwc_day_hn,gwc_night,gwc_night_qi,gwc_night_hn
```
