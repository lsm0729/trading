import finterstellar as fs


df = fs.get_price('AAPL',start_date='2020-01-01',end_date='2020-12-31')

# fs.draw_chart(df,right='AAPL')

fs.rsi(df,14)
# fs.draw_chart(df,left='rsi',right='AAPL')

indicata_result=fs.indicator_to_signal(df,factor='rsi',buy=40,sell=60)

# print(indicata_result)

fs.position(df)

# fs.draw_chart(df,left='rsi',right='position_chart')


fs.evaluate(df,cost=0.001)
# fs.draw_chart(df,left='acc_rtn_dp',right='AAPL')

fs.performance(df,rf_rate=0.01)