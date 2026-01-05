### 9-12

from privilege_admin import Privileges, Admin

admin_1 = Admin('shivanie', 'j', 'viku', 8, 'data science')
admin_1.privileges = Privileges(['can add post', 'can ban user', 'can delete any member'])
admin_1.privileges.show_privileges()