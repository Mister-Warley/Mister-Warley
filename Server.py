class CalculadoraRemota:
    
def subtract(x, y):
    """Retorne a diferença entre x e y"""
    return x - y

server = SimpleXMLRPCServer(("localhost", 8060))
print("Listening on port 8060...")
server.register_function(subtract, "subtract")

server.serve_forever()