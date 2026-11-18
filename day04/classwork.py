#davaleba 1

city = input("tbilisi")

result = city[:2] + city[-2:]

print(result)

city = input()

print(city[:2] + city[-2:])

#davaleba 2

word=("cup")
result=word[:1] + word[-1]

print(result)


#davaleba 3

name = input("dato")

print(name[::-1])

#davaleba 4

next = "gamarjoba me dato var 17 wlis"
result = next[::2] + next[--2::] +  next[::2] + next[--2::]

print(result)

next=input()

print(next[::2] + next[--2] + next[::2] + next[--2])
print(next[::2] + next[--2] + next[::2] + next[--2])









#მომხმარებელს შემოაქვს რაიმე ტექსტი. პროგრამამ უნდა ამოიღოს ტექსტის ყოველი მეორე სიმბოლო, დაწყებული პირველი სიმბოლოდან, და დაბეჭდოს მიღებული შედეგი.
