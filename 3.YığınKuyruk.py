# %% Yığın

stack = []

# Yığına eleman ekleme (push)
stack.append(1)
stack.append(2)
stack.append(3)

# Yığından eleman çıkarma (pop)
print(stack.pop())
print(stack.pop())  
print(stack.pop())  

# %% Kuyruk

from collections import deque  #çift yonlu kuyruk (deque) yapısını kulllanmamız için kullanılır 

queue = deque()

# Kuyruğa eleman ekleme (enqueue)
queue.append("Ali")
queue.append("Ayşe")
queue.append("Mehmet")

# Kuyruktan eleman çıkarma (dequeue),
print(queue.popleft())  
print(queue.popleft())  
print(queue.popleft())  

# %% Sözlük

# Sözlük oluşturma
student_grades = {"Ali": 85, "Ayşe": 92, "Mehmet": 78}

# Sözlüğe yeni eleman ekleme
student_grades["Fatma"] = 88

# Elemanları listeleme
for student, grade in student_grades.items(): #items = Sözlükteki tüm elemanları listelemek ya da üzerinde işlem yapmak istediğinizde
    print(f"{student}: {grade}")

# Sözlükten eleman silme
del student_grades["Ali"]

