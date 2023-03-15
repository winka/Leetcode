# 讀檔 4 個月
import pandas as pd
import mpl_finance as mpf
the_df = pd.DataFrame(columns=['年度', '成交股數','成交金額',
                               '開盤價', '最高價','最低價',
                               '收盤價', '漲跌價差','成交筆數'])
# for i in range(1,13):
i = 1
strr = f'C:\\Users\\USER\\Desktop\\winka\\data\\STOCK_DAY_2330_2022{i:02}.csv'
df = pd.read_csv(strr,encoding='big5')
# 重新設置列索引
df = df.reset_index()
# 刪除
df = df[:-6] # 刪除後面6個欄位
print(df)
# 下面這些也可以
# 刪除列 : df = df.drop(df.tail(5).index)
# 刪除行 : df = df.drop(df.columns[-1],axis=1)
# df = df.drop([f'111年{i:02}月 1101 台泥             各日成交資訊'], axis=1)
# 更改欄位名稱
# name_dict = { 'level_0':'年度',
#               'level_1':'成交股數',
#               'level_2':'成交金額',
#               'level_3':'開盤價',
#               'level_4':'最高價',
#               'level_5':'最低價',
#               'level_6':'收盤價',
#               'level_7':'漲跌價差',
#               'level_8':'成交筆數',
#             }
# df = df.rename(columns=name_dict)
# df = df.drop([0])
#
# # 更換資料型別
#
# # drop '，'
# df['成交股數'] = df['成交股數'].str.split(',').str.join('')
# df['成交金額'] = df['成交金額'].str.split(',').str.join('')
# # To float
# df[['最高價','最低價']] = df[['最高價','最低價']].astype(float)
#
# # 深拷貝
# df_copy = df.copy(deep=True)
#
# # 合併 並 重製index(ignore_index)
# the_df = pd.concat([the_df,df_copy], ignore_index=True)

the_df