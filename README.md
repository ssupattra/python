# python

## Installation
1. python
2. install external libraries
- pandas: pip3 install pandas
- mysql: pip3 install mysql-connector-python
- ipython (IPython provides better printing for large text. This ability makes IPython suitable for data analysis because the program prints data in a well-structured format) : pip3 install ipython
- jupyter: pip3 install jupyter
- excel: pip3 install xlrd
- geopy: pip3 install geopy
3. To run jupyter notebook: 'jupyter notebook', it will auto open browser

### Finance-app
#### Instruction
1. pip3 install pandas_datareader (remote data access eg. finance index from nasdaq), see detail in https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
2. pip3 install bokeh
3. jupyter notebook (to create/edit stock_analysis.ipynb that we can use in flask_finance_chart.py)
4. Result is in CS.html

![Result](https://github.com/ssupattra/python/blob/master/finance-app/finance-graph.png)

#### To run web in local machine
1. pip3 install flask
2. create templates, static/css and flask_finance_chart.py (copy code from stock_analysis.ipynb)
3. python3 flask_finance_chart.py
4. open browser - http://localhost:5000/
