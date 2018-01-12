import datetime as dt
#str_parse_datetime3
new_year="1/1/2018"
print("checking the type before conversion : ",type(new_year))
new_year_dt = dt.datetime.strptime(new_year,"%m/%d/%Y")
print("String Format : ",new_year_dt)
print("checking the type after conversion : ",type(new_year_dt))
