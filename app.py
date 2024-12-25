from flask import Flask

#初始化一个flask实例
app = Flask(__name__)

#app.route装饰器映射到URL和执行的函数，这个设置将根URL映射到hello_world函数上
@app.route('/)
def hello_world():
  return "Hello World!"

if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0',port=5000)
