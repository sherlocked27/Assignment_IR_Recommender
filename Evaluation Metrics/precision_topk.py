import pandas as pd
import xlrd
import math
import csv

class precision_topk():
	def top_50(self):
		path = 'D:/Recommendor-system/'
		filename = 'similarity5000.csv'
		with open(path+filename, 'r') as f:
		  reader = csv.reader(f)
		  your_list = list(reader)

		sim = []
		for i in range(len(your_list)):
		    sim.append([])
		    for j in range(len(your_list[i])):
		        if your_list[i][j]=='':
		            pass
		        else:
		            sim[i].append(float(your_list[i][j]))

		filename3 = '5000dataset3.xlsx'

		xlsfile = xlrd.open_workbook(path+filename3, on_demand= True)
		xlsfiledata = xlsfile.sheet_by_index(0)

		data=[]
		for i in range(0,100):
		    data.append([])
		    for j in range(0,5000):
		        data[i].append(xlsfiledata.cell(i,j).value)

		error1=0
		error2=0
		for i in range(0,100):
			#print(i)
			sorted_row = []
			for j in range(0,5000):
				sorted_row.append([])
				sorted_row[j].append(data[i][j])
				sorted_row[j].append(j)

			sorted_row.sort(key=lambda tup: tup[0])
			#print(sorted_row)
			top_50_index = []
			count=0
			for j in range(0,5000):
				if(sorted_row[5000-j-1][0]!=99):
					top_50_index.append(sorted_row[5000-j-1][1])
					count=count+1
					if count>=50:
						break

			#print(top_10_index)
			for j in range(0,len(top_50_index)):
				sum1=0
				sum2=0
				for k in range(0,100):
					if k==i:
						pass
					else:
						if i<k and sim[i][k-i]>0 and data[k][top_50_index[j]]!=99:
							sum1 = sum1 + (float(data[k][top_50_index[j]])*float(sim[i][k-i]))
							sum2 = sum2 + float(sim[i][k-i])
						elif i>k and sim[i-k][k]>0 and data[k][top_50_index[j]]!=99:
							sum1 = sum1 + (float(data[k][top_50_index[j]])*float(sim[i-k][k]))
							sum2 = sum2 + float(sim[i-k][k])
				value = (sum1/sum2) if sum2!=0 else 0
				error1 = error1 + ((value-data[i][j]) * (value-data[i][j]))
				error2 = error2 + 1

		xx = math.sqrt(error1)
		print("Precision Top 50 (Movie ratings of each user) ",xx/error2)

if __name__=='__main__':
	pt = precision_topk()
	pt.top_50()
"""
Precision Top 10 (Movie ratings of each user)  1.3887055521796996
"""