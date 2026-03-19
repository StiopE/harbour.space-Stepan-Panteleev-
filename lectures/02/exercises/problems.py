import math

"""Lecture 02 exercises (classes) - implement from scratch.
Any 14 / 16 problems solved count as 100%
"""

"""
1) Create class User with:
    name,
    method say_hi() which prints "Hello, I am {name}"
"""

class User:
    def __init__(self, name):
        self.name = name
      
    def say_hi(self):
        print(f"Hello, I am {self.name}")


"""
2) BankAccount
Create class `BankAccount` with:
- `__init__(self, owner: str, balance: float = 0.0) -> None`
- `deposit(self, amount: float) -> None`
- `withdraw(self, amount: float) -> None`
Rules:
- Initial negative balance becomes `0.0`.
- Non-positive `deposit`/`withdraw` amounts are ignored.
- `withdraw` bigger than current balance is ignored.
"""
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance if balance >= 0 else 0.0
      
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount


"""
3) Team
Create class `Team` with:
- `__init__(self) -> None`
- `add(self, name: str) -> None`
- `__len__(self) -> int`
Rules:
- Members are stored in insertion order.
- Each instance has independent member storage.
"""

class Team:
    def __init__(self) -> None:
        self.members: list[str] = []
    def add(self, name: str) -> None:
        self.members.append(name)
    def __len__(self) -> int:
        return len(self.members)

""" (Advanced, optional)
5) QueueState
Create class `QueueState`:
- `__init__(self) -> None` (initialize empty `items` list)
Methods:
- `push(self, item: str) -> None`
- `pop(self) -> str | None`
Rules:
- FIFO behavior.
- `pop` returns `None` when empty.
"""


""" (Advanced, optional)
6) Wallet + custom errors
Create:
- `class PaymentError(Exception): ...`
- `class InsufficientFunds(PaymentError): ...`
- `class Wallet` with:
  - `__init__(self, balance: float = 0.0) -> None`
  - `top_up(self, amount: float) -> None`
  - `pay(self, amount: float) -> None`
Rules:
- Initial balance must be >= 0.
- `top_up` and `pay` require amount > 0.
- If `pay` exceeds balance, raise `InsufficientFunds`.
"""


"""
7) ShoppingCart
Create class `ShoppingCart` with:
- `__init__(self) -> None`
- `add_item(self, name: str, price: float, qty: int = 1) -> None`
- `total_items(self) -> int`
- `total_price(self) -> float`
Rules:
- `price < 0` or `qty <= 0` items are ignored.
- `repr` must include `ShoppingCart`.
"""
class ShoppingCart:
    def __init__(self) -> None:
        self.items = []
    def add_item(self, name: str, price: float, qty: int=1) -> None:
        if price >= 0 and qty > 0:
            self.items.append({
                'name': name,
                'price': price, 
                'qty': qty
            })
    def total_items(self) -> int:
        return sum(item['qty'] for item in self.items)
    def total_price(self) -> float:
        return sum(item['price'] * item['qty'] for item in self.items)
    def __repr__(self) -> str:
        return f"ShoppingCart(items={self.items})"    

"""
8) Classroom (class attribute)
Create class `Classroom` with class attribute:
- `school_name = "Harbour Space"`
Methods:
- `__init__(self, group_name: str) -> None`
- `add_student(self, name: str) -> None`
- `__len__(self) -> int`
- `set_school_name(self, new_name: str) -> None`
Rules:
- `set_school_name` must update shared class attribute for all instances.
"""

class Classroom:
    school_name = "Harbour Space"
    def __init__(self, group_name: str) -> None:
        self.students = []
    def add_student(self, name: str) -> None:
        self.students.append(name)
    def __len__(self) -> int:
        return len(self.students)
    def set_school_name(self, new_name: str) -> None:
        Classroom.school_name = new_name

"""
9) Rectangle
Create class `Rectangle` with:
- `__init__(self, width: float, height: float) -> None`
- `area(self) -> float`
- `perimeter(self) -> float`
Rules:
- Store positive dimensions using absolute values.
"""

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = abs(width)
        self.height = abs(height)
    def area(self) -> float:
        return self.width * self.height
    def perimeter(self) -> float:
        return (self.width + self.height) * 2
    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

"""
10) Playlist
Create class `Playlist` with:
- `__init__(self) -> None`
- `add(self, song: str) -> None`
- `__len__(self) -> int`
- `__iter__(self)`
- `__contains__(self, song: str) -> bool`
Rules:
- Preserve insertion order.
"""
class Playlist:
    def __init__(self) -> None:
        self.songlist = []
    def add(self, song: str) -> None:
        self.songlist.append(song)
    def __len__(self) -> int:
        return len(self.songlist)
    def __iter__(self):
        for song in self.songlist:
            yield song
    def __contains__(self, song: str) -> bool:
        if song in self.songlist:
            return True
        elif song not in self.songlist:
            return False

"""
11) Product
Create class `Product` with:
- `__init__(self, name: str, price: float) -> None`
- `get_price(self) -> float`
- `set_price(self, value: float) -> None`
- `apply_discount(self, percent: float) -> None`
Rules:
- Negative price is clamped to `0`.
- Discount percent is clamped to `[0, 100]`.
"""

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = max(price, 0)
    def get_price(self) -> float:
        return self.price
    def set_price(self, value: float) -> None:
        self.price = max(value, 0)
    def apply_discount(self, percent: float) -> None:
        percent = max(0, min(percent, 100))
        self.price *= (1 - percent / 100)

"""
12) Person + Student (inheritance)
Create:
- `class Person` with `__init__(name)` and `describe()`
- `class Student(Person)` with `__init__(name, group)` and overridden `describe()`
Required format:
- `Person(name=Ana)`
- `Student(name=Bo, group=G2)`
"""

class Person:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return f"Person(name={self.name})"
class Student(Person):
    def __init__(self, name: str, group: str) -> None:
        super().__init__(name)
        self.group = group
    def describe(self) -> str:
        return f"Student(name={self.name}, group={self.group})"
    


"""



"""
"""
13) Point2D (magic methods)
Create class `Point2D` with:
- `__init__(self, x: float, y: float) -> None`
- `distance_to(self, other: "Point2D") -> float`
- `__eq__(self, other: object) -> bool`
Rules:
- Euclidean distance.
- `repr` format: `Point2D(x, y)`.
"""
class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def distance_to(self, other: Point2D) -> float:
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y
    
    def __repr__(self) -> str:
        return f"Point2D({self.x}, {self.y})"
    

"""
14) Inventory
Create class `Inventory` with:
- `__init__(self) -> None`
- `add(self, name: str, qty: int = 1) -> None`
- `remove(self, name: str, qty: int = 1) -> None`
- `count(self, name: str) -> int`
- `__contains__(self, name: str) -> bool`
- `__len__(self) -> int`
Rules:
- Non-positive `qty` is ignored.
- Removing too much removes item completely (count becomes `0`).
"""

class Inventory:
    def __init__(self) -> None:
        self.this_inventory = {}
    def add(self, name: str, qty: int=1) -> None:
        if qty <= 0:
            return
        self.this_inventory[name] = self.this_inventory.get(name, 0) + qty
    def remove(self, name: str, qty: int=1) -> None:
        if qty <= 0 or name not in self.this_inventory:
            return
        self.this_inventory[name] -= qty
        if self.this_inventory[name] <= 0:
            del self.this_inventory[name]
    def count(self, name: str) -> int:
        return self.this_inventory.get(name, 0)
    def __contains__(self, name: str) -> bool:
        return name in self.this_inventory
    def __len__(self) -> int:
        return len(self.this_inventory)

"""
15) CourseCatalog
Create class `CourseCatalog` with:
- `__init__(self) -> None`
- `add_course(self, code: str, title: str) -> None`
- `get_title(self, code: str) -> str | None`
- `__iter__(self)` returning `(code, title)` sorted by code
- `__len__(self) -> int`
"""
class CourseCatalog:
    def __init__(self) -> None:
        self.catalog = {}
    def add_course(self, code: str, title: str) -> None:
        self.catalog[code] = title
    def get_title(self, code: str) -> str | None:
        return self.catalog.get(code)
    def __iter__(self):
        for key, value in sorted(self.catalog.items()):
            yield key, value
            
    def __len__(self) -> int:
        return len(self.catalog)

"""
16) DefaultDict (magic methods)
Create class `DefaultDict` with:
- `__init__(self, default_factory=None) -> None`
- `__getitem__(self, key)`
- `__setitem__(self, key, value) -> None`
- `__contains__(self, key) -> bool`
- `__len__(self) -> int`
Rules:
- On missing key:
  - if `default_factory` is `None`, return `None`.
  - otherwise create value using `default_factory()`, store, return.
- If `default_factory` is not callable, treat it as `None`.
"""

class DefaultDict:
    def __init__(self, default_factory=None) -> None:
        self.default_factory = default_factory if callable(default_factory) else None
        self.data = {}
    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        if self.default_factory is None:
            return None
        
        new_value = self.default_factory()
        self.data[key] = new_value
        return new_value
    def __setitem__(self, key, value) -> None:
        self.data[key] = value
    def __contains__(self, key) -> bool:
        return key in self.data
    def __len__(self) -> int:
        return len(self.data)
