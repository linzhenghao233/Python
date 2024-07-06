#待验证用户列表
unconfirmed_users = ['alice', 'brian', 'candace']
#已验证用户列表
confirmed_users = []

#验证每个用户，验证后移入已验证用户列表
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#显示所有已验证用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())