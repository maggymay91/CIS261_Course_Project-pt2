#LaTangela Mcgee
#CIS261 
#Course Project Phase 2

from stat import FILE_ATTRIBUTE_COMPRESSED
from wsgiref import validate


def getDatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter end date in the following fromat MM/DD/YYYY: ")
    return fromDate, endDate

def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter amount of hours worked: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter Hourly Rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter Tax Rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        endDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]
        
        gPay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, endDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{gPay:,.2f}", f"{taxRate:.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        
        totalEmployees += 1
        totalHours += hours
        totalGrossPay =+ gPay
        totalTax += incometax
        totalNetPay += netpay
        
        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay
        
def printTotals(empTotals):
    print()
    print(f'Total Number Of Employees:  {empTotals["totEmp"]}')
    print(f'Total Hours Of Employee:   {empTotals["totHours"]}')
    print(f"Total Gross Pay Of Employees:   {empTotals['totGross']:,.2f}")
    print(f"Total Tax Of Employees:   {empTotals['totTax']:,.2f}")
    print(f"Total Net Pay Of Employees:  {empTotals['totNet']:,.2f}")
    
def WriteEmployeeInformation(employee):
    file = open("employeeinfo.txt", "a")
    
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
      
def GetFromDate():
     valid = False
     fromdate = ""

     while not valid:
    
        fromdate = input("Enter From Date (mm/dd/yyy): ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid Date Format: ")
        else:
            valid = True
     return fromdate

def ReadEmployeeInformation(fromdate):
    EmpDetailList = []
    
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    
    condition = True
    if fromdate.upper() == 'ALL':
        condition = False
        
    for employee in data:
    
        employee = [x.strip() for x in  employee.strip().split("|")]
        
        if not condition:
            EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]),float(employee[4]), float(employee[5])])
        else:
            if fromdate ==employee[0]:
                EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
     
    return EmpDetailList

if __name__=="__main__":
    
    empDetailList = []
    empTotals = {}
   
    while True:
        empName = getEmpName()
        if (empName.lower() == "end"):
            break
       
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
       
        print()
        
        EmpDetail = [fromDate, endDate, empName, hours, hourlyRate, taxRate]
        WriteEmployeeInformation(EmpDetail)
        
    print()
    print()
    fromDate = GetFromDate()
    
    EmpDetailList = ReadEmployeeInformation(fromDate)
    
    print()
    printInfo(EmpDetailList)
    print()
    printTotals(empTotals)
        
       
