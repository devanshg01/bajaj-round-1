from flask import Flask, jsonify, redirect, url_for, request
from collections import OrderedDict

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/oddEven',methods = ['POST'])
def postNumber():
   request_data = request.get_json()
   numbers = request_data["numbers"]
   odd_list = []
   even_list = []
   success = True
   for ele in numbers:
       try:
           number = int(ele)
           if ele%2 == 0:
               even_list.append(ele)
           else:
               odd_list.append(ele)
       except:
            success = False
   response = OrderedDict()
   response["is_success"] = success
   response["user_id"] = "Devansh_Garg_992001"
   if success:
       response["odd"] = odd_list
       response["even"] = even_list

   return jsonify(response)

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)
