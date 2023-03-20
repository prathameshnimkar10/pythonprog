netstatus = int(input("Enter http status : "))
if netstatus == 200 or netstatus == 201:
    print('Success')

elif netstatus == 400:
    print('Bad request')

elif netstatus == 404:
    print('Not found')

elif netstatus == 500 or netstatus == 501:
    print('Server not found')

else:
    print('unknown')

match netstatus:
    case 200 | 201:
        print('Great success')