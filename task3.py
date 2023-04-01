def delete(list_, index=None):
    if index == 0:
        li = list_[1:]
    elif index:
        li = list_[:index] + list_[index + 1:]
    else:
        li = list_[:-1]

    return li


print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]

# Реализовать функцию delete, принимающую список и индекс, по которому надо удалить элемент.
# По умолчанию удается последний элемент из списка.
