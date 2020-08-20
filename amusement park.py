import math


class Node:
    def __init__(self, group_size, next_node=None):
        self.group_size = group_size
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_data(self):
        return self.group_size


class Queue:
    def __init__(self, limit=None):
        self.front_node = None
        self.back_node = None
        self.length = 0
        self.limit = limit

    def is_full(self):
        return self.length == self.limit if self.limit else False

    def is_empty(self):
        return self.length == 0

    def get_total(self):
        return self.length

    def peek(self):
        if self.is_empty():
            print("Nothing to see here, move along.")
        else:
            return self.front_node.get_data()

    def enqueue(self, group_size):
        if not self.is_full():
            new_node = Node(group_size)
            if self.is_empty():
                self.front_node = new_node
                self.back_node = new_node
            else:
                self.back_node.set_next_node(new_node)
                self.back_node = new_node
            self.length += group_size
        else:
            print("Eww go away, there's no more room!")

    def dequeue(self):
        if not self.is_empty():
            removed_node = self.front_node
            self.length -= self.front_node.get_data()
            if self.get_total() == 0:
                self.front_node = None
                self.back_node = None
            else:
                self.front_node = removed_node.get_next_node()
            # self.length -=
            return removed_node.get_data()
        else:
            print("Ya basic! Nothing here nerd!")


amusement_park = Queue()
amusement_park.enqueue(5)
amusement_park.enqueue(4)
amusement_park.enqueue(1)
amusement_park.enqueue(10)
# print(amusement_park.get_total())
# print(amusement_park.peek())
# print(amusement_park.dequeue())
# print(amusement_park.peek())

option = 0
options = ["1","2","3"]
print("#" * 50)
print("Welcome to our amazing amusement park!!")
print("#" * 50)
# print(amusement_park.get_total())

while option != 3:
    waiting_time = amusement_park.get_total() * 6

    if waiting_time >= 60:
        print("\nwaiting time is: " + str(waiting_time // 60) + " hours and " + str(waiting_time % 60) + " minutes")
    else:
        print("\nwaiting time is:" + str(amusement_park.get_total() * 6) + " minutes")

    print("-" * 50)
    option = input("enter the number of the option:\n1- add new groups\n2- sign in the next group\n3- exit\nyour option >> ")

    if option.isdigit():
        if int(option) == 1:
            size = int(input("Enter the number of people >> "))
            if size == 0:
                break
            elif size > 12:
                groups = math.ceil(size / 12)
                print("you will be splitted into " + str(groups) + " groups")
                for i in range(groups):
                    if i + 1 == groups:
                        amusement_park.enqueue(size - ((groups - 1) * 12))
                    else:
                        amusement_park.enqueue(12)
                print("\n" + str(groups) + " groups have been added!")
            else:
                amusement_park.enqueue(size)
                print("\nA group has been added!")
        elif int(option) == 2:
            amusement_park.dequeue()
        elif int(option) == 3:
            break
        else:
            print("Invalid entry")

    elif not option.isdigit():
        print("Invalid entry")

    print("^" * 50)

# print(amusement_park.get_total())
