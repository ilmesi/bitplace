import requests


class Payment():
    base_api_url = "https://blockchain.info/es/api"
    callback_base_url = "http://bitplace.herokuapp.com/callback" #ABSOLUTE URL!!! TODO

    def __init__(self, price, dev_address):
                self.price = price
                self.dev_address = dev_address
                self.state = 0

    def generate(self):
        api_res = "/receive"
        #generate payment
        callback_url = self.callback_base_url
        params = {'method': 'create', 'address': self.dev_address, 'callback': callback_url}
        r = requests.get(self.base_api_url + api_res, params=params)
        print r.json()
        self.input_address = r.json()['input_address']
        self.state = 1
        return self.input_address


