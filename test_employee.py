from employee import employee_info

def test_employee_info():
    result = employee_info("Rahul", 101, "IT", 30000)

    expected = ("Employee Name: Rahul\n"
                "Employee ID: 101\n"
                "Department: IT\n"
                "Salary: 30000")

    assert result == expected