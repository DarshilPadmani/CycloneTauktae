import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def Read_csv():
    print("Reading data from CSV file")
    df=pd.read_csv("D:\\Cyclone Tauktae.csv")
    print(df)
def no_index():
    print("Reading data from csv file without index value")
    df=pd.read_csv("D:\\Cyclone Tauktae.csv",index_col=0)
    print(df)
def new_column_name():
    print("Adding new column name to existing data")
    df=pd.read_csv("D://Cyclone Tauktae.csv",index_col=0,skiprows=1,names=['States'\
    ,'Death','WindSpeed(km/h)','Date',\
    'Rainfall(mm)'])
def line_plot():
    df=pd.read_csv("D:\\Cyclone Tauktae.csv")
    st=df['States']
    dth=df['Death']
    wnds=df['WindSpeed(km/h)']
    date=df['Date']
    rnfl=df['Rainfall(mm)']
    plt.xlabel("States")
    plt.xticks(rotation="vertical")
    print("Select specific line chart as given below")
    print("Press 1 to print the data for states Vs Death")
    print("Press 2 to print the data for states Vs WindSpeed(km/h)")
    print("Press 3 to print the data for states Vs Date")
    print("Press 4 to print the data for states Vs Rainfall(mm)")
    print("Press 5 to to merge all the data in one line chart")
    op=int(input("Enter your choice"))
    if op==1:
        plt.ylabel("Death")
        plt.title("States wise Death")
        plt.plot(st,dth)
        plt.show()
    elif op==2:
        plt.ylabel("WindSpeed(km/h)")
        plt.title("States wise WindSpeed(km/h)")
        plt.plot(st,wnds)
        plt.show()
    elif op==3:
        plt.ylabel("Date")
        plt.title("States wise Date")
        plt.plot(st,date)
        plt.show()
    elif op==4:
        plt.ylabel("Rainfall(mm)")
        plt.title("States wise Rainfall(mm)")
        plt.plot(st,rnfl)
        plt.show()
    elif op==5:
        plt.ylabel("Cyclone Anylises")
        plt.plot(st,dth,label="states wise Death")
        plt.plot(st,wnds,label="states wise WindSpeed(km/h)")
        plt.plot(st,date,label="states wise Date")
        plt.plot(st,rnfl,label="states wise Rainfall(mm)")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")                  
def bar_plot():
        df=pd.read_csv("D:\\Cyclone Tauktae.csv")
        st=df['States']
        dth=df['Death']
        wnds=df['WindSpeed(km/h)']
        date=df['Date']
        rnfl=df['Rainfall(mm)']
        plt.xlabel("States")
        plt.xticks(rotation="vertical")
        print("Select specific bar chart as given below")
        print("Press 1 to print the data for states Vs Death")
        print("Press 2 to print the data for states Vs WindSpeed(km/h)")
        print("Press 3 to print the data for states Vs Date")
        print("Press 4 to print the data for states Vs Rainfall(mm)")
        print("Press 5 to to print all the data in the form of stack bar chart")
        print("Press 6 to to print all the data in the form of multiple  bar chart")
        op=int(input("Enter your choice"))
        if op==1:
            plt.ylabel("Death")
            plt.title("States wise Death")
            plt.bar(st,dth)
            plt.show()
        elif op==2:
            plt.ylabel("WindSpeed(km/h)")
            plt.title("States wise WindSpeed(km/h)")
            plt.bar(st,wnds)
            plt.show()
        elif op==3:
            plt.ylabel("Date")
            plt.title("States wise Date")
            plt.bar(st,date)
            plt.show()
        elif op==4:
            plt.ylabel("Rainfall(mm)")
            plt.title("States wise Rainfall(mm)")
            plt.bar(st,rnfl)
            plt.show()
        elif op==5:
            plt.bar(st,dth,width=0.2,label="States wise Death")
            plt.bar(st,wnds,width=0.2,label="States wise WindSpeed(km/h)")
            plt.bar(st,date,width=0.2,label="States wise Date")
            plt.bar(st,rnfl,label="states wise Rainfall(mm)")
            plt.legend()
            plt.show()
        elif op==6:
            ind=np.arange(len(st))
            width=0.25
            plt.bar(ind,dth,width,label="States wise Death")

            plt.bar(ind+0.25,wnds,width,label="States wise WindSpeed(km/h)")
            plt.bar(ind+0.50,date,width,label="States wise Date")
            plt.bar(ind+0.75,rnfl,width,label="states wise Rainfall(mm)")
            plt.legend()
            plt.show()
        else:
            print("Invalid input")

                    




def pie_plot():
        df=pd.read_csv("D:\\Cyclone Tauktae.csv")
        st=df['States']
        dth=df['Death']
        wnds=df['WindSpeed(km/h)']
        date=df['Date']
        rnfl=df['Rainfall(mm)']
        print("Select specific pie chart as given below")
        print("Press 1 to print the data for states Vs Death")
        print("Press 2 to print the data for states Vs WindSpeed(km/h)")
        print("Press 3 to print the data for states Vs Date")
        print("Press 4 to print the data for states Vs Rainfall(mm)")
        op=int(input("Enter your choice"))
        if op==1:
            plt.title("States wise Death")
            plt.pie(dth,labels=st,autopct="%3d%%")
            plt.show()
        elif op==2:
           plt.title("States wise WindSpeed(km/h)")
           plt.pie(wnds,labels=st,autopct="%3d%%")
           plt.show()
            
        elif op==3:
            plt.title("States wise Date")
            plt.pie(date,labels=st,autopct="%3d%%")
            plt.show()
        elif op==4:
            plt.title("States wise Rainfall(mm)")
            plt.pie(rnfl,labels=st,autopct="%3d%%")
            plt.show()



def scatter_chart():
        df=pd.read_csv("D:\\Cyclone Tauktae.csv")
        st=df['States']
        dth=df['Death']
        wnds=df['WindSpeed(km/h)']
        date=df['Date']
        rnfl=df['Active']
        ax=plt.gca()
        ax.scatter(st,dth,color='b',label="States wise Death")
        ax.scatter(st,wnds,color='r',label="States wise WindSpeed(km/h)")
        ax.scatter(st,date,color='g',label="States wise death cases")
        ax.scatter(st,rnfl,color='y',label="States wise Rainfall(mm)")
        plt.xl5abel("States")
        plt.xticks(rotation="vertical")
        plt.title("Complete Scatter Chart")
        plt.legend()
        plt.show()

def data_sorting():
    df=pd.read_csv("D:\\Cyclone Tauktae.csv")
    print("Select specific pie chart as given below")
    print("Press 1 to arrange the record as per the States Name")
    print("Press 2 to arrange the record as per the Death")
    print("Press 3 to arrange the record as per the WindSpeed(km/h)")
    print("Press 4 to arrange the record as per the Date")
    print("Press 5 to arrange the record as per the Rainfall(mm)")
    op=int(input("Enter your choice"))
    if op==1:
        df.sort_values(["States"],inplace=True)
        print(df)
    if op==2:
        df.sort_values(["Death"],inplace=True)
        print(df)
    if op==3:
        df.sort_values(["WindSpeed(km/h)"],inplace=True)
        print(df)
    if op==4:
        df.sort_values(["Date"],inplace=True)
        print(df)
    if op==5:
        df.sort_values(["Rsinfall(mm)"],inplace=True)
        print(df)
    else:
        print("Enter valid input")



def top_bottom_selected_records():
    df=pd.read_csv("D:\\Cyclone Tauktae.csv",index_col=0)
    top=int(input("How many records to display from top"))
    print("First",top,"Records")
    print(df.head(top))
    bottom=int(input("How many records to display from bottom"))
    print("Last",bottom,"Records")
    print(df.tail(bottom))
def duplicate():
    print("Duplicate the file with new file")
    df=pd.read_csv("D:\\Cyclone Tauktae.csv")
    df.to_csv("D:\\Cyclone Tauktae Dublicate.csv")
    print(df)
def specific_col():
    print("Press 1 for states")
    print("Press 2 for Death")
    print("Press 3 for WindSpeed(km/h)")
    print("Press 4 for Date")
    print("Press 5 for Rainfall(mm)")
    op=int(input("Enter your choice"))
    df=pd.read_csv("D:\\Cyclone Tauktae.csv")
    if op==1:
        print(df['States'])
    if op==2:
        print(df['Death'])
    if op==3:
        print(df['WindSpeed(km/h)'])
    if op==4:
        print(df['Data'])
    if op==5:
        print(df['Rainfall(mm)'])
     
    
        
    
    
    
    
    




        

def main_menu():
    print("********************************")
    print("Read data from file in different way")
    print("1. Read Complete CSV file")
    print("2. Reading Complete file without index")
    print("=========================")
    print("Data Visualization")
    print("3. Line Chart")
    print("4. Bar Chart")
    print("5. Pie Chart")
    print("6. Scatter Chart")
    print("=========================")
    print("Apply Data Manipulation in the records of CSV file")
    print("7. Sorting the data as per your choice")
    print("8. Read top and bottom records from file as per requirement")
    print("9. Make the copy of CSV file")
    print("10. Read the specific columns")
    print("******************************")
    opt=int(input("Enter your choice"))
    if opt==1:
        Read_csv()
    elif opt==2:
        no_index()
    elif opt==3:
        line_plot()
    elif opt==4:
        bar_plot()
    elif opt==5:
        pie_plot()
    elif opt==6:
        scatter_chart()
    elif opt==7:
        data_sorting()
    elif opt==8:
        top_bottom_selected_records()
    elif opt==9:
        duplicate()
    elif opt==10:
        specific_col()
    else:
        print("Enter valid input")   
main_menu()
