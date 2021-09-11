import pandas as pd
import xlrd
import math
import csv

class global_baseline():
    def gb_calculation(self):
        path = 'D:/Recommendor-system/'
        filename2 = '5000dataset3.xlsx'

        xlsfile = xlrd.open_workbook(path+filename2, on_demand= True)
        xlsfiledata = xlsfile.sheet_by_index(0)

        data=[]
        user_avg = []
        sum1=0
        count1=0
        for i in range(0,100):
            data.append([])
            sum=0
            count=0
            for j in range(0,5000):
                data[i].append(xlsfiledata.cell(i,j).value)
                if(xlsfiledata.cell(i,j).value!=99):
                    #print(xlsfiledata.cell(i,j).value," ")
                    sum=sum+xlsfiledata.cell(i,j).value
                    count=count+1
                    sum1 = sum1 + xlsfiledata.cell(i, j).value
                    count1 = count1 + 1

            user_avg.append((sum/count) if count!=0 else 0)

        overall_avg = sum1/count1;
        #print(overall_avg)

        movie_avg = []
        for i in range(0,5000):
            sum=0
            count=0
            for j in range(0,100):
                if(data[j][i]!=99):
                    #print(data[j][i])
                    sum=sum+data[j][i]
                    count=count+1

            movie_avg.append((sum/count) if count!=0 else 0)

        #print(len(movie_avg))

        global_baseline = []
        for i in range(0,100):
            print(i)
            global_baseline.append([])
            for j in range(0,5000):
                b_x = user_avg[i]-overall_avg
                b_i = movie_avg[j]-overall_avg
                x = overall_avg + b_x + b_i
                global_baseline[i].append(x)

        my_df = pd.DataFrame(global_baseline)
        my_df.to_csv(path+'global_baseline5000.csv',index=False,header=False)

if __name__=='__main__':
    gb= global_baseline()
    gb.gb_calculation()