class Dog():
    """Проста модель собаки."""

    def __init__(self, name, age):
        """Ініціалізація атрибутів name і age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака сідає по команді."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Собака перекочується по команді."""
        print(self.name.title() + " rolled over!")
