# Deterministic exam variant generator
Showcase of using cryptographically secure hashes as a way to generate uniquely distributed exam question numbers for a group of students.

## Usage
```bash
./raspred.py --file=students.txt --numbilets=20 --parameter=1337
```

#### --file
Specifies file with list of students in format:
```
Student Name 1
Student Name 2
...
```

#### --numbilets
Is the total number of exam variants available.

#### --parameter
Is a numeric parameter which uniquely identifies the generated distribution of exam variants, meaning a student with a specific name will always get the same variant number when the same parameter is used.

## Example
```bash
❯ ./raspred.py --file=students.txt --numbilets=20 --parameter=2   
Васильева Ева Тимуровна: 5
Васильева Ева Тимуровна: 5
Ильина Виктория Артёмовна: 12
Устинов Лев Миронович: 12
Чернышева Таисия Марковна: 13
Григорьев Матвей Максимович: 15
Королева Анна Владиславовна: 1
Платонов Иван Елисеевич: 10
Семенова Мария Артёмовна: 13
Кочергина Василиса Андреевна: 15
Муравьева Кира Кирилловна: 1
Казанцев Дамир Андреевич: 17
Покровская Вера Александровна: 4
Шилова Екатерина Павловна: 8
Орлова Полина Тимуровна: 6
Власова Варвара Львовна: 3
Грачева Ангелина Егоровна: 3
Горбунов Лев Евгеньевич: 15
Бондарев Кирилл Ярославович: 4
Федорова Софья Владиславовна: 5
Трошина Анастасия Всеволодовна: 13
```