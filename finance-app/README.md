# Instruction
1. pip3 install pandas_datareader (remote data access eg. finance index from nasdaq), see detail in https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
2. pip3 install bokeh
3. jupyter notebook (to create/edit stock_analysis.ipynb that we can use in flask_finance_chart.py)
4. Result is in CS.html

![Result](https://github.com/ssupattra/python/blob/master/finance-app/finance-graph.png)

## To run web in local machine
1. pip3 install flask
2. create templates, static/css and flask_finance_chart.py (copy code from stock_analysis.ipynb)
3. python3 flask_finance_chart.py
4. open browser - http://localhost:5000/
