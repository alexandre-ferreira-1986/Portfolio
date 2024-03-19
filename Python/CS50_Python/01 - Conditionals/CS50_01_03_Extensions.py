# User input
file = input('File name: ').lower()

# Images
if '.gif' in file:
    print('image/gif')
elif '.png' in file:
    print('image/png')
elif '.jpg' or '.jpeg' in file:
    print('image/jpeg')
#elif '.jpeg' in file:
#    print('image/jpeg')

# Applications
elif '.pdf' in file:
    print('application/pdf')
elif '.zip' in file:
    print('application/zip')

# Txt
elif '.txt' in file:
    print('text/plain')

# Others
else:
    print('application/octet-stream')

