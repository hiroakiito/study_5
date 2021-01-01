import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def order_input(order_num):
    search.order_input(order_num)

@ eel.expose
def calc(item_code, price, item_name ,amount):
    search.calc(item_code, price, item_name ,amount)

@ eel.expose
def make_recept(item_code, price, item_name ,amount, total_price, pay):
    search.make_recept(item_code, price, item_name ,amount, total_price, pay)
 
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)