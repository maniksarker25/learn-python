class Phone:
    manufactured = "China"

    # int(constructor on other language)
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def semd_sms(self,phone,sms):
        text = f'Sending to : {phone} and sms is: {sms}'
        return text
    
my_phone = Phone("Steve jobs","Apple",100000)

print(my_phone.owner,my_phone.brand,my_phone.price)
her_phone = Phone("She","Iphone",432000)
print(her_phone.owner,her_phone.brand,her_phone.price)

