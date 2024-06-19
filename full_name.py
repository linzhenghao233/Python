first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")
message = f"Hello, {full_name.title()}"
print(message)
print("\n\n\n")
print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript\n\n")
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip())
favorite_language = "python\t"
print(favorite_language.rstrip())
favorite_language = favorite_language.rstrip()  #永久删除结尾空格
favorite_language = "  Python  "
print(favorite_language.rstrip())
print(favorite_language.lstrip())

web_url = "https://test.com"
print(web_url.removeprefix("https://")) #注意要删除的内容是否写错
simple_url = web_url.removeprefix("https://")
print(web_url)
print(simple_url)