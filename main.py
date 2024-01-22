from flask import Flask, request, jsonify
from mybignumber import MyBigNumber  # Assume MyBigNumber class is in mybignumber.py

app = Flask(__name__)
my_big_number = MyBigNumber()

@app.route('/sum', methods=['POST'])
def sum_numbers():
    try:
        data = request.get_json()
        stn1 = data.get('stn1', '')
        stn2 = data.get('stn2', '')

        result = my_big_number.sum(stn1, stn2)

        # Ghi nhận lịch sử phép toán
        history = []  # Dùng list để ghi nhận lịch sử
        index = 1
        for line in result.split('\n'):
            history.append(f"Bước {index}: {line}")
            index += 1

        response = {
            'result': result,
            'history': history
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
