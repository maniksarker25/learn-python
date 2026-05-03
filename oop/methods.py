def call():
    print("calling someone , i don't know")
    return "call done"

class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsum'
    features = ["camara",'speaker','hammer']
    #method
    def call(self):
        print("Calling one person")
    def send_sms(self,phone,sms):
        text = f'sending sms to : {phone} and message is : {sms}'
        return text

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(4323232,"I love you")
print(result)