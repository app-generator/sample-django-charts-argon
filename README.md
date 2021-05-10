# Django Argon Charts 

Open-source Sample provided on top of **[Argon Dashboard Django](https://bit.ly/3si4e7q)** (free product). **Django Argon Charts** sample provides functional code that shows different metrics regarding a 12mo timeframe: total sales, total orders, best sale and best month (in sales value). Information is provided using charts, widgets and a paginated data table that allows editing/adding new sales. 

<br />

> App Features

- Manage orders and display the information visually using charts and widgets
- Table `Orders` store the information - properties:
    - ID, Product Name (mandatory), Price, Created Times, Updated Times.
- `Charts`: Line and Bar Charts:
    - `Line Chart` shows the sales for a 12mo timeframe
    - `Bar Chart` shows the sales for a 12mo timeframe
- `Widget 1`: Total Sales (in value)
- `Widget 2`: Peek Sale - transaction with Biggest Value
- `Widget 3`: Total Orders (sum up of all transactions)
- `Widget 4`: Best Month - selected by the number of orders

<br />

> Links

- [Django Argon Charts](https://django-argon-charts.appseed-srv1.com) - LIVE deployment
- [Django Graphs and Charts](https://www.creative-tim.com/blog/django-templates/django-graphs-charts-argon-dashboard/) - a comprehensive blog article
- [Argon Dashboard Django](https://bit.ly/3si4e7q) - the original starter

<br />

## Want more? Go PRO!

PRO versions include **Premium UI Kits**, updates and **Priority Support**

| [Django Argon PRO](https://bit.ly/3gEXOx5) | [Django Black PRO](https://bit.ly/37Q9mbp) | [Django Datta Able PRO](https://appseed.us/admin-dashboards/django-dashboard-dattaable-pro) |
| --- | --- | --- |
| [![Django Argon PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-argon-pro/master/media/django-dashboard-argon-pro-screen.png)](https://bit.ly/3gEXOx5) | [![Django Black PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-black-pro/master/media/django-dashboard-black-pro-screen.png)](https://bit.ly/37Q9mbp) | [![Django Datta PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-dattaable-pro/master/media/django-dashboard-dattaable-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-dattaable-pro)

<br />
<br />

![Django Argon Charts - Open-source Django Sample provided by AppSeed.](https://raw.githubusercontent.com/app-generator/django-argon-charts/master/media/django-argon-charts-mockup.png)

<br />

## How to use it

**Clone the sources**

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-argon-charts.git
$ cd django-argon-charts
```

<br />

**Prepare the environment** and install modules

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
```

<br />

**Create SQLite database** an tables

```bash
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

**Create the superuser**

```bash
$ python manage.py createsuperuser 
```

<br />

**Start the app**, access the `admin` section and import the [Sample File](https://github.com/app-generator/django-argon-charts/blob/master/media/sample_data/orders.csv) into the `orders` table. 

> Note: make sure your are connected with an `admin` account.   

<br />

![Django Argon Charts - how to import data using admin section.](https://raw.githubusercontent.com/app-generator/static/master/samples/django-argon-charts-import-data.gif)

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app logic and serve the static assets
   |    |-- settings.py                    # Django app bootstrapper
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |-- templates/                     # Templates used to render pages
   |         |
   |         |-- includes/                 # HTML chunks and components
   |         |-- layouts/                  # Master pages
   |         |-- accounts/                 # Authentication pages
   |         |
   |      index.html                       # The default page
   |       *.html                          # All other HTML pages
   |
   |-- authentication/                     # Handles auth routes (login and register)
   |    |-- urls.py                        # Define authentication routes  
   |    |-- forms.py                       # Define auth forms  
   |
   |-- app/                                # A simple app that serve HTML files
   |    |-- views.py                       # Serve HTML pages for authenticated users
   |    |-- urls.py                        # Define some super simple routes  
   |    |-- templates
   |         |-- dashboard.html            # The dashboard <-------- NEW 
   |
   |-- orders/                             # Handles and display ORDERS   <-------- NEW   
   |    |-- migrations/                    # Handles and display ORDERS   <-------- NEW
   |    |   |-- __init__.py
   |    |-- static/                        # order CSS files, Javascripts files and static images
   |    |   |-- orders_assets/
   |    |       | -- jquery/
   |    |       |-- js/
   |    |           |-- order_script.js
   |    |           |-- notify.js
   |    |-- templates/                     # Templates used to render order pages
   |    |   |-- orders/
   |    |-- __init__.py                    # Defines App init             <-------- NEW
   |    |-- admin.py                       # Defines App admin            <-------- NEW
   |    |-- apps.py                        # Defines App apps             <-------- NEW
   |    |-- forms.py                       # Defines App forms            <-------- NEW
   |    |-- models.py                      # Defines App models           <-------- NEW
   |    |-- signals.py                     # Defines App signals          <-------- NEW
   |    |-- tests.py                       # Defines App tests            <-------- NEW
   |    |-- urls.py                        # Defines App routes           <-------- NEW
   |    |-- views.py                       # Defines App views            <-------- NEW
   |
   |-- requirements.txt                    # Development modules - SQLite storage
   |-- .env                                # Inject Configuration via Environment
   |-- manage.py                           # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />

## Charts Feature

This section describes the coding process for this feature that allows authenticated users to update their orders and sales.

### `Orders` Table

This table will save the information shown in the charts on the main dashboard - Fields:

- ID: primary key
- Product Name: string
- Product Price: int
- Created Times: create transaction datetime
- Updated Times: update transaction datetime

<br />

### `Orders` Application

The application that manages and implements all features:

- Allow users to save and edit a new order
    - Via a popup window/separate window   
- Populate the information on the main dashboard as presented below: 
    - Widget 1: Total Sales (in value)
    - Widget 2: Peek Sale - transaction with Biggest Value
    - Widget 3: Total Orders (sum up of all transactions)
    - Widget 4: Best Month - selected by the number of orders
    - Line Chart shows the sales for a 12mo timeframe
    - Bar Chart shows the sales for a 12mo timeframe

<br />

### Additional help

This section provides more information (especially for beginners) to understand and use the project much faster.

**How to create a new application in Django**

Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

To create your app, make sure you’re in the same directory as `manage.py` and type this command:

```bash
$ python manage.py startapp orders
```

That’ll create a directory `orders`, which is laid out like this:

```bash
|-- orders/
    |-- migrations/
        |-- __init__.py
    |-- __init__.py
    |-- admin.py
    |-- apps.py
    |-- models.py
    |-- tests.py
    |-- views.py
```

Now, open up `core/settings.py`. It’s a normal Python module with module-level variables representing Django settings.

Note the `INSTALLED_APPS` setting at the top of the file. That holds the names of all Django applications that are activated in this Django instance.

By default, `INSTALLED_APPS` contains the following apps, all of which come with Django:

- **django.contrib.admin:** The admin site. You’ll use it shortly.
- **django.contrib.auth:** An authentication system.
- **django.contrib.contenttypes:** A framework for content types.
- **django.contrib.sessions:** A session framework.
- **django.contrib.messages:** A messaging framework.
- **django.contrib.staticfiles:** A framework for managing static files.

> These applications are included by default as a convenience for the common case.

Now add your created app to the `INSTALLED_APPS`, so you can use it.

`core/settings.py`
```python
INSTALLED_APPS = [    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # ...
    'orders',

]
```

<br />

**How to define a new table**

First we need to open and edit the `orders/models.py` file. In our app, we’ll create a model named **Order**.

These concepts are represented by Python classes. Edit the `orders/models.py` file so it looks like this:

```python
from django.db import models

class Order(models.Model):
    product_name = models.CharField(max_length=40)
    price = models.IntegerField()
    created_time = models.DateTimeField(db_index=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
```

Here, each model is represented by a class that subclasses `django.db.models.Model`. Each model has a number of class variables, each of which represents a database field in the model.

Each field is represented by an instance of a **Field** class, e.g., **CharField** for character fields and **DateTimeField** for datetimes, and **IntegerField** for numbers. This tells Django what type of data each field holds.

Now Django knows to include the orders app. Let’s run another command:

```bash
$ python manage.py makemigrations orders
```

You should see something similar to the following:

```bash
Migrations for 'app':
  app/migrations/0001_initial.py
    - Create model Order
```

> By running `makemigrations`, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

Now, run migrate again to create those model tables in your database:

```bash
$ python manage.py migrate
```

> The `migrate` command takes all the migrations that haven’t been applied and run them against your database. Essentially, synchronizing the changes you made to your models with the schema in the database.

<br />

**How to register the table**  in the admin section

- `Easy Way`: It's very simple. first you must import admin from `django.contrib` and the table (`Order`) you want to set up an admin interface and then follow the codes:

```python
from django.contrib import admin
from orders.models import Order

admin.site.register(Order)
```

- `Custom way`: In this way you can customize your admin page more. So, first as before you must import admin from `django.contrib` and the table (`Order`) you want to set up an admin interface create a class for your admin page like this:

```python
from django.contrib import admin
from orders.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'created_time']
    search_fields = ['product_name']
```

In this case you have more option to use.

<br />

**How to add new data in the table**  in the admin section

This is so easy. Just go to the admin section and click on the desired app (`Orders`). In this section, you will see the `Add` (`ADD ORDER +`) option. After clicking on it, you can fill the form and click the `Save` button to store your information in the database.

<br />

**How to import bulk information** (using import/export module)

`django-import-export` is a Django application and library for importing and exporting data with included admin integration.

- `Installation and configuration`: django-import-export is available on the Python Package Index (PyPI), so it can be installed with standard Python tools like `pip` or `easy_install`:

```bash
$ pip install django-import-export
```

Now, you’re good to go, Just you need to add `import_export` to your INSTALLED_APPS:

```python
# settings.py
INSTALLED_APPS = (
    ...
    'import_export',
)
```

And let Django collect its static files:

```bash
$ python manage.py collectstatic
```

All prerequisites are set up. Now you can [configure more](https://django-import-export.readthedocs.io/en/latest/installation.html#settings) in your settings file.

- `Getting started`: For example purposes, we’ll use a simplified `orders` app as we made it.

To integrate `django-import-export` with our `Order` model, we will create a `ModelResource` class in `admin.py` that will describe how this resource can be `imported` or `exported`.

**Import Data:**
```python
# orders/admin.py

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportMixin
from orders.models import Order

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = ['id', 'product_name', 'price', 'created_time']  # the fields that we want to import

@admin.register(Order)
class OrderAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['product_name', 'price', 'created_time']
    search_fields = ['product_name']
    resource_class = OrderResource
```

There you are, Now you can import data from files. [Sample File](https://github.com/app-generator/django-argon-charts/blob/master/media/sample_data/orders.csv).

You can take a look at the [django-import-export](https://django-import-export.readthedocs.io/en/latest/index.html) document for more information.

<br />

### Links & Resources

- [Django](https://www.djangoproject.com/) - the official website
- More [Django Templates](https://bit.ly/3aStaNb) provided by Creative-Tim 
- More [Django Dashboards](http://appseed.us/admin-dashboards/django) provided by AppSeed

<br />

---
[Django Argon Charts](https://django-argon-charts.appseed-srv1.com) - Provided by Creative-Tim and AppSeed.
