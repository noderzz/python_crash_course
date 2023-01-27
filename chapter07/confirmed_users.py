import time

unconfirmed_users = ['brian','alice','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop(0)

    print(f"Verifying user: {current_user.title()}.")
    time.sleep(1)
    confirmed_users.append(current_user)
    print("Success!\n")

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())