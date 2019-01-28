import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjname.settings") #pjname請改為你的專案目錄名稱
from django.conf import settings 
django.setup() 
from yourapp.models import hello  #此行為導入 models 中的 hello 資料表
接著 import 完所有需要用到的套件後

後面就可以寫入爬蟲程式

包含會呼叫到的自訂函式與連接資料庫的函式都要一起放進來

最後在文件的末端直接執行爬蟲程式，以下為範例： 

def crawler2():  # 爬蟲程式
    global 變數

    '''爬蟲程式內容'''
    
    sql()  # 將爬出的內容進行與資料庫的連接



def sql():
    global 變數
    '''連接資料庫'''



crawler2()