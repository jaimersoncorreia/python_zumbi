def new_user(active=False, admin=False):
    print(active)
    print(admin)

config = {"active": False,
          "admin": True}

new_user(config.get('active'),config.get('admin'))

new_user(**config)
