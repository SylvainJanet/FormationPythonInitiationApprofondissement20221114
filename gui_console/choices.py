def chose_admin_or_user():
  while True:
    choice = input("Admin, user or quit ? (A/U/Q)")
    if choice.lower() == 'a':
      return "admin"
    if choice.lower() == 'u':
      return "user"
    if choice.lower() == 'q':
      return ""