from flask import Flask, request, jsonify
import itertools
import hashlib
import string
import sys

app = Flask(__name__)
port = sys.argv[1]
answers = {}

def bruteforce_password(hashed_password, max_length, partition):
        chars = string.printable 
        # chars = string.ascii_lowercase # lowercase characters
        for password_length in range(0, max_length):
            # print (password_length)
            for guess in itertools.product(chars, repeat=password_length):
                guess = partition + ''.join(guess)
                Password = hashlib.md5(guess.encode()).hexdigest()
                answers[Password] = guess
                if Password == hashed_password:
                    return guess
        return None

@app.route('/passwordcracker', methods=['GET'])
def password_cracker():
    hashedPassword = request.json['password']                            
    maxLength = request.json['length']       
    partition = request.json['partition']            
    if hashedPassword in answers:
        return jsonify({'password' : answers[hashedPassword]})

    guess = bruteforce_password(hashedPassword, maxLength, partition)
    if guess:
        return jsonify({'password' : guess})
    else:
        return "Cannot crack it."
        
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=port, debug=True)
