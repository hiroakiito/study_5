import pandas as pd
import datetime
import eel
import sys

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
        
    def view_item_list(self):
        search_result = False
        for item in self.item_master:
            for order_item in self.item_order_list:
                if int(order_item) == item.item_code:
                    search_result = True
                    print("オーダーは\n商品コード:{}、商品名:{}、価格:{}円ですね。".format(item.item_code, item.item_name, item.price))
                    eel.view_log_js("オーダーは\n商品コード:{}、商品名:{}、価格:{}円ですね。\n購入数量を入力してください".format(item.item_code, item.item_name, item.price))
                    # 画面に商品情報を記載するためのJS側のメソッド呼び出し
                    eel.set_item_js(item.item_name, item.price, search_result)
                    return True
        if search_result:
            return True
        return False

def calc(item_code, price, item_name ,amount):
    if not num_check(amount, "数量"):
        return False
    total_price = int(price) * int(amount)
    eel.set_total_price_js(total_price)   
    print("【注文確認】\n商品コード:{}、商品名:{}、個数{}、合計金額:{}円ですね。".format(item_code, item_name, amount, total_price))
    eel.view_log_js("【注文確認】\n商品コード:{}、商品名:{}、個数{}、合計金額:{}円ですね。\nお支払い金額を入力してください".format(item_code, item_name, amount, total_price))

def make_recept(item_code, price, item_name ,amount, total_price, pay):
    if not pay_check(pay, total_price):
        return False
    change = int(pay) - int(total_price)
    eel.set_change_js(change)
    print("お釣りは{}円です。".format(change))
    eel.view_log_js("お釣りは{}円です。\nありがとうございました。".format(change))
    # レシートファイル出力
    now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    receipt_file_name = "{}.txt".format(now)
    with open(receipt_file_name,'w', encoding='utf_8-sig') as f:
        f.write("商品コード:{}\n商品名:{}\n数量:{}個\n合計金額:{}円\nお支払い金額:{}円\nお釣り:{}円".format(item_code, item_name, amount, total_price, pay, change))

def num_check(num_object, message_item):
    if not num_object or not num_object.isdecimal():
        eel.view_log_js("不正な値です{}は半角数字で入力してください：".format(message_item))
    else:
        return num_object

def pay_check(pay_object, total_price):
    if not num_check(pay_object, "金額"):
        return False
    if (int(pay_object) - int(total_price)) < 0:
        eel.view_log_js("金額が足りません。もう一度入力してください：")
        return False
    return pay_object

### デスクトップアプリ作成課題

def order_input(order_num):
    if not num_check(order_num, "注文番号"):
        return False
    # マスタ登録
    item_master=[]
    source = pd.read_csv("item.csv").values.tolist()
    for row in source:
        item_master.append(Item(row[0], row[1], row[2]))
    # オーダー登録
    order=Order(item_master)

    # オーダー表示
    order_result = False
    order.add_item_order(order_num)
    if order.view_item_list():
        order_result = True
    else:
        print("ご注文の商品はありません。もう一度やり直してください")
        eel.view_log_js("ご注文の商品はありません。もう一度やり直してください")