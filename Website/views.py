from flask import Blueprint, render_template, flash, request, url_for, redirect
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("base.html")


@views.route('/Display.html')
def Display():
    return render_template("Display.html")

@views.route('/Modify.html')
def Modify():
    return render_template("Modify.html")

@views.route('/Reports.html')
def Reports():
    return render_template("Reports.html")


@views.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        DBcreate = 'Phase5/Website/models/projectDBcreate.sql'
        c = open(DBcreate)
        full_sql = c.read()
        sql_commands = full_sql.replace('\n', ' ').split(';')[:-1]

        for sql_command in sql_commands:
            cursor.execute(sql_command)
            print('Table created')
        
        flash('Tables created Successfully!', category='success')

    return render_template('base.html')

@views.route('/drop', methods = ['GET', 'POST'])
def drop():
    if request.method == 'POST':
        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        DBdrop = 'Phase5/Website/models/projectDBdrop.sql'
        c = open(DBdrop)
        full_sql = c.read()
        sql_commands = full_sql.replace('\n', ' ').split(';')[:-1]

        for sql_command in sql_commands:
            cursor.execute(sql_command)
            print('Table dropped')
        
        flash('Tables dropped Successfully!', category='success')

    return render_template('base.html')

@views.route('/insert', methods = ['GET', 'POST'])
def insert():
    if request.method == 'POST':
        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        DBinsert = 'Phase5/Website/models/projectDBinsert.sql'
        c = open(DBinsert)
        full_sql = c.read()
        sql_commands = full_sql.replace('\n', ' ').split(';')[:-1]

        for sql_command in sql_commands:
            cursor.execute(sql_command)
            connection.commit()
            print('Values Inserted')

        flash('Values inserted Successfully!', category='success')


    return render_template('base.html')


@views.route('/hospital', methods = ['POST'])
def hospital():
    if request.method == 'POST':
        import cx_Oracle
        try:
            connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
            print("Success")
        except Exception as err:
            print("Connection error", err)
        cursor = connection.cursor()
        # query1 = ('insert into Fall22_S004_13_SERVICE(SSID, S_TYPE) VALUES (:SSID, :S_TYPE)')
        query = "select * from Fall22_S004_13_HOSPITAL"
        cursor.execute(query)
        # connection.commit()
        rows = cursor.fetchall()

        return render_template('Hospital_results.html', data = rows)        
    return render_template('base.html')

@views.route('/department', methods = ['POST'])
def department():
    if request.method == 'POST':
        import cx_Oracle
        try:
            connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
            print("Success")
        except Exception as err:
            print("Connection error", err)
        cursor = connection.cursor()
        query = "select * from Fall22_S004_13_DEPARTMENT"
        cursor.execute(query)
        rows = cursor.fetchall()

        return render_template('department_results.html', data = rows)        
    return render_template('base.html')

@views.route('/demployees', methods = ['POST'])
def demployees():
    if request.method == 'POST':
        import cx_Oracle
        try:
            connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
            print("Success")
        except Exception as err:
            print("Connection error", err)
        cursor = connection.cursor()
        query = "select * from Fall22_S004_13_EMPLOYEE"
        cursor.execute(query)
        rows = cursor.fetchall()

        return render_template('demployee_results.html', data = rows)        
    return render_template('base.html')

@views.route('/patient', methods = ['POST'])
def patient():
    if request.method == 'POST':
        import cx_Oracle
        try:
            connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
            print("Success")
        except Exception as err:
            print("Connection error", err)
        cursor = connection.cursor()
        # query1 = ('insert into Fall22_S004_13_SERVICE(SSID, S_TYPE) VALUES (:SSID, :S_TYPE)')
        # query = "select * from Fall22_S004_13_PATIENT"
        query = 'SELECT P.PID, P2.PA_ID, FNAME, MNAME, LNAME, P_ADDRESS, GENDER, BDATE, PH_NO, HID, S_DATE, E_DATE, AILMENT FROM Fall22_S004_13_PERSON P, Fall22_S004_13_PATIENT P2, Fall22_S004_13_PERSON_PHNO P3, Fall22_S004_13_PATIENT_AILMENT P4 WHERE P.PID = P2.PID AND P.PID = P3.PID AND P2.PA_ID = P4.PA_ID'
        cursor.execute(query)
        # connection.commit()
        rows = cursor.fetchall()

        return render_template('Patient_results.html', data = rows)        
    return render_template('base.html')

@views.route('/orders', methods = ['POST'])
def orders():
    if request.method == 'POST':
        import cx_Oracle
        try:
            connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
            print("Success")
        except Exception as err:
            print("Connection error", err)
        cursor = connection.cursor()
        # query1 = ('insert into Fall22_S004_13_SERVICE(SSID, S_TYPE) VALUES (:SSID, :S_TYPE)')
        query = "select * from Fall22_S004_13_ORDERS"
        cursor.execute(query)
        rows = cursor.fetchall()

        return render_template('orders_results.html', data = rows)        
    return render_template('base.html')




@views.route('modify_insert.html', methods = ['GET', 'POST'])
def modify_insert():
    return render_template("modify_insert.html")

@views.route('modify_update.html', methods = ['GET', 'POST'])
def modify_update():
    return render_template("modify_update.html")

@views.route('modify_delete.html', methods = ['GET', 'POST'])
def modify_delete():
    return render_template("modify_delete.html")


@views.route('patient_frequency.html', methods = ['GET', 'POST'])
def patient_frequency():
    if request.method == "POST":
        # from datetime import datetime
        # import calendar
        # testdate = datetime(2018, 6, 4)
        # res = calendar.monthrange(testdate.year, testdate.month)[1]


        s_date = request.form.get('S_DATE')
        e_date = request.form.get('E_DATE')
        month = request.form.get('month')
        year = request.form.get('year')

        print(type(year[-2:]))
        print(type(month))
        t = year[-2:]
        S_mon = s_date + "-" + month + "-" + t
        E_mon = e_date + "-" + month + "-" + t
        print(S_mon)
        print(E_mon)

        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        query = """ SELECT COUNT(*) AS NUMBER_OF_PATIENTS, HID
            FROM fall22_s004_13_PATIENT
            where (S_DATE >= :S_mon AND S_DATE  <= :E_mon ) OR (E_DATE >= :S_mon AND E_DATE  <= :E_mon)
            GROUP BY HID
            ORDER BY COUNT(*) DESC"""
        

        t = 10
        cursor.execute(query, [S_mon, E_mon, S_mon, E_mon])
        out = cursor.fetchall()
        # print(out)

        return render_template("patient_freq_results.html", data = out)

    
    import cx_Oracle
    connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
    cursor = connection.cursor()
    cursor.execute(""" SELECT DISTINCT EXTRACT(YEAR FROM S_DATE) FROM Fall22_S004_13_PATIENT UNION SELECT DISTINCT EXTRACT(YEAR FROM E_DATE) FROM Fall22_S004_13_PATIENT""")
    temp = cursor.fetchall()
    test = temp[:-1]
    return render_template("patient_frequency.html", data = test)

@views.route('/age_group', methods = ['POST'])
def age_group():
    if request.method == 'POST':
        import cx_Oracle
        try:
            connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
            print("Success")
        except Exception as err:
            print("Connection error", err)
        cursor = connection.cursor()
        query = """SELECT count(patientID) AS NUMBER_OF_PATIENTS , Age FROM (
            SELECT pa.Pa_ID as patientID , TRUNC(months_between(sysdate, pe.Bdate) / 12) AS Age FROM fall22_s004_13_patient pa INNER JOIN fall22_s004_13_person pe ON pa.PID = pe.PID)
            GROUP BY rollup(Age)
            ORDER BY count(patientID) DESC
            FETCH FIRST 5 rows ONLY"""
        cursor.execute(query)
        rows = cursor.fetchall()

        return render_template('age_group.html', data = rows)        
    return render_template('base.html')



@views.route('modify_insert_hospital.html', methods = ['GET', 'POST'])
def modify_insert_hospital():
    if request.method == "POST":
        HNAME = request.form.get('Hname')
        STREET = request.form.get('Street')
        CITY = request.form.get('City')
        ZIP = request.form.get('ZIP')
        REGIONID = request.form.get('RegionID')
        REGISTERED_BEDS = request.form.get('Registered_beds')
        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        cursor.execute("SELECT HID FROM Fall22_S004_13_HOSPITAL ORDER BY HID DESC FETCH FIRST 1 ROWS ONLY")
        temp_HID = cursor.fetchall()
        HID = temp_HID[0][0] + 1

        query1 = ('insert into Fall22_S004_13_HOSPITAL(HID, HNAME, STREET, CITY, ZIP, REGIONID, REGISTERED_BEDS) VALUES (:HID, :HNAME, :STREET, :CITY, :ZIP, :REGIONID, :REGISTERED_BEDS)')

        cursor.execute(query1, [HID, HNAME, STREET, CITY, ZIP, REGIONID, REGISTERED_BEDS])
        connection.commit()
        flash("The data was added Successfully", category = "success")

        return render_template("base.html")

    return render_template("modify_insert_hospital.html")

@views.route('modify_insert_patient.html', methods = ['GET', 'POST'])
def modify_insert_patient():
    if request.method == "POST":
        FNAME = request.form.get('Hname')
        MNAME = request.form.get('Mname')
        LNAME = request.form.get('Lname')
        ADDRESS = request.form.get('Address')
        GENDER = request.form.get('Gender')
        BDATE = request.form.get('Bdate')
        PH_NO = request.form.get('Ph_no')
        S_DATE = request.form.get('S_DATE')
        E_DATE = request.form.get('E_DATE')
        AILMENT = request.form.get('AILMENT')
        HID = request.form.get('HID')
        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        cursor.execute("SELECT PID FROM Fall22_S004_13_PERSON ORDER BY PID DESC FETCH FIRST 1 ROWS ONLY")
        temp_PID = cursor.fetchall()
        PID = temp_PID[0][0] + 1
        query1 = ('insert into Fall22_S004_13_PERSON(PID, FNAME, MNAME, LNAME, P_ADDRESS, GENDER, BDATE) VALUES (:PID, :FNAME, :MNAME, :LNAME, :ADDRESS, :GENDER, :BDATE)')
        cursor.execute(query1, [PID, FNAME, MNAME, LNAME, ADDRESS, GENDER, BDATE])
        connection.commit()
        query2 = ('insert into Fall22_S004_13_PERSON_PHNO(PID, PH_NO) VALUES (:PID, :PH_NO)')
        cursor.execute(query2, [PID, PH_NO])
        connection.commit()
        cursor.execute("SELECT PA_ID FROM Fall22_S004_13_PATIENT ORDER BY PA_ID DESC FETCH FIRST 1 ROWS ONLY")
        temp_PA_ID = cursor.fetchall()
        PA_ID = temp_PA_ID[0][0] + 1
        query3 = ('insert into Fall22_S004_13_PATIENT(PID, PA_ID, HID, S_DATE, E_DATE) VALUES (:PID, :PA_ID, :HID, :S_DATE, :E_DATE)')
        cursor.execute(query3, [PID, PA_ID, HID, S_DATE, E_DATE])
        connection.commit()
        al = ('insert into Fall22_S004_13_PATIENT_AILMENT(PA_ID, AILMENT) VALUES (:PA_ID, :AILMENT)')
        cursor.execute(al, [PA_ID, AILMENT])
        connection.commit()
        flash("The data was added Successfully", category = "success")


        # query1 = ('insert into Fall22_S004_13_HOSPITAL(HID, HNAME, STREET, CITY, ZIP, REGIONID, REGISTERED_BEDS) VALUES (:HID, :HNAME, :STREET, :CITY, :ZIP, :REGIONID, :REGISTERED_BEDS)')

        # cursor.execute(query1, [HID, HNAME, STREET, CITY, ZIP, REGIONID, REGISTERED_BEDS])
        # connection.commit()

        return render_template("base.html")

    import cx_Oracle
    connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
    cursor = connection.cursor()
    cursor.execute("SELECT HID FROM Fall22_S004_13_HOSPITAL ORDER BY HID ASC")
    TEMP_HID = cursor.fetchall()

    return render_template("modify_insert_patient.html", TEMP_HID = TEMP_HID)

@views.route('employee_list.html', methods = ['GET', 'POST'])
def employee_list():
    if request.method == "POST":
        EMPTYPE = request.form.get("EMPTYPE")
        print(EMPTYPE)

        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        sql = """select eid, fname, lname, ssn from Fall22_S004_13_PERSON p,Fall22_S004_13_EMPLOYEE e where p.pid=e.pid AND emptype = :EMPTYPE"""
        cursor.execute(sql, [EMPTYPE])
        out = cursor.fetchall()

        return render_template("employee_results.html", data = out)

    return render_template("employee_list.html")


@views.route('modify_update_hospital.html', methods = ['GET', 'POST'])
def modify_update_hospital():
    

    if request.method == "POST":
        HNAME = request.form.get('Hname')
        STREET = request.form.get('Street')
        CITY = request.form.get('City')
        ZIP = request.form.get('ZIP')
        REGIONID = request.form.get('RegionID')
        REGISTERED_BEDS = request.form.get('Registered_beds')
        HID = request.form.get('HID')
        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        QUERY1 =  ("UPDATE Fall22_S004_13_HOSPITAL SET HNAME = :HNAME, STREET = :STREET, CITY = :CITY, ZIP = :ZIP, REGIONID = :REGIONID, REGISTERED_BEDS = :REGISTERED_BEDS WHERE HID = :HID")

        cursor.execute(QUERY1, [HNAME, STREET, CITY, ZIP, REGIONID, REGISTERED_BEDS, HID])
        connection.commit()
        flash("The update was successfull", category="success")

        return render_template("base.html")

    import cx_Oracle
    connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
    cursor = connection.cursor()
    cursor.execute("SELECT HID FROM Fall22_S004_13_HOSPITAL ORDER BY HID")
    temp_HID = cursor.fetchall()
    return render_template("modify_update_hospital.html", HID = temp_HID)


@views.route('modify_update_patient.html', methods = ['GET', 'POST'])
def modify_update_patient():
    

    if request.method == "POST":
        DISCHARGED_DATE = request.form.get('DISCHARGED_DATE')
        PA_ID = request.form.get('PA_ID')
        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        QUERY1 =  ("UPDATE Fall22_S004_13_PATIENT SET E_DATE = :E_DATE WHERE PA_ID = :PA_ID")

        cursor.execute(QUERY1, [DISCHARGED_DATE, PA_ID])
        connection.commit()
        flash("The update was successfull", category="success")

        return render_template("base.html")

    import cx_Oracle
    connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
    cursor = connection.cursor()
    cursor.execute("SELECT PA_ID FROM Fall22_S004_13_PATIENT ORDER BY PA_ID")
    temp_PA_ID = cursor.fetchall()
    return render_template("modify_update_patient.html", PA_ID = temp_PA_ID)



@views.route('modify_delete_hospital.html', methods = ['GET', 'POST'])
def modify_delete_hospital():
    

    if request.method == "POST":
        HID = request.form.get('HID')
        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        QUERY1 =  ("DELETE FROM Fall22_S004_13_HOSPITAL WHERE HID = :HID ")

        cursor.execute(QUERY1, [HID])
        connection.commit()

        flash("Deleted Successfully", category="success")

        return render_template("base.html")

    import cx_Oracle
    connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
    cursor = connection.cursor()
    cursor.execute("SELECT HID FROM Fall22_S004_13_HOSPITAL ORDER BY HID")
    temp_HID = cursor.fetchall()
    return render_template("modify_delete_hospital.html", HID = temp_HID)

@views.route('modify_delete_employee.html', methods = ['GET', 'POST'])
def modify_delete_employee():
    

    if request.method == "POST":
        EID = request.form.get('EID')
        import cx_Oracle
        connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
        cursor = connection.cursor()
        QUERY1 =  ("SELECT PID FROM Fall22_S004_13_EMPLOYEE WHERE EID = :EID ")
        cursor.execute(QUERY1, [EID])
        TEMP_PID = cursor.fetchall()
        print(TEMP_PID)
        PID = TEMP_PID[0][0]
        print(PID)
        QUERY4 = ("DELETE FROM Fall22_S004_13_PERSON_PHNO WHERE PID = :PID ")
        cursor.execute(QUERY4, [PID])
        connection.commit()
        QUERY3 = ("DELETE FROM Fall22_S004_13_EMPLOYEE WHERE EID = :EID ")
        cursor.execute(QUERY3, [EID])
        connection.commit()
        QUERY2 = ("DELETE FROM Fall22_S004_13_PERSON WHERE PID = :PID ")
        cursor.execute(QUERY2, [PID])
        connection.commit()
        
       
        
       
        flash("Deleted Successfully", category="success")
        return render_template("base.html")

    import cx_Oracle
    connection = cx_Oracle.connect('pxk5233/DatabasePraveen30@az6F72ldbp1.az.uta.edu:1523/pcse1p.data.uta.edu')
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT E.EID FROM Fall22_S004_13_EMPLOYEE E, Fall22_S004_13_DEPARTMENT D WHERE E.EID NOT IN (SELECT E.EID FROM Fall22_S004_13_EMPLOYEE E, Fall22_S004_13_DEPARTMENT D WHERE E.EID=D.EID) ORDER BY E.EID")

    temp_EID = cursor.fetchall()
    return render_template("modify_delete_employee.html", EID = temp_EID)


