class Contact:
   def __init__(self, name, phone_number, email):
      self.name = name
      self.phone_number = phone_number
      self.email = email
      self.favorite = False

def view_options():
   print('[1]. View contacts')
   print('[2]. Add contact')
   print('[3]. Edit contact')
   print('[4]. Mark contact as a favorite')
   print('[5]. View favorite contacts')
   print('[6]. Delete contact')
   print('[7]. Exit')
   
def view_contacts(contacts):
   if not contacts:
      print('No contacts')
   else:
      print('Contacts:')
      for index, contact in enumerate(contacts):
         print(f'[{index + 1}]. Name: {contact.name}')
         print(f'Phone number: {contact.phone_number}')
         print(f'Email: {contact.email}')
         print(f'Favorite: {contact.favorite}')
         print('-------------------')

def edit_contact(contacts):
   if not contacts:
      print('No contacts to edit.')
      return
   view_contacts(contacts)
   index = int(input('Enter the number of the contact to edit: ')) - 1
   if 0 <= index < len(contacts):
      name = input('Enter new name (leave blank to keep current): ')
      phone_number = input('Enter new phone number (leave blank to keep current): ')
      email = input('Enter new email (leave blank to keep current): ')
      if name:
         contacts[index].name = name
      if phone_number:
         contacts[index].phone_number = phone_number
      if email:
         contacts[index].email = email
      print('Contact updated!')
   else:
      print('Invalid contact number.')

def mark_favorite(contacts):
   if not contacts:
      print('No contacts to mark as favorite.')
      return
   view_contacts(contacts)
   index = int(input('Enter the number of the contact to mark as favorite: ')) - 1
   if 0 <= index < len(contacts):
      contacts[index].favorite = True
      print(f'{contacts[index].name} marked as favorite!')
   else:
      print('Invalid contact number.')

def view_favorites(contacts):
   favorites = [contact for contact in contacts if contact.favorite]
   if not favorites:
      print('No favorite contacts.')
   else:
      print('Favorite Contacts:')
      for contact in favorites:
         print(f'Name: {contact.name}')
         print(f'Phone number: {contact.phone_number}')
         print(f'Email: {contact.email}')
         print('-------------------')

def delete_contact(contacts):
   if not contacts:
      print('No contacts to delete.')
      return
   view_contacts(contacts)
   index = int(input('Enter the number of the contact to delete: ')) - 1
   if 0 <= index < len(contacts):
      deleted_contact = contacts.pop(index)
      print(f'{deleted_contact.name} deleted.')
   else:
      print('Invalid contact number.')

# Main loop
contacts = []
option = -1
while option != 7:
   view_options()
   choice = int(input('Enter an option: '))
   option = choice
   match choice:
      case 1:
         view_contacts(contacts)
            
      case 2:
         name = input('Enter name: ')
         phone_number = input('Enter phone number: ')
         email = input('Enter email: ')
         contact = Contact(name, phone_number, email)
         contacts.append(contact)
         print('Contact added!')
      
      case 3:
         edit_contact(contacts)

      case 4:
         mark_favorite(contacts)
      
      case 5:
         view_favorites(contacts)
      
      case 6:
         delete_contact(contacts)
      
      case 7:
         print('Goodbye!')

      case _:
         print('Invalid option')
