import os
import uuid
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--src_dir", help="source dir", required=True )#入力ファイル
parser.add_argument("--dst_dir", help="destnation dir", required=True )#結果のファイル
parser.add_argument("--max_articles", help="max num", default=-1, type=int )
args = parser.parse_args()

#保存先の空のファイルを作成
if not os.path.isdir(args.dst_dir):
    os.mkdir(args.dst_dir)
    for a in '0123456789abcdef':
        for b in '0123456789abcdef':
            os.mkdir(args.dst_dir+'/'+a+b)

n_out = 0
def one_copy(src_file):#wiki-text/AA/wiki_00
    global n_out

    with open(src_file) as f:
        ln = f.readlines()

    df = None
    for text in ln:#入力ファイルを一行ずつ読み込み
        text = text.strip()
        if not (text.startswith('<doc ') or text.startswith('</doc>')):#wiki-text/AA/wiki_00の中身が<doc,</docで始まらないなら
            if len(text) > 0:
                if df is None:
                    ui = str(uuid.uuid4())
                    dst_file = args.dst_dir + '/' + ui[0] + ui[1] + '/' + ui + '.txt'
                    df = open(dst_file, "w")
                df.write(text+'\n')#保存先に書き込み
                df.flush()
        else:
            if df is not None:
                df.close()
                n_out = n_out + 1
                if args.max_articles > 0 and n_out >= args.max_articles:
                    exit(0)
            df = None
    if df is not None:
        df.close()

for d in os.listdir(args.src_dir):#wiki-text
    for f in os.listdir(args.src_dir+'/'+d):#wiki-text/AA
        one_copy(args.src_dir+'/'+d+'/'+f)#wiki-text/AA/wiki_00

print("end")
