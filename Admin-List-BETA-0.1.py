class Admin:
  admin = []

  def add_admin(username):
    admin.append(username)

  def del_admin():
    admin.clear()

  def is_admin(name):
    if name in admin:
      return True
    else:
      return False
