import pandas as pd
import eel
import sys

### デスクトップアプリ作成課題
def kimetsu_search(word, file_name):
    print("file_name{}".format(file_name))
    # 検索対象取得
    df=pd.read_csv("./{}".format(file_name))
    source=list(df["name"])

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.view_log_js("『{}』はあります".format(word))
    elif not word:
        print("入力されていません")
        eel.view_log_js("入力されていません")
        sys.exit(0)
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js("『{}』はありません".format(word))
        # 追加
        add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        if add_flg=="1":
            source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./{}".format(file_name),encoding="utf_8-sig")
    print(source)
    eel.view_log_js(source)
