You could write your app in app.py

The app will get input from index.html and send prime to backend, using payment_tappay.py module to communicate with tappay backend api to complete payment.

### TapPay uses two pare of elements for backend and frontend respectively
Backend:
1. PARTNER KEY for registered company
2. Merchant ID for registered store in compay

Frontend:
1. APP ID for inicializing your payment application
2. APP KEY for inicializing your payment application

# Setup
1. Clone the repo or download it
2. Run ```python app.py```or```python3 app.py``` in terminal or just run app.py
3. Open Browser and go to 127.0.0.1:5000 or you default port

# Step1 Type in infos
input
card: 4242 4242 4242 4242
date: date not due
ccv: 123

# Step2 Get Prime and send to backend
![Alt text](<readme_folder/截圖 2024-01-10 下午11.21.01.png>)
![Alt text](<readme_folder/截圖 2024-01-10 下午11.21.40.png>)

# Step3 Use payment_tappay.py
![Alt text](<readme_folder/截圖 2024-01-10 下午11.21.56.png>)
![Alt text](<readme_folder/截圖 2024-01-10 下午11.22.39.png>)
![Alt text](<readme_folder/截圖 2024-01-10 下午11.23.46.png>)