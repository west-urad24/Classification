①KaggleからBeginner's Classification Datasetをダウンロードする。  
②データの説明  
age,interest,success(0:blue、1:red)というラベルがある。  
年齢と興味の度合いによって新しいスポーツを学んだ場合、成功するかしないかを示したデータセットである。
(例)  
|  Age  |  Interest  |  Success  |
| ---- | ---- | ---- |
|  20  |  80  | 1 |
|  50  |  10  | 0 |

③データを決定木、ランダムフォレスト、サポートベクトルマシン、ロジスティック回帰、KNNで評価。  
結果をheatmapで可視化
