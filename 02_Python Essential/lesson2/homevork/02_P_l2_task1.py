# Завдання 1

# Створіть клас Editor, який містить методи view_document та edit_document. 
# Нехай метод edit_document виводить на екран інформацію про те, що редагування 
# документів недоступне для безкоштовної версії. Створіть підклас ProEditor, 
# у якому цей метод буде перевизначено. Введіть ліцензійний ключ із клавіатури і, 
# якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor. 
# Викликайте методи перегляду та редагування документів.

class Editor:   
    def view_document(self):
        print('Watching the document...')
    
    def edit_document(self):
        print("Only Premiun users can use this function. If you have licenzion key, tipe it here: ")

class ProEditor(Editor):
    def edit_document(self):
        print("Editting the document...") 

CORRECT_KEY = 12
user_key = int(input('Enter licenze key: '))
editor = ProEditor() if user_key == CORRECT_KEY else Editor() 

editor.view_document()
editor.edit_document()
        
