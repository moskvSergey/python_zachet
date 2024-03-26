# Inventory system

The application for accounting of goods in the store

## There are two classes in the program:

- InventoryApp
- Dialog

The first one is needed in order to run the main application in which you can add and delete entries
The second opens a dialog box where you can update records in the database

## Tech

The application uses a number of libraries to work properly:

- numpy
- PyQt5
- PyQt5-Qt5
- PyQt5-sip

## About methods

Now we will describe the main methods by which the application works

- create_connection (responsible for connecting to the database)
- create_table (responsible for creating the database)
- load_data (responsible for adding information to the database and displaying it on the widget)
- update_base (responsible for updating the database and displaying these updates on the widget)
- delete_product (responsible for removing a certain product from the database)
- add_product (responsible for adding the product to the database)
