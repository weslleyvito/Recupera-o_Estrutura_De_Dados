from pilhas_codificada import Pilhas_codificadas

# Exemplos
# s = input("3[a]2[bc]", retorna "aaabcbc".)
# s = input("3[a2[c]]", retorna "accaccacc".)
# s = input("2[abc]3[cd]ef", retorna "abcabccdcdcdef".)


q4 = Pilhas_codificadas()
s = input('Digite aqui:')
q4.decifrar_string(s)