import logging
import time
import requests
import json

logger = logging.getLogger("TapPay Gateway")

class TAPPAY_GATEWAY:

    def __init__(self, partner_key, merchant_id, sandbox=True ):
        self.sandbox = sandbox
        self.partner_key = partner_key
        self.merchant_id = merchant_id
        self.base_url = 'https://sandbox.tappaysdk.com' if sandbox else 'https://prod.tappaysdk.com'

    def pay_by_prime(self, prime, amount, details, cardholder, order_id=None, test_method=None, bind=None):
        if test_method:
            if test_method == 'Direct Pay':
                prime = 'test_3a2fb2b7e892b914a03c95dd4dd5dc7970c908df67a49527c0a648b2bc9'
            elif test_method == 'Apple Pay':
                prime = 'ap_test_utigjeyfutj5867uyjhuty47rythfjru485768tigjfheufhtu5i6ojk'
                amount = 12
            elif test_method == 'Google Pay':
                prime = 'gp_test_kjo6i5uthfuehfjgit867584urjfhtyr74ytuhjyu7685jtufyejgitu'    # 卡號交易
            elif test_method == 'Samsung Pay':
                prime = 'sp_test_utigjeyfutj5867uyjhuty47rythfjru485768tigjfheufhtu5i6ojk'
        
        url = f'{self.base_url}/tpc/payment/pay-by-prime'
        headers = {
            'content-type': 'application/json',
            'x-api-key': self.partner_key
        }
        payload = {
            'partner_key': self.partner_key,
            'prime': prime,
            'amount': int(amount),
            'merchant_id': self.merchant_id,
            'details': details,
            'cardholder': cardholder,
            'order_number': order_id,
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response_dict = response.json()
        logger.debug(f'Pay by prime: response: {response.status_code}.')

        if response_dict['status'] == 0:
            logger.debug('Pay by prime: Succuess')
            return True, response_dict
        else:
            logger.error(f'Pay by prime: Failed {response_dict}')
            return False, response_dict
        
    def get_trade_history(self, rec_trade_id):
        url = f'{self.base_url}/tpc/transaction/trade-history'
        headers = {
            'content-type': 'application/json',
            'x-api-key': self.partner_key
        }
        payload = {
            "partner_key": self.partner_key,
            "rec_trade_id": rec_trade_id
        }

        print(url, headers, payload)
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        logger.debug(f'Get trade history: {response}')
        print('\n',response)
        response_dict = response.json()
        print('\ndict' ,response_dict)
        if response.status_code == 200:
            return True, response_dict
        else:
            return False, response_dict

    def get_records(self, upper_amount_limit=None, lower_amount_limit=None, merchant_id=None, record_status=None, rec_trade_id=None, order_number=None, bank_transaction_id=None, currency=None):
        url = f'{self.base_url}/tpc/transaction/query'
        headers = {
            'content-type': 'application/json',
            'x-api-key': self.partner_key
        }
        payload = {
            "partner_key": self.partner_key,
            "filters":{
                "time":{
                    'start_time':int(time.time() * 1000)-1800000,   # Half hour ago
                    'end_time':int(time.time() * 1000)
                },
            }
        }
        amount = {}
        if merchant_id:
            payload["merchant_id"]= merchant_id
        if record_status:
            payload["record_status"]= record_status
        if rec_trade_id:
            payload["rec_trade_id"]= rec_trade_id
        if order_number:
            payload["order_number"]= order_number
        if bank_transaction_id:
            payload["bank_transaction_id"]= bank_transaction_id
        if currency:
            payload["currency"]= currency
        if upper_amount_limit:
            amount["upper_limit"]: upper_amount_limit
        if lower_amount_limit:
            amount["lower_limit"]: lower_amount_limit
        if amount:
            payload["filters"]["amount"] = amount

        print(url, headers, payload)
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        logger.debug(f'Get record: {response}')
        print('\n',response)
        response_dict = response.json()
        print('\ndict' ,response_dict)
        if response_dict['status'] == 0:
            print('success')
            logger.debug('Get record: Succuess')
            return True, response_dict
        elif response_dict['status'] == 2:
            logger.debug(f'Get record: This is all the records')
            return True, response_dict
        else:
            print('fail')
            logger.error(f'Get record: Failed {response_dict}')
            return False, response_dict
 

# Unfinished beneath



    def pay_by_token(self, card_key, card_token, amount, payment_details):
        response_data_dict = self.client.pay_by_token(card_key, card_token, amount, payment_details)

        logger.debug(f'Pay by token: {response_data_dict}')
        print(response_data_dict)

        if response_data_dict['status'] == '0':
            logger.debug('Pay by token: Succuess')
            return True, response_data_dict
        else:
            logger.error(f'Pay by token: Failed {response_data_dict}')
            return False, response_data_dict

    def bind_card(self, prime_token, cardholder):
        response_data_dict = self.client.bind_card(prime_token, cardholder)

        logger.debug(f'Bind card: {response_data_dict}')
        print(response_data_dict)
        return response_data_dict
    
    def remove_card(self, card_key, card_token):
        response_data_dict = self.client.remove_card(card_key, card_token)

        logger.debug(f'Remove card: {response_data_dict}')
        print(response_data_dict)
        return response_data_dict

# client = TAPPAY_GATEWAY('partner_6ID1DoDlaPrfHw6HBZsULfTYtDmWs0q0ZZGKMBpp4YICWBxgK97eK3RM', 'GlobalTesting_CTBC', True)

# response = client.pay_by_prime('prime', '50', 'test product', {'phone_number':'0987123456', 'member_id':'U371bb3871f4e24521d0cb806a56919f5', 'email':'555@gmail.co', 'name':''}, 'Apple Pay')
# print(response)

# response_record = client.get_trade_history('AP20231216zzbWS8')
# print(response_record)

# response_records = client.get_records()
# print(response_records)