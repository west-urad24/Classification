[参考書](https://www.amazon.co.jp/作ってわかる-自然言語処理AI〜BERT・GPT2・NLPプログラミング入門-坂本-俊之/dp/4863543700)を用いてBERTモデルを作成します。  
クラス分類や要約のタスクを投稿していく予定です。また、様々な論文を読んで自分なりのアプローチを考えていきます。

# 準備(cpu環境)
※jawiki-latest-pages-articles.xml.bz2、wiki_text、wiki_contents、wiki_encode24kはデータ量の関係からgithub上に入れていません。  
## トークンのリストを入手  
①トークナイズされた文書と絵文字のファイルをダウンロード  
wget https://github.com/tanreinama/Japanese-BPEEncoder_V2/raw/master/ja-swe24k.txt  
wget https://github.com/tanreinama/Japanese-BPEEncoder_V2/raw/master/emoji.json  

②wikipediaコーパスをダウンロード(しばらく時間かかります)  
wget https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2  
  
③pip3コマンドで「wikiextractor」をインストール  
pip3 install wikiextractor  

④②のXMLファイルを展開し、wiki_textというフォルダを自動作成  
python3 -m wikiextractor.WikiExtractor jawiki-latest-pages-articles.xml.bz2 -o wiki_text  

⑤wiki_textファイルをコンテンツごとに保存  
python3 wiki_copy.py --src_dir wiki_text --dst_dir wiki_contents  

⑥エンコード済みファイルの作成  
python3 encode_swe.py --vocabulary ja-swe24k.txt --src_dir wiki_contents --dst_file wiki_encode24k  

これでTransformerモデルの事前学習を行えます。
