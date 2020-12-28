from flask import Flask, request
import scrypt, os
import hashlib
import hmac
import json
import binascii



def hmac_sha256(msg, key):
    return hmac.new(key, msg, hashlib.sha256).digest()

app =Flask(__name__)

@app.route('/crypto1/sha256', methods=["POST"])
def sha256_endpoint():
    values = request.get_json()

    if not values:
        return "Missing body", 400

    required = ["msg"]

    if not all(k in values for k in required):
        return "Missing values", 400
	#* Implemented
	
    dataValues = values["msg"]
    data = dataValues.encode("utf8")
    
    print("Data: ", data)
    sha256hash = hashlib.sha256(data).digest()
    
    print("SHA256:    ", binascii.hexlify(sha256hash))
    
    responseHash = binascii.hexlify(sha256hash).decode("utf8")
    response = {"hash": responseHash}
    
    print(response)
    return json.dumps(response), 201

@app.route('/crypto1/sha512', methods=["POST"])
def sha512_endpoint():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["msg"]
    
    if not all(k in values for k in required):
        return "Missing values", 400
    
	#* Implemented
    dataValues = values["msg"]
    data = dataValues.encode("utf8")

    print("Data:", data)
    sha512hash = hashlib.sha512(data).digest()

    print("SHA512:    ", binascii.hexlify(sha512hash))

    responseHash = binascii.hexlify(sha512hash).decode("utf8"
    )
    response = {"hash": responseHash}

    return json.dumps(response), 201

@app.route('/crypto1/ripemd160', methods=["POST"])
def ripemd160_endpoint():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["msg"]
    if not all(k in values for k in required):
        return "Missing values", 400
    
    #* Implemented
    dataValues = values["msg"]
    data = dataValues.encode("utf8")

    print("Data:", data)
    ripemd160 = hashlib.new("ripemd160", data).digest()

    print("RIPEMD-160:    ", binascii.hexlify(ripemd160))

    responseHash = binascii.hexlify(ripemd160).decode("utf8")
    response = {"hash": responseHash}
    return json.dumps(response), 201

@app.route('/crypto1/hmac', methods=["POST"])
def hmac_endpoint():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["msg", "key"]
    if not all(k in values for k in required):
        return "Missing values", 400

    #* Implemented
    keyA = values["key"]
    key = keyA.encode("utf8")
    print(key)

    msgs = values["msg"]
    msg = msgs.encode("utf8")

    # res = binascii.hexlify(hmac_sha256(key, msg)).decode("utf8")
    response = {"hmac": binascii.hexlify(hmac_sha256(msg, key)).decode("utf8")}

    return json.dumps(response), 201

@app.route('/crypto1/scrypt', methods=["POST"])
def scrypt_endpoint():
    values = request.get_json()
    
    if not values:
        return "Missing body", 400

    required = ["passwd", "salt"]
    
    if not all(k in values for k in required):
        return "Missing values", 400
    
    #* Implemented
    password = values["passwd"]
    passwd = password.encode("utf8")

    print(passwd)
    salts = values["salt"]
    
    print(salts)
    salt = salts.encode('utf8')
    
    print("Salt: ", binascii.hexlify(salt))
    key = scrypt.hash(passwd, salt, 16384, 16, 1, 64)

    print("Derived key:", binascii.hexlify(key))

    responseKey = binascii.hexlify(key).decode("utf8")
    response = {"key": responseKey}

    return json.dumps(response), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

