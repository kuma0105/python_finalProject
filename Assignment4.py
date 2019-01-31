from tkinter import *
import csv
import operator
import sqlite3


def gui():
    """Starting point when module is the main routine."""
    global root
    root = Tk()  # making a gui object using tkinter API
    top = Assignment4(root)  # Creating an instance of Create_GUI class
    root.mainloop()  # Keep the window running


class Assignment4:
    """
    Class declaration designed for making graphical user interface showing data from csv file
    Attributes:
        count       variable to keep record of the number of rows in the csv file
        i           the column on based of which the list should be sorted default is 1st column
    """

    __author__ = "Rajat Kumar"
    count = 0
    i = 0

    # connecting to the database named Info.db - if it does not exists then it creates one for us
    with sqlite3.connect("Info.db") as db:
        cursor = db.cursor()

    def __init__(self, root=None):
        """init method to initialize the class"""
        root.geometry("999x586+145+7")
        root.title("Rajat Kumar Final project")
        root.configure(background="#82b5d8")

        # scroll bar for the listbox
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # creating a listbox to hold the data
        self.listbox = Listbox(root, font=('monospace', 10),  yscrollcommand=self.scrollbar.set)
        self.listbox.place(relx=0.0, rely=0.495, relheight=0.5, relwidth=1.0)
        self.listbox.bind('<<ListboxSelect>>', self.select_list)

        self.scrollbar.config(command=self.listbox.yview)

        # Populating the GUI with Labels and entry widgets
        self.lblDate = Label(root)
        self.lblDate.place(relx=0.03, rely=0.034, height=21, width=48)
        self.lblDate.configure(background="#d9d9d9")
        self.lblDate.configure(text='''ref_date''')

        self.lblGeo = Label(root)
        self.lblGeo.place(relx=0.03, rely=0.085, height=21, width=26)
        self.lblGeo.configure(background="#d9d9d9")
        self.lblGeo.configure(text='''geo''')

        self.lblDguid = Label(root)
        self.lblDguid.place(relx=0.03, rely=0.137, height=21, width=37)
        self.lblDguid.configure(background="#d9d9d9")
        self.lblDguid.configure(text='''dguid''')

        self.lblCategory = Label(root)
        self.lblCategory.place(relx=0.03, rely=0.188, height=21, width=84)
        self.lblCategory.configure(background="#d9d9d9")
        self.lblCategory.configure(disabledforeground="#a3a3a3")
        self.lblCategory.configure(foreground="#000000")
        self.lblCategory.configure(text='''Food Category''')

        self.lblCommodity = Label(root)
        self.lblCommodity.place(relx=0.03, rely=0.239, height=21, width=68)
        self.lblCommodity.configure(background="#d9d9d9")
        self.lblCommodity.configure(text='''commodity''')

        self.lblUom = Label(root)
        self.lblUom.place(relx=0.03, rely=0.29, height=21, width=31)
        self.lblUom.configure(background="#d9d9d9")
        self.lblUom.configure(text='''uom''')

        self.lblUom_id = Label(root)
        self.lblUom_id.place(relx=0.03, rely=0.341, height=21, width=46)
        self.lblUom_id.configure(background="#d9d9d9")
        self.lblUom_id.configure(text='''uom_id''')

        self.lblScalar = Label(root)
        self.lblScalar.place(relx=0.03, rely=0.392, height=21, width=36)
        self.lblScalar.configure(background="#d9d9d9")
        self.lblScalar.configure(text='''scalar''')

        self.entryRef_date = Entry(root)
        self.entryRef_date.place(relx=0.12, rely=0.034, height=20
                                 , relwidth=0.164)

        self.entryGeo = Entry(root)
        self.entryGeo.place(relx=0.12, rely=0.085, height=20, relwidth=0.164)

        self.entryDguid = Entry(root)
        self.entryDguid.place(relx=0.12, rely=0.137, height=20, relwidth=0.164)

        self.entryCategory = Entry(root)
        self.entryCategory.place(relx=0.12, rely=0.188, height=20
                                 , relwidth=0.164)

        self.entryCommodity = Entry(root)
        self.entryCommodity.place(relx=0.12, rely=0.239, height=20
                                  , relwidth=0.164)

        self.entryUom = Entry(root)
        self.entryUom.place(relx=0.12, rely=0.29, height=20, relwidth=0.164)

        self.entryUom_id = Entry(root)
        self.entryUom_id.place(relx=0.12, rely=0.341, height=20, relwidth=0.164)

        self.entryScalar = Entry(root)
        self.entryScalar.place(relx=0.12, rely=0.392, height=20, relwidth=0.164)

        self.lblScalar_id = Label(root)
        self.lblScalar_id.place(relx=0.581, rely=0.034, height=21, width=51)
        self.lblScalar_id.configure(background="#d9d9d9")
        self.lblScalar_id.configure(text='''scalar_id''')

        self.lblVector = Label(root)
        self.lblVector.place(relx=0.581, rely=0.085, height=21, width=39)
        self.lblVector.configure(background="#d9d9d9")
        self.lblVector.configure(text='''vector''')

        self.lblCoordinate = Label(root)
        self.lblCoordinate.place(relx=0.581, rely=0.137, height=21, width=63)
        self.lblCoordinate.configure(background="#d9d9d9")
        self.lblCoordinate.configure(text='''coordinate''')

        self.lblValue = Label(root)
        self.lblValue.place(relx=0.581, rely=0.188, height=21, width=34)
        self.lblValue.configure(background="#d9d9d9")
        self.lblValue.configure(text='''value''')

        self.lblStatus = Label(root)
        self.lblStatus.place(relx=0.581, rely=0.239, height=21, width=37)
        self.lblStatus.configure(background="#d9d9d9")
        self.lblStatus.configure(text='''status''')

        self.lblSymbol = Label(root)
        self.lblSymbol.place(relx=0.581, rely=0.29, height=21, width=45)
        self.lblSymbol.configure(background="#d9d9d9")
        self.lblSymbol.configure(text='''symbol''')

        self.lblTerminated = Label(root)
        self.lblTerminated.place(relx=0.581, rely=0.341, height=21, width=64)
        self.lblTerminated.configure(background="#d9d9d9")
        self.lblTerminated.configure(text='''terminated''')

        self.lblDecimal = Label(root)
        self.lblDecimal.place(relx=0.581, rely=0.392, height=21, width=48)
        self.lblDecimal.configure(background="#d9d9d9")
        self.lblDecimal.configure(text='''decimal''')

        self.entryScalar_id = Entry(root)
        self.entryScalar_id.place(relx=0.651, rely=0.034, height=20
                                  , relwidth=0.164)

        self.entryVector = Entry(root)
        self.entryVector.place(relx=0.651, rely=0.085, height=20, relwidth=0.164)


        self.entryValue = Entry(root)
        self.entryValue.place(relx=0.651, rely=0.188, height=20, relwidth=0.164)

        self.entryCoordinate = Entry(root)
        self.entryCoordinate.place(relx=0.651, rely=0.137, height=20
                                   , relwidth=0.164)

        self.entryStatus = Entry(root)
        self.entryStatus.place(relx=0.651, rely=0.239, height=20, relwidth=0.164)


        self.entrySymbol = Entry(root)
        self.entrySymbol.place(relx=0.651, rely=0.29, height=20, relwidth=0.164)

        self.entryTerminated = Entry(root)
        self.entryTerminated.place(relx=0.651, rely=0.341, height=20
                                   , relwidth=0.164)

        self.entryDecimal = Entry(root)
        self.entryDecimal.place(relx=0.651, rely=0.392, height=20
                                , relwidth=0.164)

        self.entrySearch = Entry(root)
        self.entrySearch.place(relx=0.33, rely=0.430, height=20, relwidth=0.164)

        self.buttonInsert = Button(root)
        self.buttonInsert.place(relx=0.39, rely=0.048, height=24, width=40)
        self.buttonInsert.configure(background="#d9d9d9")
        self.buttonInsert.configure(text='''Insert''', command= lambda: Assignment4.insert_data(self))

        self.buttonUpdate = Button(root)
        self.buttonUpdate.place(relx=0.39, rely=0.120, height=24, width=47)
        self.buttonUpdate.configure(background="#d9d9d9")
        self.buttonUpdate.configure(text='''Update''',command=lambda: Assignment4.update_data(self, self.entrySearch.get()))

        self.buttonDelete = Button(root)
        self.buttonDelete.place(relx=0.39, rely=0.190, height=24, width=47)
        self.buttonDelete.configure(background="#d9d9d9")
        self.buttonDelete.configure(text='''Delete''',command=lambda: Assignment4.delete_data(self, self.entrySearch.get()))

        self.buttonClear = Button(root)
        self.buttonClear.place(relx=0.39, rely=0.260, height=24, width=69)
        self.buttonClear.configure(background="#d9d9d9")
        self.buttonClear.configure(text='''Clear fields''')
        self.buttonClear.configure(command=lambda: Assignment4.clear_fields(self))

        self.buttonLoad = Button(root)
        self.buttonLoad.place(relx=0.39, rely=0.330, height=24, width=70)
        self.buttonLoad.configure(background="#d9d9d9")
        self.buttonLoad.configure(text='''Load CSV''', command=lambda: Assignment4.read_csv(self, 0))

        self.buttonSearch = Button(root)
        self.buttonSearch.place(relx=0.50, rely=0.430, height=24, width=47)
        self.buttonSearch.configure(background="#d9d9d9")
        self.buttonSearch.configure(text='''Search''',  command=lambda: Assignment4.search_data(self, self.entrySearch.get()))



        self.connect_table()
        self.read_database()



    def connect_table(self):
        """
        function to create a table having id which increments on itself and 16 other columns from the csv file
        """
        # executing a query of creating a table named food

        Assignment4.cursor.execute("""
            CREATE TABLE IF NOT EXISTS food(
            id INTEGER PRIMARY KEY,
            ref_date INTEGER NOT NULL,    
            geo VARCHAR(24) NOT NULL,        
            dgu_id VARCHAR(24) NOT NULL,       
            food_categories VARCHAR(24) NOT NULL,        
            commodity VARCHAR(24) NOT NULL,        
            uom INTEGER NOT NULL,        
            uom_id INTEGER NOT NULL,        
            scalar_factor VARCHAR(24) NOT NULL,        
            scalar_id INTEGER NOT NULL,        
            vector VARCHAR(24) NOT NULL,        
            coordinate VARCHAR(24) NOT NULL,        
            value INTEGER NOT NULL,        
            status VARCHAR(24) NOT NULL,        
            symbol VARCHAR(24) NOT NULL,        
            terminated VARCHAR(24) NOT NULL,        
            decimals VARCHAR(24) NOT NULL        
            )
            """)
        return "Connected"

    #opening a csv file and reading the data
    def read_csv(self, j):
        """Return the total number of rows in the csv file
            This function is used to read the csv file named data.csv when user presses the load Data button and
            insert tbe data into the database
            :return: Assignment4.count

        """
        with open('data.csv') as csv_file:
            try:
                Assignment4.count = 0

                reader = csv.reader(csv_file, delimiter=',')


                # sorting based on a particular column from the csv reader
                sort = sorted(reader, key=operator.itemgetter(j))
                Assignment4.cursor.execute("delete from food")
                # inserting the data into the table named food in the database
                for eachline in sort:
                    Assignment4.count += 1
                    Assignment4.cursor.execute("INSERT INTO food (ref_date, geo, dgu_id, food_categories, commodity,uom, uom_id,scalar_factor,scalar_id,vector,coordinate,value,status,symbol,terminated, decimals) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                               (eachline[0],eachline[1],eachline[2],eachline[3],eachline[4],eachline[5],eachline[6],eachline[7],eachline[8],eachline[9],eachline[10],eachline[11],eachline[12],eachline[13],eachline[14],eachline[15]))
                    print("Data inserted")
                Assignment4.db.commit()
                Assignment4.read_database(self)
            except: print("There was an error opening the csv file")
        return Assignment4.count


    def read_database(self):
        """
            Creates listbox and vertical scrollbar for that listbox
            Listbox is populated from database
        """
        try:
            self.listbox.delete( 0 , END)
            Assignment4.cursor.execute("""select * from food""")
            print("Reading Database completed!")
            rows = Assignment4.cursor.fetchall()
            print("Please wait while populating list.....")
            # looping through every row in the table to populate the listbox
            for row in rows:
                self.listbox.insert(END, str(row[0])+'|' +str(row[1])+'|' +str(row[2])+'|' +str(row[3])+'|' +str(row[4])+'|' +str(row[5])+'|' +str(row[6])+'|' +str(row[7])+'|' +str(row[8])+'|' +str(row[9])+'|' +str(row[10])+'|' +str(row[11])+'|' +str(row[12])+'|' +str(row[13])+'|' +str(row[14])+'|' +str(row[15])+'|' +str(row[16]))
            print(str(Assignment4.count))
        except:
            print ("No data found. Load database from csv")

    def search_data(self,id=""):
        """
        This function is used to search a row based on the id given by user in the entrySearch widget
        it returns a row after searching it from database
        :return: row
        """
        try:
            Assignment4.cursor.execute('select * from food where id =?', id)
            row =Assignment4.cursor.fetchall()
            print (row)
        except:
            print("No id given")
        return "Row"

    def delete_data(self,id=""):
        """
        This function is used to search a row based on the id given by user in the entrySearch widget and delete it from the database
        :return:
        """
        try:
            # self.listbox.bind('<FocusOut>', lambda e: self.listbox.selection_clear(0, END))
            Assignment4.cursor.execute('delete from food where id =?', id)
            Assignment4.db.commit()
            print ("Row deleted with id = " +id)
            Assignment4.read_database(self)
        except:
            print("No id given for deleting")

    def update_data(self, id=""):
        """
        This function is used to search a row based on the id given by user in the entrySearch widget and update it in the database
        :return:
        """
        try:
            # self.listbox.bind('<FocusOut>', lambda e: self.listbox.selection_clear(0, END))
            Assignment4.cursor.execute("""update food set ref_date =?, geo=?, dgu_id=?, food_categories=?, commodity=?,uom=?, uom_id=?,scalar_factor=?,scalar_id=?,vector=?,coordinate=?,value=?,status=?,symbol=?,terminated=?, decimals=? where id =?""",
                                       (self.entryRef_date.get(), self.entryGeo.get(), self.entryDguid.get(),
                                        self.entryCategory.get(), self.entryCommodity.get(), self.entryUom.get(),
                                        self.entryUom_id.get(), self.entryScalar.get(),
                                        self.entryScalar_id.get(), self.entryVector.get(), self.entryCoordinate.get(),
                                        self.entryValue.get(), self.entryStatus.get(), self.entrySymbol.get(),
                                        self.entryTerminated.get(), self.entryDecimal.get(), id))
            Assignment4.db.commit()
            print("Row updated with id = " + id)
            Assignment4.read_database(self)
        except:
            print("No id given for updating")

    def clear_fields(self):
        """
        Clears all the entry widgets
        :return:
        """

        self.entrySearch.delete(0, END)
        self.entryRef_date.delete(0, END)
        self.entryGeo.delete(0, END)
        self.entryDguid.delete(0, END)
        self.entryCategory.delete(0, END)
        self.entryCommodity.delete(0, END)
        self.entryUom.delete(0, END)
        self.entryUom_id.delete(0, END)
        self.entryScalar.delete(0, END)
        self.entryScalar_id.delete(0, END)
        self.entryVector.delete(0, END)
        self.entryCoordinate.delete(0, END)
        self.entryValue.delete(0, END)
        self.entryStatus.delete(0, END)
        self.entrySymbol.delete(0, END)
        self.entryTerminated.delete(0, END)
        self.entryDecimal.delete(0, END)
        return "Field Cleared"


    def insert_data(self):
        """
        This function is used to insert a new record into the database
        user inputs the data into the entry widgets and press Insert button, the data in inserted into the database and all entry widgets are cleared 
        :return:
        """
        Assignment4.cursor.execute('INSERT INTO food (ref_date, geo, dgu_id, food_categories, commodity,uom, uom_id,scalar_factor,scalar_id,vector,coordinate,value,status,symbol,terminated, decimals) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                       (self.entryRef_date.get(),self.entryGeo.get(),self.entryDguid.get(),self.entryCategory.get(),self.entryCommodity.get(),self.entryUom.get(),self.entryUom_id.get(),self.entryScalar.get(),
                        self.entryScalar_id.get(),self.entryVector.get(),self.entryCoordinate.get(),self.entryValue.get(),self.entryStatus.get(),self.entrySymbol.get(),self.entryTerminated.get(),self.entryDecimal.get()))
        Assignment4.db.commit()
        print("New record inserted!!")
        self.clear_fields()
        Assignment4.read_database(self)

    def select_list(self, event):
        """
        it will get the selected line from the listbox and fill the entry widgets based on that line
        :param event:
        :return:
        """
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        value2=value.split("|",16)
        print ("selection:", selection, ": '%s'" % value2)

        self.clear_fields()

        self.entrySearch.insert(0, value2[0])
        self.entryRef_date.insert(0, value2[1])
        self.entryGeo.insert(0, value2[2])
        self.entryDguid.insert(0, value2[3])
        self.entryCategory.insert(0, value2[4])
        self.entryCommodity.insert(0, value2[5])
        self.entryUom.insert(0, value2[6])
        self.entryUom_id.insert(0, value2[7])
        self.entryScalar.insert(0, value2[8])
        self.entryScalar_id.insert(0, value2[9])
        self.entryVector.insert(0, value2[10])
        self.entryCoordinate.insert(0, value2[11])
        self.entryValue.insert(0, value2[12])
        self.entryStatus.insert(0, value2[13])
        self.entrySymbol.insert(0, value2[14])
        self.entryTerminated.insert(0, value2[15])
        self.entryDecimal.insert(0, value2[16])

# main method to create window by calling gui function
if __name__ == '__main__':
    gui()
