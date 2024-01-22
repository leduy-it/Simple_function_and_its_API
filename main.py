from flask import Flask, request, jsonify
from mybignumber import MyBigNumber

app = Flask(__name__)
my_big_number = MyBigNumber()


@app.route('/sum', methods=['POST'])
def sum_numbers():
    try:
        data = request.get_json()
        str1 = data.get('str1', '')
        str2 = data.get('str2', '')

        result, history = my_big_number.sum(str1, str2)

        # Chuyển đổi chuỗi Unicode sang UTF-8
        decoded_history = history.encode('utf-8').decode('utf-8')

        response = {
            'result': result,
            'history': decoded_history
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
