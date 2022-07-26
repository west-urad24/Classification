①Kaggleからmushrooms.csvをダウンロード  
# 目的関数 
## classes: 
○edible(食用)=e, poisonous(毒)=p


# 特徴量
## cap-shape:  
○形状：ベル= b、円錐= c、凸= x、フラット= f、こぶ= k、沈み= s  


## cap-surface:  
○表面：繊維状= f、溝= g、うろこ状= y、滑らか= s  


## cap-color:  
○色：ブラウン= n、バフ= b、シナモン= c、グレー= g、グリーン= r、ピンク= p、パープル= u、レッド= e、ホワイト= w、イエロー= y  


## bruises:  
○あざ：あざ= t、あざがない = f  


## odor:  
○におい：アーモンド= a、アニス= l、クレオソート= c、フィッシュ= y、ファウル= f、ムスティ= m、なし= n、辛味= p、スパイシー= s  


## gill-attachment: 
○ひだの付着物：付いていた=a、減っている=d、付いてない=f、傷がある=n

## gill-spacing: 
○ひだの間隔: 近い=c、混雑=w、遠い=d


## gill-size:  
○ひだのサイズ: 広い = b, 狭い = n  


## gill-color:  
○ひだの色：黒= k、茶色= n、バフ= b、チョコレート= h、灰色= g、緑= r、オレンジ= o、ピンク= p、紫= u、赤= e、白= w、黄色= y  


## stalk-shape: 
○茎の形：太い= e、細い= t


## stalk-root: 
○茎の根：球根状 = b、太くて重い = c、杯状 = u、均等 = e、菌糸束 = z、根づいている = r、不明 =？


## stalk-surface-above-ring:  
○リングの上の茎の表面：繊維状= f、うろこ状= y、絹のような= k、滑らかな= s  


## stalk-surface-below-ring:  
○リングの下の茎の表面：繊維状= f、うろこ状= y、絹のような= k、滑らかな= s  


## stalk-color-above-ring:  
○リングの上の茎の色：茶色= n、バフ= b、シナモン= c、灰色= g、オレンジ= o、ピンク= p、赤= e、白= w、黄色= y  


## stalk-color-below-ring:  
○リングの下の茎の色：茶色= n、バフ= b、シナモン= c、灰色= g、オレンジ= o、ピンク= p、赤= e、白= w、黄色= y  


## veil-type:  
○膜タイプ　部分的=p、普遍的= u  


## veil-color:  
○膜の色：茶色= n、オレンジ= o、白= w、黄色= y  


## ring-number:  
○リング番号：なし= n、1 = o、2 = t  


## ring-type: 
○リングタイプ：軽く薄い=c,次第に消えてゆく=e,派手=f,大きい=l,none=n,ペンダント=p,覆われている=s,帯=z


## spore-print-color:  
○胞子紋の色：黒= k、茶色= n、バフ= b、チョコレート= h、緑= r、オレンジ= o、紫= u、白= w、黄色= y  


## population:  
○人口　豊富な=a、クラスター化された= c、多数の= n、分散された= s、いくつかの= v、孤立した= y  


## habitat:  
○生息地　草=g、葉= l、牧草地= m、小道= p、都市= u、廃棄物= w、森= d
