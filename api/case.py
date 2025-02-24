class MinhaClasse :
    def __enter__(self):
        print("Entrouuu")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saiuuu")
        

with MinhaClasse() as mc:
    print("Ta dentro da classe!")