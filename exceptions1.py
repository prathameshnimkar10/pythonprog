def divide_by(a, b):
    return a/b

try:
    ans = divide_by(40, 0)
# except Exception:
#     print('Mathematical error!')
except Exception as e:
    print('Mathematical error!', e)
    print(e.__class__)