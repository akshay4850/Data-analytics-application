import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
from tkinter import messagebox
from pandastable import Table


class PenaltyFile:
    # stores the rows of the file and some key information about the set
    def __init__(self, penalty_list):
        self.rows = penalty_list[0]
        self.column_names = penalty_list[1]
        self.earliest_date = ""
        self.last_date = ""
        self.start_and_end_date()

    def start_and_end_date(self):
        # Finds the first and last date for the Penalty file dataset
        start_end_list = [self.rows[0].OFFENCE_MONTH, self.rows[0].OFFENCE_MONTH]
        for x in range(len(self.rows)):
            if self.rows[x].OFFENCE_MONTH < start_end_list[0]:
                start_end_list[0] = self.rows[x].OFFENCE_MONTH
            elif self.rows[x].OFFENCE_MONTH > start_end_list[1]:
                start_end_list[1] = self.rows[x].OFFENCE_MONTH
        self.earliest_date = start_end_list[0]
        self.last_date = start_end_list[1]

    def get_codes(self):
        codes = set()
        for x in range(len(self.rows)):
            codes.add(self.rows[x].OFFENCE_CODE)
            codes.update(self.rows[x].tags)
        return codes

    def retrieve_cases(self, start_date, end_date, tag):
        # retrieves all data matching tag for period
        # returns a pandas dataframe
        # finds all rows in datetime with tag
        # turns those rows into a new dataframe
        # dataframe requires a dictionary with string keys and list values = a lot of lists
        data_rows = []
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        c5 = []
        c6 = []
        c7 = []
        c8 = []
        c9 = []
        c10 = []
        c11 = []
        c12 = []
        c13 = []
        c14 = []
        c15 = []
        c16 = []
        c17 = []
        c18 = []
        c19 = []
        c20 = []
        c21 = []
        c22 = []
        c23 = []
        c24 = []
        c24 = []
        c25 = []
        data_dict = {}
        for y in range(len(self.rows)):
            if tag in self.rows[y].tags and end_date >= self.rows[y].OFFENCE_MONTH >= start_date:
                data_rows.append(self.rows[y].row_number)
        for x in range(len(data_rows)):
            c1.append(self.rows[data_rows[x] - 1].OFFENCE_FINYEAR)
            c2.append(self.rows[data_rows[x] - 1].OFFENCE_MONTH)
            c3.append(self.rows[data_rows[x] - 1].OFFENCE_CODE)
            c4.append(self.rows[data_rows[x] - 1].OFFENCE_DESC)
            c5.append(self.rows[data_rows[x] - 1].LEGISLATION)
            c6.append(self.rows[data_rows[x] - 1].SECTION_CLAUSE)
            c7.append(self.rows[data_rows[x] - 1].FACE_VALUE)
            c8.append(self.rows[data_rows[x] - 1].CAMERA_IND)
            c9.append(self.rows[data_rows[x] - 1].CAMERA_TYPE)
            c10.append(self.rows[data_rows[x] - 1].LOCATION_CODE)
            c11.append(self.rows[data_rows[x] - 1].LOCATION_DETAILS)
            c12.append(self.rows[data_rows[x] - 1].SCHOOL_ZONE_IND)
            c13.append(self.rows[data_rows[x] - 1].SPEED_BAND)
            c14.append(self.rows[data_rows[x] - 1].SPEED_IND)
            c15.append(self.rows[data_rows[x] - 1].POINT_TO_POINT_IND)
            c16.append(self.rows[data_rows[x] - 1].RED_LIGHT_CAMERA_IND)
            c17.append(self.rows[data_rows[x] - 1].SPEED_CAMERA_IND)
            c18.append(self.rows[data_rows[x] - 1].SEATBELT_IND)
            c19.append(self.rows[data_rows[x] - 1].MOBILE_PHONE_IND)
            c20.append(self.rows[data_rows[x] - 1].PARKING_IND)
            c21.append(self.rows[data_rows[x] - 1].CINS_IND)
            c22.append(self.rows[data_rows[x] - 1].FOOD_IND)
            c23.append(self.rows[data_rows[x] - 1].BICYCLE_TOY_ETC_IND)
            c24.append(self.rows[data_rows[x] - 1].TOTAL_NUMBER)
            c25.append(self.rows[data_rows[x] - 1].TOTAL_VALUE)
        dict_rows = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18,
                     c19, c20, c21, c22, c23, c24, c24, c25]
        for i in range(25):
            data_dict.update({self.column_names[i]: dict_rows[i]})
        new_dataframe = pd.DataFrame(data_dict)
        return dict_rows


class PenaltyFileRow:
    # stores the data for one row of the penalty dataset
    def __init__(self, init_list):
        self.OFFENCE_FINYEAR = init_list[0]
        the_date = init_list[1].split("/")
        self.OFFENCE_MONTH = datetime.datetime(int(the_date[2]), int(the_date[1]), int(the_date[0]))
        self.OFFENCE_CODE = init_list[2]
        self.OFFENCE_DESC = init_list[3]
        self.LEGISLATION = init_list[4]
        self.SECTION_CLAUSE = init_list[5]
        self.FACE_VALUE = init_list[6]
        self.CAMERA_IND = init_list[7]
        self.CAMERA_TYPE = init_list[8]
        self.LOCATION_CODE = init_list[9]
        self.LOCATION_DETAILS = init_list[10]
        self.SCHOOL_ZONE_IND = init_list[11]
        self.SPEED_BAND = init_list[12]
        self.SPEED_IND = init_list[13]
        self.POINT_TO_POINT_IND = init_list[14]
        self.RED_LIGHT_CAMERA_IND = init_list[15]
        self.SPEED_CAMERA_IND = init_list[16]
        self.SEATBELT_IND = init_list[17]
        self.MOBILE_PHONE_IND = init_list[18]
        self.PARKING_IND = init_list[19]
        self.CINS_IND = init_list[20]
        self.FOOD_IND = init_list[21]
        self.BICYCLE_TOY_ETC_IND = init_list[22]
        self.TOTAL_NUMBER = init_list[23]
        self.TOTAL_VALUE = init_list[24]
        self.row_number = init_list[25]
        self.tags = {"All"}
        self.get_tags()

    # function to get the tags from the excel file and add them to the dataframe.
    def get_tags(self):
        if self.OFFENCE_DESC.find("Camera") != -1:
            self.tags.add("Camera")
            self.tags.add("Radar or Camera")
            self.tags.add("Camera or Radar")
        if self.OFFENCE_DESC.find("Lidar") != -1:
            self.tags.add("Lidar")
        if self.OFFENCE_DESC.find("Radar") != -1:
            self.tags.add("Radar")
            self.tags.add("Radar or Camera")
            self.tags.add("Camera or Radar")
        self.tags.add(self.OFFENCE_CODE)
        if self.MOBILE_PHONE_IND == "Y":
            self.tags.add("Mobile")
        if self.CAMERA_IND == "Y":
            self.tags.add("Camera")
        if self.SCHOOL_ZONE_IND == "Y":
            self.tags.add("School Zone")
        if self.SPEED_IND == "Y":
            self.tags.add("Speeding")
        if self.POINT_TO_POINT_IND == "Y":
            self.tags.add("Point to Point")
        if self.RED_LIGHT_CAMERA_IND == "Y":
            self.tags.add("Red Light")
        if self.SPEED_CAMERA_IND == "Y":
            self.tags.add("Speed Camera")
        if self.SEATBELT_IND == "Y":
            self.tags.add("Seatbelt")
        if self.MOBILE_PHONE_IND == "Y":
            self.tags.add("Mobile Phone Usage")
        if self.PARKING_IND == "Y":
            self.tags.add("Parking")
        if self.CINS_IND == "Y":
            self.tags.add("CINS")
        if self.FOOD_IND == "Y":
            self.tags.add("Food")
        if self.BICYCLE_TOY_ETC_IND == "Y":
            self.tags.add("Bicycle/Toys")


def open_csv_to_list(file_location):
    # returns the file in list format
    row_list = []
    column_list = []
    with open(file_location, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row = 0
        for line in csv_reader:
            if row == 0:
                for y in line:
                    column_list.append(y)
            else:
                class_data_init_list = []
                for x in line:
                    class_data_init_list.append(x)
                class_data_init_list.append(row)
                row_list.append(PenaltyFileRow(class_data_init_list))
            row += 1
    return_list = [row_list, column_list]
    return return_list


def get_tag_fines_by_month(start_date, end_date, row_list, tag):
    # function takes start end date returns a list of tuples
    fine_date_dict = {}
    for y in range(len(row_list)):
        if tag in row_list[y].tags and end_date >= row_list[y].OFFENCE_MONTH >= start_date:
            fine_date_dict.update({row_list[y].OFFENCE_MONTH.strftime("%m/%y"):
                                       fine_date_dict.get(row_list[y].OFFENCE_MONTH.strftime("%m/%y"), 0) + 1})
            # dictionary, key is date, value is number of fines
    tuple_list = []
    x_plot = []
    y_plot = []
    # Uses tuples to sort the list, then returns [[x],[y]] for easy plotting
    for item in fine_date_dict.keys():
        tuple_list.append((item, int(fine_date_dict.get(item))))
        tuple_list.sort()
    for a in range(len(tuple_list)):
        x_plot.append(tuple_list[a][0])
        y_plot.append(tuple_list[a][1])
    return_list = [x_plot, y_plot]
    return return_list


def offence_trends(file):
    # plots 4 graphs
    # % of total offences by month
    # % increase month to month
    # % while also speeding
    # tag total by month
    # graph1
    code = str(offence_code_box.get())
    if code == "":
        code = str(Offences.get(Offences.curselection()))
    offense_codes = file.get_codes()
    if code not in offense_codes:
        messagebox.showinfo("Error", "Code not found in file")
        return
    else:
        start_date = datetime.datetime(int(getSelectedSpinBoxValue1()), int(getSelectedSpinBoxValue2()), 1)
        end_date = datetime.datetime(int(getSelectedSpinBoxValue3()), int(getSelectedSpinBoxValue4()), 1)
        x_y_to_plot = get_tag_fines_by_month(start_date, end_date, file.rows, code)
        if not x_y_to_plot:
            messagebox.showinfo("Error", "Code not found in date range")
            return
        else:
            # % increase month to month
            percent_change_y = [0 for _ in range(len(x_y_to_plot[1]))]
            percent_change_y[0] = 0
            for i in range(1, len(x_y_to_plot[1])):
                percent_change_y[i] = ((x_y_to_plot[1][i] - x_y_to_plot[1][i - 1]) / x_y_to_plot[1][i - 1]) * 100
            # % of total offences by month
            all_codes = get_tag_fines_by_month(start_date, end_date, file.rows, "All")
            percent_of_codes_y = [0 for _ in range(len(all_codes[1]))]
            for n in range(len(percent_of_codes_y)):
                percent_of_codes_y[n] = (x_y_to_plot[1][n] / all_codes[1][n]) * 100
            # % while also speeding
            speeding_xy = get_tag_fines_by_month(start_date, end_date, file.rows, "Speeding")
            percent_speeding = [0 for _ in range(len(speeding_xy[1]))]
            for n in range(len(percent_speeding)):
                percent_speeding[n] = (x_y_to_plot[1][n] / speeding_xy[1][n]) * 100

        fig, axis = plt.subplots(2, 2)
        axis[0, 0].bar(x_y_to_plot[0], percent_of_codes_y)
        axis[0, 0].set_title(code + " % of Total Offences")
        axis[0, 0].set(xlabel="Month/Year", ylabel="Percent %")
        axis[0, 1].stem(x_y_to_plot[0], percent_change_y)
        axis[0, 1].set_title("% Increase of " + code + "Offences from previous month")
        axis[0, 1].set(xlabel="Month/Year", ylabel="Percent %")
        axis[1, 0].plot(x_y_to_plot[0], percent_speeding, 'tab:blue')
        axis[1, 0].set_title("% of " + code + " while Speeding")
        axis[1, 0].set(xlabel="Month/Year", ylabel=("Percent of total " + code + " Offences"))
        axis[1, 1].plot(x_y_to_plot[0], x_y_to_plot[1], 'tab:red')
        axis[1, 1].set_title(code + " Total Offences")
        axis[1, 1].set(xlabel="Month", ylabel="Number of Offences")
        fig.show()


# exports data as a csv file
def export_data_as_csv(data_to_export, file_path):
    data_to_export.to_csv(file_path)
    return


# used to display a seperate browse window for the user to select the csv file.
def Filename():
    global dataset
    file = filedialog.askopenfilename(initialdir="C:\\", title="Select the dataset")
    dataset = pd.read_csv(file)
    return file


# displays the number of rows and columns from the dataset in a messagebox.
def Shape():
    messagebox.showinfo("Dataset Shape", dataset.shape)


def getListboxValue():
    itemSelected = list(Offences.curselection())
    return itemSelected


# function used to remove all nan or null values from the excel sheet.
def datawrangling():
    global offenses
    global sum_freq
    dataset.fillna(value="N", inplace=True)
    dataset[offences] = dataset[offences].astype('category')
    dataset['OFFENCE_MONTH'] = dataset['OFFENCE_MONTH'].apply(lambda x: pd.datetime.strptime(x, '%d/%m/%Y'))
    messagebox.showinfo("Data Wrangling", "File Ready!")
    offenses = {}
    for i, field in enumerate(offences):
        offenses[field] = dataset[dataset[field] == 'Y'].groupby('OFFENCE_MONTH').agg(
            {'FACE_VALUE': 'count'}).reset_index().sort_values('OFFENCE_MONTH').iloc[:, -1].tolist()
    offenses = pd.DataFrame(offenses)
    sum_freq = dataset[offences].sum(axis=0)
    offenses['months'] = dataset['OFFENCE_MONTH'].map(lambda x: x.strftime("%b '%y")).unique()


#
def offencecount():
    global number
    global typeo
    code = getListboxValue()
    typeo = offences[int(code[0])]
    start_year = str(getSelectedSpinBoxValue1())
    start_month = str(getSelectedSpinBoxValue2())
    end_year = str(getSelectedSpinBoxValue3())
    end_month = str(getSelectedSpinBoxValue4())
    if start_year > end_year:
        messagebox.showwarning("Retry", "Selected timeline doesnt exist!")
    elif start_year == end_year:
        if start_month > end_month:
            messagebox.showwarning("Retry", "Selected timeline doesnt exist!")
        else:
            if int(start_month) < 10:
                startdate = (start_year + "-" + "0" + start_month + "-" + "01")
            if int(start_month) >= 10:
                startdate = (start_year + "-" + start_month + "-" + "01")
            if int(end_month) < 10:
                enddate = (end_year + "-" + "0" + end_month + "-" + "01")
            if int(end_month) >= 10:
                enddate = (end_year + "-" + end_month + "-" + "01")

    else:
        if int(start_month) < 10:
            startdate = (start_year + "-" + "0" + start_month + "-" + "01")
        if int(start_month) >= 10:
            startdate = (start_year + "-" + start_month + "-" + "01")
        if int(end_month) < 10:
            enddate = (end_year + "-" + "0" + end_month + "-" + "01")
        if int(end_month) >= 10:
            enddate = (end_year + "-" + end_month + "-" + "01")
    tempset = dataset
    tempset = tempset.set_index('OFFENCE_MONTH')
    tempset = tempset.sort_index()
    tempset = tempset[startdate:enddate]
    number = tempset.loc[tempset[typeo] == "Y"]
    print(number)
    messagebox.showinfo("Offence Details", "Number of reportings found are " + str(number.shape[0]))


# Function to display a graph from the offence count function.
def graphoffence():
    number2 = number.reset_index()
    number2["OFFENCE_MONTH"] = number.index
    print(number2.head())
    tempo = {}
    tempo[typeo] = number2[number2[typeo] == 'Y'].groupby('OFFENCE_MONTH').agg(
        {'FACE_VALUE': 'count'}).reset_index().sort_values('OFFENCE_MONTH').iloc[:, -1].tolist()
    tempo = pd.DataFrame(tempo)
    tempo['months'] = number2['OFFENCE_MONTH'].map(lambda x: x.strftime("%b '%y")).unique()
    plt.plot(tempo[typeo], label=typeo)
    plt.title("Number of offences for each category", fontsize=18, fontweight='bold')
    plt.xlabel("Months", size=14)
    plt.ylabel("Number of fines", size=14)
    plt.show()


# Visualising the graph for analysing variance in growth rate
def freqVariance():
    rollingav = dataset.OFFENCE_MONTH.dt.to_period('M').sort_index().value_counts()
    rollingav.index = rollingav.index.to_timestamp()
    rollingav = rollingav.sort_index()
    rollingav = rollingav.rolling(12, axis=0).sum().pct_change(axis=0)
    x = rollingav.index
    y = rollingav.values
    plt.fill_between(x, y, label="Variance in growth", color="Turquoise")
    plt.xlabel("Years")
    plt.ylabel("Variance in growth rate")
    plt.title("Variance graph ")
    plt.show()


def btnClickFunction():
    fig, a = plt.subplots(1, figsize=(20, 12))
    for column in offenses.drop('months', axis=1):
        plt.plot(offenses[column], label=column)
    plt.legend(loc=1, ncol=1)
    plt.title("Distributions for various types of offence indicators")
    plt.xlabel("Months")
    plt.ylabel("Frequency of indicator during offence")
    fig.show()


def getSelectedSpinBoxValue1():
    return YearStart.get()


def getSelectedSpinBoxValue2():
    return MonthStart.get()


def getSelectedSpinBoxValue3():
    return EndYear.get()


def getSelectedSpinBoxValue4():
    return EndMonth.get()


def process_data():
    global pen_file
    pen_file = PenaltyFile(open_csv_to_list(Filename()))
    datawrangling()


def enter_offense(file):
    #   takes the penaltyfile class as input, output is a graph on screen
    code = str(offence_code_box.get())
    if code == "":
        code = str(Offences.get(Offences.curselection()))
        print(code)
    offense_codes = file.get_codes()
    if code in offense_codes:
        start_date = datetime.datetime(int(getSelectedSpinBoxValue1()), int(getSelectedSpinBoxValue2()), 1)
        end_date = datetime.datetime(int(getSelectedSpinBoxValue3()), int(getSelectedSpinBoxValue4()), 1)
        if start_date > end_date:
            messagebox.showinfo("Error", "Start date must be before end date")
            return
        x_y = get_tag_fines_by_month(start_date, end_date, file.rows, code)
        if not x_y[1]:
            messagebox.showinfo("Error", "Code not found in range")
        else:
            plt.bar(x_y[0], x_y[1])
            plt.xlabel("Month")
            plt.ylabel("Number of offences")
            plt.suptitle(str(code))
            plt.show()
    else:
        messagebox.showinfo("Error", "Code not found in file")


def view_offence_dataframe(file):
    # takes penaltyfile class as input, output it table data in the scroll window
    code = str(offence_code_box.get())
    if code == "":
        code = str(Offences.get(Offences.curselection()))
    offense_codes = file.get_codes()
    if code in offense_codes:
        start_date = datetime.datetime(int(getSelectedSpinBoxValue1()), int(getSelectedSpinBoxValue2()), 1)
        end_date = datetime.datetime(int(getSelectedSpinBoxValue3()), int(getSelectedSpinBoxValue4()), 1)
        if start_date > end_date:
            messagebox.showinfo("Error", "Start date must be before end date")
            return
        rv = file.retrieve_cases(start_date, end_date, code)
        if not rv:
            messagebox.showinfo("Error", "Code not found in range")
            return
        columns = file.column_names
        tree = ttk.Treeview(tableFrame, columns=columns, show='headings')
        for name in columns:
            tree.heading(name, text=name)
        rows = []
        for x in range(len(rv[1])):
            rows.append((rv[0][x], rv[1][x], rv[2][x], rv[3][x], rv[4][x], rv[5][x], rv[6][x], rv[7][x],
                         rv[8][x], rv[9][x], rv[10][x], rv[11][x], rv[12][x], rv[13][x], rv[14][x],
                         rv[15][x], rv[16][x], rv[17][x], rv[18][x], rv[19][x], rv[20][x], rv[21][x],
                         rv[22][x], rv[23][x], rv[24][x], rv[25][x]))
        for row in rows:
            tree.insert('', tk.END, values=row)
        tree.grid(row=0, column=0)
        treescrolly = tk.Scrollbar(tableFrame, orient="vertical", command=tree.yview)
        treescrollx = tk.Scrollbar(tree, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        tree.pack(fill="both", expand=True)
        # treescrollx.place(x=720, y=920, height=2, width=100)


init_blank = [PenaltyFileRow(["1/1/1" for x in range(26)])]

global pen_file

global offences
offences = ['CAMERA_IND', 'SCHOOL_ZONE_IND', 'SPEED_IND', 'POINT_TO_POINT_IND',
            'RED_LIGHT_CAMERA_IND', 'SPEED_CAMERA_IND', 'SEATBELT_IND', 'MOBILE_PHONE_IND',
            'PARKING_IND', 'CINS_IND', 'FOOD_IND', 'BICYCLE_TOY_ETC_IND']
root = Tk()

root.geometry('1980x1080')
root.configure(background='#F0F8FF')
root.title('Traffic analytics Tool')

tableFrame = tk.LabelFrame(root, text="Excel data")
tableFrame.place(x=720, y=3, height=900, width=750)

offence_code_box = Entry(root, bg='#66CDAA', width=25)
offence_code_box.place(x=25, y=338)
Button(root, text='Browse', bg='#66CDAA', font=('arial', 12, 'normal'), command=process_data).place(x=25, y=15)

Button(root, text='File data', bg='#66CDAA', font=('arial', 12, 'normal'), command=Shape).place(x=25, y=45)

Label(root, text='Browse the address for the DataSet', bg='#F0F8FF', font=('arial', 8, 'normal')).place(x=25, y=-4)

Offences = Listbox(root, bg='#66CDAA', font=('arial', 12, 'normal'), width=0, height=0)
Offences.insert(0, 'Camera')
Offences.insert(1, 'School Zone')
Offences.insert(2, 'Speeding')
Offences.insert(3, 'Point to Point')
Offences.insert(4, 'Red Light')
Offences.insert(5, 'Speed Camera')
Offences.insert(6, 'Seatbelt')
Offences.insert(7, 'Mobile Phone Usage')
Offences.insert(8, 'Parking')
Offences.insert(9, 'CINS')
Offences.insert(10, 'Food')
Offences.insert(11, 'Bicycle/Toys')
Offences.place(x=25, y=105)

Button(root, text='View Data for offence', bg='#66CDAA', font=('arial', 12, 'normal'),
       command=lambda: view_offence_dataframe(pen_file)).place(x=25, y=380)

Button(root, text='Visualize', bg='#66CDAA', font=('arial', 12, 'normal'),
       command=lambda: enter_offense(pen_file)).place(x=215, y=380)

Button(root, text='View Trends for Offence', bg='#66CDAA', font=('arial', 12, 'normal'),
       command=lambda: offence_trends(pen_file)).place(x=25, y=435)

Button(root, text='Frequency variance of Offences', bg='#66CDAA', font=('arial', 12, 'normal'),
       command=freqVariance).place(x=280, y=45)

Button(root, text='Visualize offence summary', bg='#66CDAA', font=('arial', 12, 'normal'),
       command=btnClickFunction).place(x=520, y=45)

YearStart = Spinbox(root, from_=2012, to=2017, font=('arial', 12, 'normal'), bg='#66CDAA', width=10)
YearStart.place(x=285, y=135)

MonthStart = Spinbox(root, from_=1, to=12, font=('arial', 12, 'normal'), bg='#66CDAA', width=10)
MonthStart.place(x=285, y=195)

Label(root, text='Choose Start Year', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=285, y=115)

Label(root, text='Choose Start Month', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=285, y=175)

EndYear = Spinbox(root, from_=2012, to=2017, font=('arial', 12, 'normal'), bg='#66CDAA', width=10)
EndYear.place(x=465, y=135)

EndMonth = Spinbox(root, from_=1, to=12, font=('arial', 12, 'normal'), bg='#66CDAA', width=10)
EndMonth.place(x=465, y=195)

Label(root, text='Choose End Year', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=465, y=115)

Label(root, text='Choose End Month', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=465, y=175)

Label(root, text='Select the type of offence or enter into the box', bg='#F0F8FF', font=('arial', 12, 'normal')).place(
    x=25, y=85)

root.mainloop()
