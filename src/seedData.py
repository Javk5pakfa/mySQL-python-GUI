import getpass
import mysql.connector
from mysql.connector import Error


def database_connection(hostname, username, password, database_name):
    try:
        connection = mysql.connector.connect(host=hostname,
                                             user=username,
                                             password=password)
        if connection.is_connected():
            print("1st connection successful.")
            cursor = connection.cursor()
            print("create database " + database_name)
            cursor.execute("create database " + database_name)
        else:
            print("Connection error.")
            quit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("1st connection is closed")
        else:
            print("Error while closing connection.")
            quit()

    # 2nd connection, where the bulk of the operation is located.
    try:
        connection = mysql.connector.connect(host=hostname,
                                             database=database_name,
                                             user=username,
                                             password=password)
        if connection.is_connected():
            print("2nd connection successful.")
            cursor = connection.cursor()

            # Create table region.
            cursor.execute("CREATE TABLE region ("
                           "Region_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                           "Region_Name CHAR(2) UNIQUE NOT NULL)")

            connection.commit()

            # Insert region data into region.
            cursor.execute("insert into region(Region_Name) values ('NW')")
            cursor.execute("insert into region(Region_Name) values ('SW')")
            cursor.execute("insert into region(Region_Name) values ('MN')")
            cursor.execute("insert into region(Region_Name) values ('MS')")
            cursor.execute("insert into region(Region_Name) values ('NE')")
            cursor.execute("insert into region(Region_Name) values ('SE')")

            connection.commit()

            # Insert table skill.
            cursor.execute(
                "CREATE TABLE skill ("
                "Skill_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                "Skill_Descrpt VARCHAR(255) UNIQUE NOT NULL,"
                "Skill_Rate FLOAT NOT NULL)")

            connection.commit()

            # Insert data into skill.
            cursor.execute("insert into skill(Skill_Descrpt, Skill_Rate) values"
                           "('Data Entry I', 30.0),"
                           "('Data Entry II', 50.0),"
                           "('Systems Analyst I', 30.0),"
                           "('Systems Analyst II', 50.0),"
                           "('DB Designer I', 60.0),"
                           "('DB Designer II', 80.0),"
                           "('Cobol I', 40.0),"
                           "('Cobol II', 60.0),"
                           "('C++ I', 50.0),"
                           "('C++ II', 70.0),"
                           "('VB I', 40.0),"
                           "('VB II', 60.0),"
                           "('ColdFusion I', 30.0),"
                           "('ColdFusion II', 50.0),"
                           "('ASP I', 70.0),"
                           "('ASP II', 80.0),"
                           "('Oracle DBA', 120.0),"
                           "('SQL Server DBA', 120.0),"
                           "('Network Engineer I', 90.0),"
                           "('Network Engineer II', 100.0),"
                           "('Web Administrator', 80.0),"
                           "('Technical Writer', 40.0),"
                           "('Project Manager', 150.0)")

            connection.commit()

            # Insert table customer.
            cursor.execute("CREATE TABLE customer ("
                           "Cus_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                           "Region_ID INT NOT NULL,"
                           "Cus_Name VARCHAR(255) NOT NULL,"
                           "Cus_Phone VARCHAR(255),"
                           "FOREIGN KEY (Region_ID)"
                           "REFERENCES region (Region_ID))")

            connection.commit()

            # Insert table employee.
            cursor.execute("CREATE TABLE employee ("
                           "Emp_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                           "Region_ID INT NOT NULL,"
                           "Emp_Lname VARCHAR(255) NOT NULL,"
                           "Emp_Mi CHAR(1),"
                           "Emp_Fname VARCHAR(255) NOT NULL,"
                           "Emp_Hiredate DATE NOT NULL,"
                           "FOREIGN KEY (Region_ID)"
                           "REFERENCES region (Region_ID))")

            connection.commit()

            # Insert data into employee.
            cursor.execute(
                "insert into employee(Emp_ID, Region_ID, Emp_Lname, Emp_Fname, EMP_Hiredate)"
                "values (501,"
                "(select Region_ID from region where Region_Name = 'NW'),"
                "'Connor', 'Sean', '1990/01/02')")

            connection.commit()

            cursor.execute(
                "insert into employee(Region_ID, Emp_Lname, Emp_Fname, EMP_Hiredate) values"
                "((select Region_ID from region where Region_Name = 'NW'),"
                "'Zebras', 'Steve', '1990/01/02'),"
                "((select Region_ID from region where Region_Name = 'NW'),"
                "'Burklow', 'Shane', '1990/01/02'),"
                "((select Region_ID from region where Region_Name = 'NW'),"
                "'Smith', 'Mary', '1990/02/02'),"
                "((select Region_ID from region where Region_Name = 'NW'),"
                "'Smith', 'Jose', '1990/02/02'),"
                "((select Region_ID from region where Region_Name = 'NW'),"
                "'Summers', 'Anna', '1990/03/02'),"
                "((select Region_ID from region where Region_Name = 'NW'),"
                "'Ellis', 'Maria', '1990/03/02'),"
                "((select Region_ID from region where Region_Name = 'NW'),"
                "'Epahnor', 'Victor', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'NW'),"
                "'Kilby', 'Surgena', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'NW'),"
                "'Bush', 'Emily', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'SW'),"
                "'Seaton', 'Amy', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'SW'),"
                "'Chandler', 'Joseph', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'SW'),"
                "'Bender', 'Larry', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'SW'),"
                "'Batts', 'Melissa', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'SW'),"
                "'Kattan', 'Chris', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'MN'),"
                "'Williams', 'Josh', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'MN'),"
                "'Yarbrough', 'Peter', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'MN'),"
                "'Pascoe', 'Jonathan', '1992/05/10'),"
                "((select Region_ID from region where Region_Name = 'MS'),"
                "'Underwood', 'Trish', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'MS'),"
                "'Robbins', 'Erin', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'MS'),"
                "'Newton', 'Christopher', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'MS'),"
                "'Duarte', 'Miriam', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'NE'),"
                "'Paine', 'Brad', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'NE'),"
                "'Craig', 'Brett', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'NE'),"
                "'Mudd', 'Roger', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'NE'),"
                "'Kenyon', 'Tiffany', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'SE'),"
                "'Rogers', 'Adam', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'SE'),"
                "'Bible', 'Hanah', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'SE'),"
                "'Cope', 'Leslie', '1993/04/03'),"
                "((select Region_ID from region where Region_Name = 'SE'),"
                "'Swell', 'Beth', '1993/04/03')")

            connection.commit()

            # Insert table empskill.
            cursor.execute("CREATE TABLE empskill("
                           "Emp_ID INT NOT NULL,"
                           "Skill_ID INT NOT NULL,"
                           "PRIMARY KEY (Emp_ID , Skill_ID),"
                           "FOREIGN KEY(Emp_ID)"
                           "REFERENCES employee (Emp_ID),"
                           "FOREIGN KEY (Skill_ID)"
                           "REFERENCES skill (Skill_ID))")

            connection.commit()

            # Insert data into empskill.
            cursor.execute("insert into empskill(Emp_ID, Skill_ID)"
                           "values"
                           "((select Emp_ID from employee where Emp_Fname in ('Amy')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Data Entry I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Josh')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Data Entry I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Trish')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Data Entry I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Amy')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Data Entry II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Josh')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Data Entry II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Brett')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Beth')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Erin')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Emily')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Steve')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Joseph')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Shane')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Erin')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Peter')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'DB Designer I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Mary')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'DB Designer I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Peter')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'DB Designer II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Jonathan')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'DB Designer II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Chris')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Cobol I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Victor')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Cobol I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Anna')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Cobol I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Maria')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Cobol I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Chris')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Cobol II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Victor')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Cobol II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Melissa')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Cobol II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Jose')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'C++ I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Adam')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'C++ I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Leslie')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'C++ I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Adam')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'C++ II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Hanah')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'C++ II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Steve')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'VB I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Maria')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'VB I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Steve')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'VB II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Christopher')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'VB II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Miriam')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'ColdFusion I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Emily')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'ColdFusion I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Emily')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'ColdFusion II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Christopher')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'ColdFusion II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Miriam')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'ASP I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Emily')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'ASP I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Miriam')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'ASP II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Christopher')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'ASP II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Jose')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Oracle DBA')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Jonathan')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Oracle DBA')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Peter')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'SQL Server DBA')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Jose')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'SQL Server DBA')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Emily')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Network Engineer I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Mary')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Network Engineer I')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Emily')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Network Engineer II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Mary')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Network Engineer II')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Emily')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Web Administrator')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Mary')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Web Administrator')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Christopher')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Web Administrator')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Surgena')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Technical Writer')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Larry')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Technical Writer')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Trish')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Technical Writer')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Brad')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Project Manager')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Roger')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Project Manager')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Tiffany')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Project Manager')),"
                           "((select Emp_ID from employee where Emp_Fname in ('Sean')),"
                           "(select Skill_ID from skill where Skill_Descrpt = 'Project Manager'))")

            connection.commit()

            # Create table project.
            cursor.execute("CREATE TABLE project("
                           "Proj_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                           "Cus_ID INT NOT NULL,"
                           "Emp_ID INT NOT NULL,"
                           "Proj_Date DATE NOT NULL,"
                           "Proj_Descrpt VARCHAR(255) NOT NULL,"
                           "Proj_EstDateSt DATE NOT NULL,"
                           "Proj_EstDateEnd DATE NOT NULL,"
                           "Proj_EstBudget FLOAT NOT NULL,"
                           "Proj_ActDateSt DATE,"
                           "Proj_ActDateEnd DATE,"
                           "Proj_ActCost FLOAT,"
                           "FOREIGN KEY (Cus_ID)"
                           "REFERENCES customer (Cus_ID),"
                           "FOREIGN KEY (Emp_ID)"
                           "REFERENCES employee (Emp_ID))")

            connection.commit()

            # Insert customer See Rocks.
            cursor.execute(
                "insert into customer(Cus_ID, Region_ID, Cus_Name, Cus_Phone)"
                "value"
                "(101, "
                "(select Region_ID from region where Region_Name = 'NW'), "
                "'See Rocks', "
                "'1-800-333-3333')")

            connection.commit()

            # Insert sample project.
            cursor.execute(
                "insert into project(Proj_ID, Cus_ID, Emp_ID, Proj_Date, Proj_Descrpt, Proj_EstDateSt, Proj_EstDateEnd, Proj_EstBudget, Proj_ActDateSt, Proj_ActDateEnd, Proj_ActCost)"
                "value"
                "(1,"
                "(select Cus_ID from customer where Cus_Name = 'See Rocks'),"
                "(select Emp_ID from employee where Emp_Lname = 'Connor'),"
                "'2014/02/12',"
                "'Sales Management System',"
                "'2014/03/01',"
                "'2014/07/01',"
                "'15500',"
                "'2014/03/01',"
                "'2014/07/01',"
                "'30000')")

            connection.commit()

            # Create table task.
            cursor.execute("CREATE TABLE task ("
                           "Task_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                           "Proj_ID INT NOT NULL,"
                           "Task_Info VARCHAR(255) NOT NULL,"
                           "Task_DateSt DATE,"
                           "Task_DateEnd DATE,"
                           "FOREIGN KEY (Proj_ID)"
                           "REFERENCES project (Proj_ID))")

            connection.commit()

            # Create table task_skills.
            cursor.execute("CREATE TABLE task_skills ("
                           "TS_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                           "Task_ID INT NOT NULL,"
                           "Skill_ID INT NOT NULL,"
                           "TS_Qty INT NOT NULL,"
                           "FOREIGN KEY(Task_ID)"
                           "REFERENCES task (Task_ID),"
                           "FOREIGN KEY (Skill_ID)"
                           "REFERENCES skill (Skill_ID))")

            connection.commit()

            # Insert data into task.
            cursor.execute(
                "insert into task(Proj_ID, Task_Info, Task_DateSt, Task_DateEnd) values"
                "((select Proj_ID from project where Proj_Descrpt = 'Sales Management System'), 'Initial Interview', '2014/03/01', '2014/03/06'),"
                "((select Proj_ID from project where Proj_Descrpt = 'Sales Management System'), 'Database Design', '2014/03/11', '2014/03/15'),"
                "((select Proj_ID from project where Proj_Descrpt = 'Sales Management System'), 'System Design', '2014/03/11', '2014/04/12'),"
                "((select Proj_ID from project where Proj_Descrpt = 'Sales Management System'), 'Database Implementation', '2014/03/18', '2014/03/22'),"
                "((select Proj_ID from project where Proj_Descrpt = 'Sales Management System'), 'System Coding & Testing', '2014/03/25', '2014/05/20'),"
                "((select Proj_ID from project where Proj_Descrpt = 'Sales Management System'), 'System Documentation', '2014/03/25', '2014/06/07'),"
                "((select Proj_ID from project where Proj_Descrpt = 'Sales Management System'), 'Final Evaluation', '2014/06/10', '2014/06/14'),"
                "((select Proj_ID from project where Proj_Descrpt = 'Sales Management System'), 'On-Site System Online and Data Loading', '2014/06/17', '2014/06/21'),"
                "((select Proj_ID from project where Proj_Descrpt = 'Sales Management System'), 'Sign-Off', '2014/07/01', '2014/07/01')")

            connection.commit()

            # Insert data into task_skills.
            cursor.execute(
                "insert into task_skills(Task_ID, Skill_ID, TS_Qty) values"
                "((select Task_ID from task where Task_Info = 'Initial Interview'), (select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst II'), 1),"
                "((select Task_ID from task where Task_Info = 'Initial Interview'), (select Skill_ID from skill where Skill_Descrpt = 'Project Manager'), 1),"
                "((select Task_ID from task where Task_Info = 'Initial Interview'), (select Skill_ID from skill where Skill_Descrpt = 'DB Designer I'), 1),"
                "((select Task_ID from task where Task_Info = 'Database Design'), (select Skill_ID from skill where Skill_Descrpt = 'DB Designer I'), 1),"
                "((select Task_ID from task where Task_Info = 'System Design'), (select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst II'), 2),"
                "((select Task_ID from task where Task_Info = 'System Design'), (select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst I'), 1),"
                "((select Task_ID from task where Task_Info = 'Database Implementation'), (select Skill_ID from skill where Skill_Descrpt = 'Oracle DBA'), 1),"
                "((select Task_ID from task where Task_Info = 'System Coding & Testing'), (select Skill_ID from skill where Skill_Descrpt = 'Cobol I'), 2),"
                "((select Task_ID from task where Task_Info = 'System Coding & Testing'), (select Skill_ID from skill where Skill_Descrpt = 'Cobol II'), 1),"
                "((select Task_ID from task where Task_Info = 'System Coding & Testing'), (select Skill_ID from skill where Skill_Descrpt = 'Oracle DBA'), 1),"
                "((select Task_ID from task where Task_Info = 'System Documentation'), (select Skill_ID from skill where Skill_Descrpt = 'Technical Writer'), 1),"
                "((select Task_ID from task where Task_Info = 'Final Evaluation'), (select Skill_ID from skill where Skill_Descrpt = 'Project Manager'), 1),"
                "((select Task_ID from task where Task_Info = 'Final Evaluation'), (select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst II'), 1),"
                "((select Task_ID from task where Task_Info = 'Final Evaluation'), (select Skill_ID from skill where Skill_Descrpt = 'DB Designer I'), 1),"
                "((select Task_ID from task where Task_Info = 'Final Evaluation'), (select Skill_ID from skill where Skill_Descrpt = 'Cobol II'), 1),"
                "((select Task_ID from task where Task_Info = 'On-Site System Online and Data Loading'), (select Skill_ID from skill where Skill_Descrpt = 'Project Manager'), 1),"
                "((select Task_ID from task where Task_Info = 'On-Site System Online and Data Loading'), (select Skill_ID from skill where Skill_Descrpt = 'Systems Analyst II'), 1),"
                "((select Task_ID from task where Task_Info = 'On-Site System Online and Data Loading'), (select Skill_ID from skill where Skill_Descrpt = 'DB Designer I'), 1),"
                "((select Task_ID from task where Task_Info = 'On-Site System Online and Data Loading'), (select Skill_ID from skill where Skill_Descrpt = 'Cobol II'), 1),"
                "((select Task_ID from task where Task_Info = 'Sign-Off'), (select Skill_ID from skill where Skill_Descrpt = 'Project Manager'), 1)")

            connection.commit()

            # Create table assign.
            cursor.execute("CREATE TABLE assign ("
                           "Asn_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                           "Emp_ID INT NOT NULL,"
                           "Asn_DateSt DATE,"
                           "Asn_DateEnd DATE,"
                           "TS_ID INT NOT NULL,"
                           "FOREIGN KEY (Emp_ID)"
                           "REFERENCES employee (Emp_ID),"
                           "FOREIGN KEY (TS_ID)"
                           "REFERENCES task_skills (TS_ID))")

            cursor.execute("alter table assign auto_increment=101")

            connection.commit()

            # Insert data into assign.
            cursor.execute(
                "insert into assign(Emp_ID, Asn_DateSt, Asn_DateEnd, TS_ID) values"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID = region.Region_ID and region.Region_Name = 'NW' and employee.Emp_ID = empskill.Emp_ID and skill.Skill_ID = empskill.Skill_ID and skill.Skill_Descrpt = 'Project Manager'),"
                "'2014/03/01',"
                "'2014/03/06',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID = skill.Skill_ID AND task_skills.Task_ID = task.Task_ID AND Task_Info = 'Initial Interview' AND skill.Skill_Descrpt = 'Project Manager')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID = region.Region_ID and region.Region_Name = 'NW' and employee.Emp_ID = empskill.Emp_ID and skill.Skill_ID = empskill.Skill_ID and skill.Skill_Descrpt = 'Systems Analyst II'),"
                "'2014/03/01',"
                "'2014/03/06',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID=skill.Skill_ID AND task_skills.Task_ID=task.Task_ID AND Task_Info='Initial Interview' AND skill.Skill_Descrpt='Systems Analyst II')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID=region.Region_ID and region.Region_Name='NW' and employee.Emp_ID=empskill.Emp_ID and skill.Skill_ID=empskill.Skill_ID and skill.Skill_Descrpt='DB Designer I'),"
                "'2014/03/01',"
                "'2014/03/06',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID=skill.Skill_ID AND task_skills.Task_ID=task.Task_ID AND Task_Info='Initial Interview' AND skill.Skill_Descrpt='DB Designer I')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID=region.Region_ID and region.Region_Name='NW' and employee.Emp_ID=empskill.Emp_ID and skill.Skill_ID=empskill.Skill_ID and skill.Skill_Descrpt='DB Designer I'),"
                "'2014/03/11',"
                "'2014/03/14',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID=skill.Skill_ID AND task_skills.Task_ID=task.Task_ID AND Task_Info='Database Design' AND skill.Skill_Descrpt='DB Designer I')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID=region.Region_ID and region.Region_Name='NW' and employee.Emp_ID=empskill.Emp_ID and skill.Skill_ID=empskill.Skill_ID and skill.Skill_Descrpt='Systems Analyst II'),"
                "'2014/03/11',"
                "'',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID=skill.Skill_ID AND task_skills.Task_ID=task.Task_ID AND Task_Info='System Design' AND skill.Skill_Descrpt='Systems Analyst II')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID=region.Region_ID and region.Region_Name='NW' and employee.Emp_ID=empskill.Emp_ID and skill.Skill_ID=empskill.Skill_ID and skill.Skill_Descrpt='Systems Analyst I' and employee.Emp_Lname='Bush'),"
                "'2014/03/11',"
                "'',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID=skill.Skill_ID AND task_skills.Task_ID=task.Task_ID AND Task_Info='System Design' AND skill.Skill_Descrpt='Systems Analyst I')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID=region.Region_ID and region.Region_Name='NW' and employee.Emp_ID=empskill.Emp_ID and skill.Skill_ID=empskill.Skill_ID and skill.Skill_Descrpt='Systems Analyst I' and employee.Emp_Lname='Zebras'),"
                "'2014/03/11',"
                "'',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID=skill.Skill_ID AND task_skills.Task_ID=task.Task_ID AND Task_Info='System Design' AND skill.Skill_Descrpt='Systems Analyst I')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID=region.Region_ID and region.Region_Name='NW' and employee.Emp_ID=empskill.Emp_ID and skill.Skill_ID=empskill.Skill_ID and skill.Skill_Descrpt='Oracle DBA'),"
                "'2014/03/15',"
                "'2014/03/19',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID=skill.Skill_ID AND task_skills.Task_ID=task.Task_ID AND Task_Info='Database Implementation' AND skill.Skill_Descrpt='Oracle DBA')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID = region.Region_ID and region.Region_Name = 'NW' and employee.Emp_ID = empskill.Emp_ID and skill.Skill_ID = empskill.Skill_ID and skill.Skill_Descrpt = 'Cobol I' and employee.Emp_Lname = 'Summers'),"
                "'2014/03/21',"
                "'',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID = skill.Skill_ID AND task_skills.Task_ID = task.Task_ID AND Task_Info = 'System Coding & Testing' AND skill.Skill_Descrpt = 'Cobol I')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID = region.Region_ID and region.Region_Name = 'NW' and employee.Emp_ID = empskill.Emp_ID and skill.Skill_ID = empskill.Skill_ID and skill.Skill_Descrpt = 'Cobol I' and employee.Emp_Lname = 'Ellis'),"
                "'2014/03/21',"
                "'',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID=skill.Skill_ID AND task_skills.Task_ID=task.Task_ID AND Task_Info='System Coding & Testing' AND skill.Skill_Descrpt='Cobol I')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID=region.Region_ID and region.Region_Name='NW' and employee.Emp_ID=empskill.Emp_ID and skill.Skill_ID=empskill.Skill_ID and skill.Skill_Descrpt='Cobol II'),"
                "'2014/03/21',"
                "'',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID=skill.Skill_ID AND task_skills.Task_ID=task.Task_ID AND Task_Info='System Coding & Testing' AND skill.Skill_Descrpt='Cobol II')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID=region.Region_ID and region.Region_Name='NW' and employee.Emp_ID=empskill.Emp_ID and skill.Skill_ID=empskill.Skill_ID and skill.Skill_Descrpt='Oracle DBA'),"
                "'2014/03/21',"
                "'',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID=skill.Skill_ID AND task_skills.Task_ID=task.Task_ID AND Task_Info='System Coding & Testing' AND skill.Skill_Descrpt='Oracle DBA')),"
                "((select employee.EMP_ID from employee, region, skill, empskill where employee.Region_ID=region.Region_ID and region.Region_Name='NW' and employee.Emp_ID=empskill.Emp_ID and skill.Skill_ID=empskill.Skill_ID and skill.Skill_Descrpt='Technical Writer'),"
                "'2014/03/25',"
                "'',"
                "(SELECT TS_ID FROM task_skills, task, skill WHERE task_skills.Skill_ID = skill.Skill_ID AND task_skills.Task_ID = task.Task_ID AND Task_Info = 'System Documentation' AND skill.Skill_Descrpt = 'Technical Writer'))")

            connection.commit()

            # Create table bill.
            cursor.execute("CREATE TABLE bill ("
                           "Bill_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                           "Bill_Date DATE NOT NULL,"
                           "Proj_ID INT NOT NULL,"
                           "FOREIGN KEY(Proj_ID)"
                           "REFERENCES project (Proj_ID))")

            connection.commit()

            # Create table worklog.
            cursor.execute("CREATE TABLE worklog ("
                           "WL_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                           "Asn_ID INT NOT NULL,"
                           "WL_date DATE NOT NULL,"
                           "WL_Hours FLOAT,"
                           "Bill_ID INT,"
                           "FOREIGN KEY (Asn_ID)"
                           "REFERENCES assign (Asn_ID),"
                           "FOREIGN KEY (Bill_ID)"
                           "REFERENCES bill (Bill_ID))")

            connection.commit()

            # Insert data into bill.

            cursor.execute(
                "insert into bill(Bill_ID, Bill_Date, Proj_ID) values"
                "('201', '2014/03/15', '1')")

            connection.commit()

            cursor.execute(
                "insert into worklog(Asn_ID, WL_Date, WL_Hours, Bill_ID) values"
                "('102', '2014/03/01', '4', '201'),"
                "('101', '2014/03/01', '4', '201'),"
                "('103', '2014/03/01', '4', '201'),"
                "('102', '2014/03/08', '24', '201'),"
                "('101', '2014/03/08', '24', '201'),"
                "('103', '2014/03/08', '24', '201'),"
                "('105', '2014/03/15', '40', '201'),"
                "('106', '2014/03/15', '40', '201'),"
                "('108', '2014/03/15', '6', '201'),"
                "('104', '2014/03/15', '32', '201'),"
                "('107', '2014/03/15', '35', '201')")

            connection.commit()

            cursor.execute(
                "insert into worklog(Asn_ID, WL_Date, WL_Hours) values"
                "('105', '2014/03/22', '40'),"
                "('106', '2014/03/22', '40'),"
                "('110', '2014/03/22', '12'),"
                "('111', '2014/03/22', '12'),"
                "('108', '2014/03/22', '12'),"
                "('112', '2014/03/22', '12'),"
                "('109', '2014/03/22', '12'),"
                "('107', '2014/03/22', '35'),"
                "('105', '2014/03/29', '40'),"
                "('106', '2014/03/29', '40'),"
                "('110', '2014/03/29', '35'),"
                "('111', '2014/03/29', '35'),"
                "('113', '2014/03/29', '40'),"
                "('112', '2014/03/29', '35'),"
                "('109', '2014/03/29', '35'),"
                "('107', '2014/03/29', '35')")

            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("2nd connection is closed")


def begin_seeding():
    # Please input your connection info here.

    print("Your username: ")
    username = input('--> ')

    print("Your password")
    password = getpass.getpass()

    print("Host name to connect to: ")
    hostname = input('--> ')

    print("Name of database: ")
    database_name = input('--> ')

    return username, password, hostname, database_name


def begin_process():
    username_input, passwd_input, hostname_input, db_name_input = begin_seeding()

    database_connection(hostname_input, username_input,
                        passwd_input, db_name_input)
