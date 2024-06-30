favorite_languages = {
    'jen': 'python',
    'lin': 'c',
    'edward': 'rust',
    'phil': 'python'
}

message = favorite_languages.get('lam', '404')  #get()获取字典值，参数类似if和else
print(message)                                  #第二个参数不写默认为：None