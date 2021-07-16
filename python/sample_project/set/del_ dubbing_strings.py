# example input:
# привет|еще строка|и снова строка|привет|и снова строка|да здравствуют чебупели


print("\n".join(list(sorted(set(input().split("|"))))))