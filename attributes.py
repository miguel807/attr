"""
    1- Puedes crear un producto (ej: smart_tv),
    2- creas un grupo de atributos (ej: tv)
    3- le asignas atributos a ese grupo (ej: size, screen)
    4- le asigas valores a esos atributos (ej: xl,hd)
    5- le asignas ese grupo de atributos y los atributos con valores personalizados al producto (ej: tv (size=xxl,screen = 4k))
    6- muestra los productos
    """

class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.id = product_id
        self.name = name
        self.price = price
        self.attribute_groups = {}

    def add_attribute_group_with_custom_values(self, attribute_group, custom_values):
        """
        Adds an attribute group with custom values for each attribute in the group.
        """
        attributes_with_values = []
        for attr in attribute_group.attributes:
            value = custom_values.get(attr.name, attr.value)
            attributes_with_values.append(Attribute(attr.name, value, attribute_group.id))

        self.attribute_groups[attribute_group.id] = {
            "group_name": attribute_group.name,
            "attributes": attributes_with_values
        }

    def display_info(self):
        print(f"Product ID: {self.id}, Name: {self.name}, Price: ${self.price}")
        for group_id, group_data in self.attribute_groups.items():
            print(f"  Attribute Group: {group_data['group_name']}")
            for attr in group_data['attributes']:
                print(f"    {attr.name}: {attr.value}")


class Attribute:
    def __init__(self, name: str, value: str, attribute_group_id: int):
        self.name = name
        self.value = value
        self.attribute_group_id = attribute_group_id


class AttributeGroup:
    def __init__(self, group_id: int, name: str):
        self.id = group_id
        self.name = name
        self.attributes = []

    def add_attribute(self, attribute):
        self.attributes.append(attribute)


# Sample Data
products = []
attribute_groups = []


# Functions for menu options
def create_product():
    product_id = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    product = Product(product_id, name, price)
    products.append(product)
    print("Product added successfully!")


def create_attribute_group():
    group_id = int(input("Enter Attribute Group ID: "))
    name = input("Enter Attribute Group Name: ")
    group = AttributeGroup(group_id, name)
    attribute_groups.append(group)
    print("Attribute group created successfully!")


def add_attribute_to_group():
    if not attribute_groups:
        print("No attribute groups available. Please create an attribute group first.")
        return

    group_id = int(input("Enter Attribute Group ID: "))
    group = next((g for g in attribute_groups if g.id == group_id), None)
    if not group:
        print("Attribute group not found.")
        return

    name = input("Enter Attribute Name: ")
    value = input("Enter Default Attribute Value: ")
    attribute = Attribute(name, value, group_id)
    group.add_attribute(attribute)
    print("Attribute added to group successfully!")


def assign_group_to_product_with_custom_values():
    if not products:
        print("No products available. Please create a product first.")
        return
    if not attribute_groups:
        print("No attribute groups available. Please create an attribute group first.")
        return

    product_id = int(input("Enter Product ID to assign attribute group: "))
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        print("Product not found.")
        return

    group_id = int(input("Enter Attribute Group ID to assign to product with custom values: "))
    group = next((g for g in attribute_groups if g.id == group_id), None)
    if not group:
        print("Attribute group not found.")
        return

    custom_values = {}
    for attribute in group.attributes:
        value = input(f"Enter custom value for '{attribute.name}' (default: '{attribute.value}'): ")
        custom_values[attribute.name] = value if value else attribute.value

    product.add_attribute_group_with_custom_values(group, custom_values)
    print("Attribute group with custom values assigned to product successfully!")


def display_products():
    if not products:
        print("No products available.")
    for product in products:
        product.display_info()


# Menu
def menu():
    while True:
        print("\nMenu:")
        print("1. Create Product")
        print("2. Create Attribute Group")
        print("3. Add Attribute to Group")
        print("4. Assign Group to Product with Custom Values")
        print("5. Display Products")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            create_product()
        elif choice == "2":
            create_attribute_group()
        elif choice == "3":
            add_attribute_to_group()
        elif choice == "4":
            assign_group_to_product_with_custom_values()
        elif choice == "5":
            display_products()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")



menu()
