<<<<<<< HEAD
# example input:
# привет|еще строка|и снова строка|привет|и снова строка|да здравствуют чебупели


=======
# example input:
# привет|еще строка|и снова строка|привет|и снова строка|да здравствуют чебупели


>>>>>>> refs/remotes/origin/readme
print("\n".join(list(sorted(set(input().split("|"))))))