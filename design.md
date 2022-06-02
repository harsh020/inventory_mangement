## Requirements

- Basic CRUD Functionality. You should be able to:
    - Create inventory items
    - Edit Them
    - Delete Them
    - View a list of them

- ONLY ONE OF THE FOLLOWING (We will only evaluate the first feature chosen, so please only choose one)
    - When deleting, allow deletion comments and undeletion
    - Ability to create warehouses/locations and assign inventory to specific locations
    - Ability to create “shipments” and assign inventory to the shipment, and adjust inventory appropriately


## Model

- Item
- Category
- Warehouse
- Address


## Relationship

- Item (n is stored in 1) Warehouse 
- Item (1 is sold by 1) Category
- Warehouse (1 is located at 1) Address
