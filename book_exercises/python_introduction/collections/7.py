info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# lst = info.split(':')
# new_info = '+'.join(lst)
# print(new_info)

new_info = info.replace(':', '+')
print(new_info)
