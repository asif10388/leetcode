def betterPasswords(string):
    if(len(string) >= 0 and len(string) <= 16):
        password = string.lower()
        return password.capitalize().replace("o", "()").replace("s", "$").replace("i", "!") + "."
    else:
        return "Invalid input"


print(betterPasswords("unsophisticated"))
