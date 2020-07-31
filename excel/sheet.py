from openpyxl import load_workbook
filename = "invoice.xlsx"
workbook = load_workbook(filename)
sheet = workbook.active
#the prefilled data is to give you an idea of the user data needed, you should replace them with data gotten from a user
def user_invoice():
    invoicedate = ""
    duedate = ""
    #company details
    company_name = ""
    company_address=""
    company_city = ""
    company_country = ""
    #client details
    client_name = ""
    client_address = ""
    client_city = ""
    client_country = ""
    #invoice items
    items = [
         ]
    #definition of first row of invoice items
    first_item_row = 21
    #sub total  and sales tax defaults to none unless they is assigned a value
    sub_total = None
    sales_tax = None
    total = sub_total+sales_tax
    note = ""
    terms = ""
    #adding items to the excelsheet
    #company details
    sheet["C6"] = company_name
    sheet["C7"] = company_address
    sheet["C8"] = company_city
    sheet["C9"] = company_country
    #client_details
    sheet["C13"] = client_name
    sheet["C14"] = client_address
    sheet["C15"] = client_city
    sheet["C16"] = client_country
    sheet["E4"] = invoicedate
    sheet["E6"] = duedate
    sheet["F31"] = sub_total
    sheet["F32"] = sales_tax
    sheet["F33"] = total
    sheet["B36"] = note
    sheet["B38"] = terms
    columns = ["B","D","E","F"]
    rowitems = []
    count = 0
    #invoice items
    for item in items:
         for key in item:
             rowitems.append(item[key])
             while len(rowitems)>len(columns):
                 newcolumns=["B","D","E","F"]
                 columns.extend(newcolumns)
                 first_item_row+=1
             itemposition=columns[count]+str(first_item_row)
             sheet[itemposition]=item[key]
             count+=1
    workbook.save(filename="invoice.xlsx")
user_invoice()
