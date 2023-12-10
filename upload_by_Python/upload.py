import requests

# URL ของ API
api_url = 'http://localhost:5000/upload'

# ส่งไฟล์ไปยัง API
files = {'file_upload': open('picture.jpg', 'rb')}
headers = {'API-Key': 'abc123'}  # ใส่ API key ที่คุณใช้งาน
response = requests.post(api_url, files=files, headers=headers)

# ตรวจสอบสถานะการตอบกลับ
if response.status_code == 200:
    print('File uploaded successfully!')
else:
    print(f'Error: {response.status_code} - {response.text}')
