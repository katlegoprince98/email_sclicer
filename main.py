email_id = input("Enter your email id ").strip() # to remove spaces before and after

username = email_id[:email_id.index('@')]
domain = email_id[email_id.index('@') + 1:]

print(f'Your username is {username} and your domain name is {domain}')