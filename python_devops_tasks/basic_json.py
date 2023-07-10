import json

pepole_string = '''
{
"pepole":[
    {
      "name":"John Smith",
      "Phone":"878657699",
      "Email":["john_smith32@gmail.com","john_smith21@gmail.com"],
      "has_license": false
    },
    {
     "name":"sushant jadhav",
      "Phone":"9373730950",
      "Email":["sushant_416@gmail.com","svj_777@gmail.com"],
      "has_license": true 
    }
       ]
}
'''

data = json.loads(pepole_string)
print(data)
print(data['pepole'])
