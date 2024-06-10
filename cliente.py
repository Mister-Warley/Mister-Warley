import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8060/")

# Chamada da função subtrair
x, y = 22, 3
result = proxy.subtract(x, y)
print(f"{x} - {y} = {result}")