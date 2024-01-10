import logging
from flask import Flask, render_template, request, redirect, url_for, flash

from payment_tappay import TAPPAY_GATEWAY

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

TAPPAY_CLIENT = TAPPAY_GATEWAY(partner_key='partner_6ID1DoDlaPrfHw6HBZsULfTYtDmWs0q0ZZGKMBpp4YICWBxgK97eK3RM', \
                               merchant_id='GlobalTesting_CTBC', \
                                sandbox=True)

@app.route('/')
def index():
    amount_to_front = 5
    return render_template('index.html', amount=amount_to_front)

@app.route('/api/pay', methods=['POST'])
def pay():
    prime = request.form['prime']
    amount = request.form['amount']
    method = request.form['method']
    print(f'prime: {prime}')
    print(f'amount: {amount}')
    print(f'method: {method}')

    details = "Test Pay"
    
    cardholder = {  # You may put '' empty string if you don't have the info. but it will be more secure if you have it.
        "phone_number": '',
        "name": '',
        "email": '',
        "member_id": '',    # Optional if you don't have member system
    }
    response = TAPPAY_CLIENT.pay_by_prime(prime, amount, details, cardholder, test_method=method)
    print('TapPay Backend API response: {response}'.format(response=response))
    return 'Payment Success! Redirect to /payment_confirmed', 200

if __name__ == '__main__':
    app.run(debug=True)