from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1350x750+0+0")  # width x height + x-axis + y-axis

        # =================Variables=================
        self.memberType = StringVar()
        self.prnNo = StringVar()
        self.idVar = StringVar()
        self.firstName = StringVar()
        self.lastName = StringVar()
        self.address1 = StringVar()
        self.address2 = StringVar()
        self.postCode = StringVar()
        self.mobileNo = StringVar()
        self.bookID = StringVar()
        self.bookTitle = StringVar()
        self.author = StringVar()
        self.dateBorrowed = StringVar()
        self.dateDue = StringVar()
        self.daysOnBook = StringVar()
        self.lateReturnFine = StringVar()
        self.dateOverDue = StringVar()
        self.finalPrice = StringVar()

        lbltitle = Label(
            self.root,
            text="LIBRARY MANAGEMENT SYSTEM",
            font=("times new roman", 40, "bold"),
            bg="sky blue",
            fg="green",
            bd=18,
            relief=RIDGE,
            padx=2,
            pady=6,
        )
        lbltitle.pack(side=TOP, fill=X)

        # =================Data-frame=================
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="sky blue")
        frame.place(x=0, y=103, width=1280, height=390)  # 2nd out-box

        # box inside 2nd out-box
        # =================Data-frame-left=================
        DataFrameLeft = LabelFrame(
            frame,
            text="Library Membership information",
            font=("times new roman", 12, "bold"),
            bg="sky blue",
            fg="green",
            bd=12,
            relief=RIDGE,
            padx=2,
            pady=6,
        )
        DataFrameLeft.place(x=0, y=5, width=740, height=355)

        lblMemberType = Label(
            DataFrameLeft,
            text="Member Type",
            bg="sky blue",
            font=("times new roman", 13, "bold"),
            padx=2,
            pady=6,
        )
        lblMemberType.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(
            DataFrameLeft,
            font=("times new roman", 12, "bold"),
            width=27,
            textvariable=self.memberType,
            state="readonly",
        )
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(
            DataFrameLeft,
            text="PRN No",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(
            DataFrameLeft,
            font=("times new roman", 12, "bold"),
            textvariable=self.prnNo,
            width=30,
        )
        txtPRN_No.grid(row=1, column=1)

        lblID = Label(
            DataFrameLeft,
            text="ID No:",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=4,
        )
        lblID.grid(row=2, column=0, sticky=W)
        txtID = Entry(
            DataFrameLeft,
            font=("times new roman", 13, "bold"),
            textvariable=self.idVar,
            width=27,
        )
        txtID.grid(row=2, column=1)

        lblFirstName = Label(
            DataFrameLeft,
            text="First Name",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(
            DataFrameLeft,
            textvariable=self.firstName,
            font=("times new roman", 13, "bold"),
            width=27,
        )
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(
            DataFrameLeft,
            text="Last Name",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(
            DataFrameLeft,
            textvariable=self.lastName,
            font=("times new roman", 13, "bold"),
            width=27,
        )
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(
            DataFrameLeft,
            text="Address 1",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(
            DataFrameLeft,
            textvariable=self.address1,
            font=("times new roman", 13, "bold"),
            width=27,
        )
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(
            DataFrameLeft,
            text="Address 2",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(
            DataFrameLeft,
            textvariable=self.address2,
            font=("times new roman", 13, "bold"),
            width=27,
        )
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(
            DataFrameLeft,
            text="Post Code",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=4,
        )
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(
            DataFrameLeft,
            textvariable=self.postCode,
            font=("times new roman", 13, "bold"),
            width=27,
        )
        txtPostCode.grid(row=7, column=1)

        lblMobileNo = Label(
            DataFrameLeft,
            text="Mobile No",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblMobileNo.grid(row=8, column=0, sticky=W)
        txtMobileNo = Entry(
            DataFrameLeft,
            textvariable=self.mobileNo,
            font=("times new roman", 13, "bold"),
            width=27,
        )
        txtMobileNo.grid(row=8, column=1)

        lblBookID = Label(
            DataFrameLeft,
            text="Book ID:",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
        )
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID = Entry(
            DataFrameLeft,
            textvariable=self.bookID,
            font=("times new roman", 12, "bold"),
            width=27,
        )
        txtBookID.grid(row=0, column=3)

        lblBookTitle = Label(
            DataFrameLeft,
            text="Book Title:",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(
            DataFrameLeft,
            textvariable=self.bookTitle,
            font=("times new roman", 12, "bold"),
            width=27,
        )
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(
            DataFrameLeft,
            text="Author:",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(
            DataFrameLeft,
            font=("times new roman", 12, "bold"),
            textvariable=self.author,
            width=27,
        )
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed = Label(
            DataFrameLeft,
            text="Borrow Date:",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(
            DataFrameLeft,
            font=("times new roman", 12, "bold"),
            width=27,
            textvariable=self.dateBorrowed,
        )
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(
            DataFrameLeft,
            text="Due Date:",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(
            DataFrameLeft,
            font=("times new roman", 12, "bold"),
            textvariable=self.dateDue,
            width=27,
        )
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(
            DataFrameLeft,
            text="Days on Book:",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(
            DataFrameLeft,
            textvariable=self.daysOnBook,
            font=("times new roman", 12, "bold"),
            width=27,
        )
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(
            DataFrameLeft,
            text="Late Return Fine:",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        textLateReturnFine = Entry(
            DataFrameLeft,
            font=("times new roman", 12, "bold"),
            width=27,
            textvariable=self.lateReturnFine,
        )
        textLateReturnFine.grid(row=6, column=3)

        lblDateOverDue = Label(
            DataFrameLeft,
            text="Date Over Due:",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue = Entry(
            DataFrameLeft,
            font=("times new roman", 12, "bold"),
            width=27,
            textvariable=self.dateOverDue,
        )
        txtDateOverDue.grid(row=7, column=3)

        lblFinalPrice = Label(
            DataFrameLeft,
            text="Final Price:",
            bg="sky blue",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblFinalPrice.grid(row=8, column=2, sticky=W)
        txtFinalPrice = Entry(
            DataFrameLeft,
            font=("times new roman", 12, "bold"),
            width=27,
            textvariable=self.finalPrice,
        )
        txtFinalPrice.grid(row=8, column=3)

        # =================Data-frame-right=================
        DataFrameRight = LabelFrame(
            frame,
            text="Book Details",
            font=("arial", 12, "bold"),
            bg="sky blue",
            fg="green",
            bd=12,
            relief=RIDGE,
            padx=2,
            pady=6,
        )
        DataFrameRight.place(x=750, y=5, width=470, height=355)

        self.txtBox = Text(
            DataFrameRight,
            font=("times new roman", 12, "bold"),
            width=30,
            height=16,
            padx=2,
            pady=6,
        )
        self.txtBox.grid(row=0, column=2)

        listScrollBar = Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky="ns")

        listBooks = [
            "Clean Code",
            "Theory of Computation",
            "The Pragmatic Programmer",
            "Design Patterns",
            "Cracking the Coding Interview",
            "Operating System Concepts",
            "Artificial Intelligence",
            "Introduction to Algorithms",
            "The C Programming Language",
            "Computer Networks",
            "Compilers",
            "Code Complete",
            "Programming Pearls",
            "Introduction to Database Systems",
            "Refactoring",
            "The Mythical man-month",
            "Head First Design Patterns",
            "Algorithms to live by",
            "The Art of computer programming",
            "Introduction to machine learning",
            "Database System Concepts",
            "Data Structures and Algorithms in Python",
            "Domain-Driven Design",
            "Python Cookbook",
            "Python Crash Course",
        ]

        def selectedBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "Clean Code":
                self.bookID.set("BK001")
                self.bookTitle.set("The Clean Coding")
                self.author.set("Robert Cecil Martin")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateBorrowed.set(d1)
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.900")
            if x == "Theory of Computation":
                self.bookID.set("BK002")
                self.bookTitle.set("Computation Theory")
                self.author.set("Michael Sipser")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateBorrowed.set(d1)
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.700")
            if x == "The Pragmatic Programmer":
                self.bookID.set("BK003")
                self.bookTitle.set("Programmer`s Guide")
                self.author.set("David Thomas and Andrew Hunt")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateBorrowed.set(d1)
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.1000")
            if x == "Design Patterns":
                self.bookID.set("BK004")
                self.bookTitle.set("Design Patterns")
                self.author.set("Erich Gamma, Richard Helm")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateBorrowed.set(d1)
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.760")
            if x == "Cracking the Coding Interview":
                self.bookID.set("BK005")
                self.bookTitle.set("Coding Interview")
                self.author.set("Gayle Laakmann McDowell")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateBorrowed.set(d1)
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.960")
            if x == "Operating System Concepts":
                self.bookID.set("BK006")
                self.bookTitle.set("Operating System Concepts")
                self.author.set(" Ralph Johnson, John Vlissides")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateBorrowed.set(d1)
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.890")
            if x == "Artificial Intelligence":
                self.bookID.set("BK007")
                self.bookTitle.set("Artificial Intelligence")
                self.author.set("Stuart Russell, Peter Norvig")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateBorrowed.set(d1)
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.769")
            if x == "Introduction to Algorithms":
                self.bookID.set("BK008")
                self.bookTitle.set("Algorithms")
                self.author.set("Thomas H. Cormen, Charles E. Leiserson")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateBorrowed.set(d1)
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.2090")
            if x == "The C Programming Language":
                self.bookID.set("BK009")
                self.bookTitle.set("C Programming Language")
                self.author.set("Brian W. Kernighan, Dennis M. Ritchie")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateBorrowed.set(d1)
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.450")
            if x == "Computer Networks":
                self.bookID.set("BK010")
                self.bookTitle.set("Computer Networks")
                self.author.set("Andrew S. Tanenbaum")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateBorrowed.set(d1)
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.690")
            if x == "Compilers":
                self.bookID.set("BK011")
                self.bookTitle.set("Compilers")
                self.author.set("Alfred V. Aho, Ravi Sethi")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.780")
            if x == "Code Complete":
                self.bookID.set("BK012")
                self.bookTitle.set("Code Complete")
                self.author.set("Steve McConnell")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.890")
            if x == "Programming Pearls":
                self.bookID.set("BK013")
                self.bookTitle.set("Programming Pearls")
                self.author.set("Jon Bentley")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.670")
            if x == "Introduction to Database Systems":
                self.bookID.set("BK014")
                self.bookTitle.set("Database Systems")
                self.author.set("C. J. Date, Hugh Darwen, Nikos A. Lorentzos")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.990")
            if x == "Refactoring":
                self.bookID.set("BK015")
                self.bookTitle.set("Refactoring")
                self.author.set("Martin Fowler, Kent Beck")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.590")
            if x == "The Mythical man-month":
                self.bookID.set("BK016")
                self.bookTitle.set("Mythical man-month")
                self.author.set("Frederick P. Brooks Jr.")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.650")
            if x == "Head First Design Patterns":
                self.bookID.set("BK017")
                self.bookTitle.set("Head First Design Patterns")
                self.author.set("Eric Freeman, Elisabeth Robson")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.550")
            if x == "Algorithms to live by":
                self.bookID.set("BK018")
                self.bookTitle.set("Algorithms to live by")
                self.author.set("Brian Christian, Tom Griffiths")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.670")
            if x == "The Art of computer programming":
                self.bookID.set("BK019")
                self.bookTitle.set("Art of computer programming")
                self.author.set("Donald Knuth")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.790")
            if x == "Introduction to machine learning":
                self.bookID.set("BK020")
                self.bookTitle.set("Introduction to machine learning")
                self.author.set("Ethem Alpaydin")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.890")
            if x == "Database System Concepts":
                self.bookID.set("BK021")
                self.bookTitle.set("Database System Concepts")
                self.author.set("Abraham Silberschatz, Henry F. Korth")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.990")
            if x == "Data Structures and Algorithms in Python":
                self.bookID.set("BK022")
                self.bookTitle.set("Data Structures and Algorithms in Python")
                self.author.set("Michael T. Goodrich, Roberto Tamassia")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.390")
            if x == "Domain-Driven Design":
                self.bookID.set("BK023")
                self.bookTitle.set("Domain-Driven Design")
                self.author.set("Eric Evans, Martin Fowler")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.690")
            if x == "Python Cookbook":
                self.bookID.set("BK024")
                self.bookTitle.set("Python Cookbook")
                self.author.set("David Beazley, Brian K. Jones")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.490")
            if x == "Python Crash Course":
                self.bookID.set("BK025")
                self.bookTitle.set("Python Crash Course")
                self.author.set("Eric Matthes")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateDue.set(d3)
                self.daysOnBook.set(15)
                self.lateReturnFine.set("Rs.50")
                self.dateOverDue.set("NO")
                self.finalPrice.set("Rs.990")

            
            
            

        listBox = Listbox(
            DataFrameRight, font=("times new roman", 12, "bold"), width=20, height=15
        )
        listBox.bind("<<ListboxSelect>>", selectedBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # =================Buttons Frame=================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="sky blue")
        Framebutton.place(x=0, y=490, width=1280, height=60)

        btnAddData = Button(
            Framebutton,
            text="Add Data",
            command=self.add_data,
            font=("times new roman", 12, "bold"),
            width=22,
            bg="blue",
            fg="white",
        )
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(
            Framebutton,
            text="Show Data",
            command=self.showData,
            font=("times new roman", 12, "bold"),
            width=22,
            bg="blue",
            fg="white",
        )
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(
            Framebutton,
            text="Update",
            command=self.update,
            font=("times new roman", 12, "bold"),
            width=21,
            bg="blue",
            fg="white",
        )
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(
            Framebutton,
            text="Delete",
            command=self.delete,
            font=("times new roman", 12, "bold"),
            width=21,
            bg="blue",
            fg="white",
        )
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(
            Framebutton,
            text="Reset",
            command=self.reset,
            font=("times new roman", 12, "bold"),
            width=21,
            bg="blue",
            fg="white",
        )
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(
            Framebutton,
            text="Exit",
            command=self.iExit,
            font=("times new roman", 12, "bold"),
            width=21,
            bg="blue",
            fg="white",
        )
        btnAddData.grid(row=0, column=5)

        # =================Information Frame=================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="sky blue")
        FrameDetails.place(x=0, y=548, width=1280, height=150)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="sky blue")
        Table_frame.place(x=0, y=2, width=1220, height=123)

        xscroll = Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(
            Table_frame,
            columns=(
                "membertype",
                "prnno",
                "title",
                "firstname",
                "lastname",
                "address1",
                "address2",
                "postid",
                "mobile",
                "bookid",
                "booktitle",
                "author",
                "dateborrowed",
                "datedue",
                "days",
                "latereturnfine",
                "dateoverdue",
                "finalprice",
            ),
            xscrollcommand=xscroll.set,
            yscrollcommand=yscroll.set,
        )

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile No.")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Borrow Date")
        self.library_table.heading("datedue", text="Due Date")
        self.library_table.heading("days", text="Days on Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):
        connect = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Sarthak@123",
            database="mydatabase",
        )
        my_cursor = connect.cursor()
        my_cursor.execute(
            "insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                self.memberType.get(),
                self.prnNo.get(),
                self.idVar.get(),
                self.firstName.get(),
                self.lastName.get(),
                self.address1.get(),
                self.address2.get(),
                self.postCode.get(),
                self.mobileNo.get(),
                self.bookID.get(),
                self.bookTitle.get(),
                self.author.get(),
                self.dateBorrowed.get(),
                self.dateDue.get(),
                self.daysOnBook.get(),
                self.lateReturnFine.get(),
                self.dateDue.get(),
                self.finalPrice.get(),
            ),
        )

        connect.commit()
        self.fatch_data()
        connect.close()

        messagebox.showinfo("Success", "Record has been inserted")

    def update(self):
        connect = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Sarthak@123",
            database="mydatabase",
        )
        my_cursor = connect.cursor()
        my_cursor.execute(
            "update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostCode=%s,Mobile=%s,BookId=%s,BookTitle=%s,Author=%s,DateBorrowed=%s,DateDue=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDue=%s,FinalPrice=%s where PRN_NO=%s",
            (
                self.memberType.get(),
                self.idVar.get(),
                self.firstName.get(),
                self.lastName.get(),
                self.address1.get(),
                self.address2.get(),
                self.postCode.get(),
                self.mobileNo.get(),
                self.bookID.get(),
                self.bookTitle.get(),
                self.author.get(),
                self.dateBorrowed.get(),
                self.dateDue.get(),
                self.daysOnBook.get(),
                self.lateReturnFine.get(),
                self.dateOverDue.get(),
                self.finalPrice.get(),
                self.prnNo.get(),
            ),
        )
        connect.commit()
        self.fatch_data()
        self.reset()
        connect.close()

        messagebox.showinfo("Success", "Record has been updated")

    def fatch_data(self):
        connect = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Sarthak@123",
            database="mydatabase",
        )
        my_cursor = connect.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            connect.commit()
        connect.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]

        self.memberType.set(row[0]),
        self.prnNo.set(row[1]),
        self.idVar.set(row[2]),
        self.firstName.set(row[3]),
        self.lastName.set(row[4]),
        self.address1.set(row[5]),
        self.address2.set(row[6]),
        self.postCode.set(row[7]),
        self.mobileNo.set(row[8]),
        self.bookID.set(row[9]),
        self.bookTitle.set(row[10]),
        self.author.set(row[11]),
        self.dateBorrowed.set(row[12]),
        self.dateDue.set(row[13]),
        self.daysOnBook.set(row[14]),
        self.lateReturnFine.set(row[15]),
        self.dateOverDue.set(row[16]),
        self.finalPrice.set(row[17])
    
    def showData(self):
        self.txtBox.insert(END, "Member Type:\t" + self.memberType.get() + "\n")
        self.txtBox.insert(END, "PRN No.:\t" + self.prnNo.get() + "\n")
        self.txtBox.insert(END, "ID:\t" + self.idVar.get() + "\n")
        self.txtBox.insert(END, "First Name:\t" + self.firstName.get() + "\n")
        self.txtBox.insert(END, "Last Name:\t" + self.lastName.get() + "\n")
        self.txtBox.insert(END, "Address 1:\t" + self.address1.get() + "\n")
        self.txtBox.insert(END, "Address 2:\t" + self.address2.get() + "\n")
        self.txtBox.insert(END, "Post Code:\t" + self.postCode.get() + "\n")
        self.txtBox.insert(END, "Mobile No.:\t" + self.mobileNo.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t" + self.bookID.get() + "\n")
        self.txtBox.insert(END, "BookTitle:\t" + self.bookTitle.get() + "\n")
        self.txtBox.insert(END, "Author:\t" + self.author.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed:\t" + self.dateBorrowed.get() + "\n")
        self.txtBox.insert(END, "Date Due:\t" + self.dateDue.get() + "\n")
        self.txtBox.insert(END, "DaysOnBook:\t" + self.daysOnBook.get() + "\n")
        self.txtBox.insert(END, "LateReturnFine:\t" + self.lateReturnFine.get() + "\n")
        self.txtBox.insert(END, "Date Over Due:\t" + self.dateOverDue.get() + "\n")
        self.txtBox.insert(END, "Final Price:\t" + self.finalPrice.get() + "\n")

    def reset(self):
       self.memberType.set(""),
       self.prnNo.set(""),
       self.idVar.set(""),
       self.firstName.set(""),
       self.lastName.set(""),
       self.address1.set(""),
       self.address2.set(""),
       self.postCode.set(""),
       self.mobileNo.set(""),
       self.bookID.set(""),
       self.bookTitle.set(""),
       self.author.set(""),
       self.dateBorrowed.set(""),
       self.dateDue.set(""),
       self.daysOnBook.set(""),
       self.lateReturnFine.set(""),
       self.dateOverDue.set(""),
       self.finalPrice.set("")
       self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit?")
        if iExit > 0:
            self.root.destroy()
            return

    def delete(self):
        if self.prnNo.get() == "" or self.idVar.get() == "":
            messagebox.showerror("Error", "First select the Member")
        else:
            connect = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Sarthak@123",
                database="mydatabase",
            )
            my_cursor = connect.cursor()
            query = "delete from library where PRN_NO=%s"
            value = (self.prnNo.get(),)
            my_cursor.execute(query, value)
            connect.commit()
            self.fatch_data()
            self.reset()
            connect.close()

            messagebox.showinfo("Success", "Record has been deleted")


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
