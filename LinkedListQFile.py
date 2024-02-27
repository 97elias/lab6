class Node:
    """
    Representerar en nod i en länkad lista.
    """

    def __init__(self, value, next=None):
        """
        Initierar en ny nod med det angivna värdet och referens till nästa nod.

        Args:
            value: Värdet som ska lagras i noden.
            next: Referens till nästa nod i den länkade listan.
        """
        self.value = value
        self.next = next

    def __str__(self):
        """
        Returnerar en strängrepresentation av noden.

        Returns:
            En strängrepresentation av nodens värde.
        """
        return str(self.value)


class LinkedListQ:
    """
    Representerar en kö implementerad med en länkad lista.
    """

    def __init__(self, first=None, last=None):
        """
        Initierar en ny tom länkad lista-kö.

        Args:
            first: Referens till den första noden i den länkade listan.
            last: Referens till den sista noden i den länkade listan.
        """
        self.__first = first
        self.__last = last

    def __str__(self):
        """
        Returnerar en strängrepresentation av den länkade lista-kön.

        Returns:
            En strängrepresentation av den länkade lista-kön.
        """
        return str(self.__first) + str(self.__first.next) + str(self.__last)

    def isEmpty(self):
        """
        Kontrollerar om den länkade lista-kön är tom.

        Returns:
            True om kön är tom, False annars.
        """
        if self.__first == None:
            return True
        return False

    def enqueue(self, value):
        """
        Lägger till en ny nod med det angivna värdet i slutet av den länkade lista-kön.

        Args:
            value: Värdet som ska läggas till i kön.
        """
        x = Node(value)
        if self.isEmpty():
            self.__first = x
            self.__last = x
        else:
            self.__last.next = x
            self.__last = x

    def dequeue(self):
        """
        Tar bort och returnerar den första noden i den länkade lista-kön.

        Returns:
            Värdet på den borttagna noden.
        """
        x = self.__first
        self.__first = self.__first.next
        return x

    def remove(self, indata):
        """
        Tar bort den första förekomsten av en nod med det angivna värdet från den länkade lista-kön.

        Args:
            indata: Värdet som ska tas bort från kön.
        """
        prev_node = self.__first
        next_node = self.__first.next

        while next_node.next:
            if next_node.value == indata or prev_node.value == indata:
                break
            else:
                prev_node = prev_node.next
                next_node = next_node.next

        if prev_node.value == indata:  # Om den första noden ska tas bort
            self.__first = prev_node.next
            return print("1. Värdet har tagits bort")

        elif next_node.next == None and next_node.value == indata:  # Om den sista noden ska tas bort
            prev_node.next = next_node.next
            self.__last = prev_node

        elif next_node.value == indata:  # Om en nod i mitten ska tas bort
            prev_node.next = next_node.next
            return print("2. Värdet har tagits bort")

        else:
            return print("Värdet hittades inte i listan")

