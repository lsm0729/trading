import finterstellar as fs


df = fs.get_price('AAPL',start_date='2020-01-01',end_date='2020-12-31')

fs.draw_chart(df,right='AAPL')