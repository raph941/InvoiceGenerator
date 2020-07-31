from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active
#the prefilled data is to give you an idea of the user data needed, you should replace them with data gotten from a user
def user_invoice():
    invoicedate = "jan 20,2020"
    duedate = "aug 20,2020"
    #company details
    company_name = "saf"
    company_address="50"
    company_city = "nairobi"
    company_country = "kenya"
    #client details
    client_name = "john"
    client_address = "500"
    client_city = "eldoret"
    client_country = "kenya"
    #invoice items
    items = [{"productDescription":"webisite","rate":"5%","quantity":"49","price":"200"},
         {"productDescription":"web","rate":"6%","quantity":"50","price":"205"}
         ]
    #definition of first row of invoice items
    first_item_row = 21
    #sub total  and sales tax defaults to none unless they is assigned a value
    sub_total = 400
    sales_tax = 500
    total = sub_total+sales_tax
    note = "Thank you"
    terms = "Please pay on time"
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
    #invoice items
    for item in items:
        for key in item:
            #increment column character
            for a in range(5):
                x='B'
                if (x=='C'):
                    continue
                val=chr(ord(x)+a)
                #column and row to place the item
                itemposition = val+str(first_item_row)
                C = "C"
                if (C in itemposition):
                    continue
                else:
                    sheet[itemposition] = item[key]
    workbook.save(filename="invoice.xlsx")
user_invoice()
