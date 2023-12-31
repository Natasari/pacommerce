from tabulate import tabulate
from math import sqrt

class Membership:
    database_user = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }

    table_membership = {
        'Platinum' : ['Platinum', '15%', 'Voucher Makanan + Voucher Ojek Online + Voucher Liburan + Chasback Max 30%'],
        'Gold' : ['Gold', '10%', 'Voucher Makanan + Voucher Ojek Online'],
        'Silver' : ['Silver', '8%', 'Voucher Makanan']
    }

    table_requirement = {
        'Platinum' : ['Platinum', 8, 15],
        'Gold' : ['Gold', 6, 10],
        'Silver' : ['Silver', 5, 7]
    }

    def __init__(self, username):
        self.username = username
        self.database_user[username] = ""

    def check_all_membership(self):
        table = [value for membership, value in self.table_membership.items()]
        header = ['Membership', 'Diskon', 'Detail']
        print(tabulate(table, headers=header))

    def check_requirement(self):
        table = [value for membership, value in self.table_requirement.items()]
        header = ['Membership', 'Diskon', 'Detail']
        print(tabulate(table, headers=header))

    def predict_membership(self, username, monthly_expense, monthly_income):
        if username in self.database_user.keys():
            distance = {}

            for key, value in self.table_requirement.items():
                euclidean_distance = round(sqrt((monthly_expense - value[1])**2 + (monthly_income - value[2])**2),2)
                distance[key] = euclidean_distance

            print(f"Hasil perhitungan Euclidean Distance dari user Shandy adalah {distance}")

            for key, value in distance.items():
                if value == min(distance.values()):
                    self.database_user[username] = key
                    return key
        else:
            return 'Username tidak terdaftar'

    def show_membership(self, username):
        if isinstance(username, str):
            if username in self.database_user.keys():
                return self.database_user[username]
            else:
                return 'Username tidak terdaftar'
        else:
            return "Inputan bukan string"

    def calculate_bill(self, username, list_harga):
        try:
            if username in self.database_user.keys():
                membership_type = self.database_user[username]
                if membership_type != '':
                    diskon = int(self.table_membership[membership_type][1].split('%')[0]) / 100
                    total_bill = (1 - diskon) * sum(list_harga)
                    return total_bill
                else:
                    raise Exception("Membership kosong, silahkan lakukan predict!")
            else:
                raise Exception('Username tidak terdaftar')
        except Exception as e:
            print(e)

peni = Membership("peni")
peni.predict_membership("peni", 9,12)
print(peni.calculate_bill('peni', [150000, 200000, 400000]))

rani = Membership("rani")
rani.calculate_bill('ranip', [150000, 200000, 400000])

