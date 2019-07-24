from employee import Employee

emp_1 = Employee(1, "Sunny", "M.tech", 56000, "CS")
emp_2 = Employee(2, "Bunny", "M.tech", 46000, "IS")

emp_1.show_info()
emp_2.show_info()
emp_1.increment_salary(3000)
emp_1.show_info()
emp_2.show_info()
