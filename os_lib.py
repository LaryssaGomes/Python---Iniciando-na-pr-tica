import os
print(os.path.abspath('.')) # Caminho para chega no arquivo que eu estou
print(os.path.abspath('./test/folder/test_file.py'))

path_test_file = os.path.abspath('./test/folder/test_file.py') # Guardando caminho 
print(os.path.dirname(path_test_file))  # Pega o nome da ultima pasta
print(os.path.exists(path_test_file + '1'))# Verifica se existe
print(os.path.isfile(path_test_file)) # Verifica se e file
print(os.path.isdir(path_test_file)) # Verifica se e dir

print(__file__) # Nome da pasta
print(os.path.abspath(__file__)) # Caminho absoluto

print(os.path.dirname(os.path.abspath(__file__)))  # Pasta atual do arquivo
