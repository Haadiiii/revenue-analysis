# 📗 Table of Contents

- [📖 About the Project](#about-project)

  - [🛠 Built With](#built-with)

    - [Tech Stack](#tech-stack)

  - [🚀 Live Demo](#live-demo)

- [💻 Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [DEPENDENCIES](#dependencies)
  - [Usage](#usage)
  - [Run tests](#run-tests)
  - [Deployment](#deployment)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [🙏 Acknowledgements](#acknowledgements)
- [❓ FAQ (OPTIONAL)](#faq)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 [Revenue-Analysis] <a name="about-project"></a>

**[Revenue-Analysis]** is a web application that allows users to analyze their revenue data based on different parameters such as date, sales, and prducts.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://www.sqlalchemy.org/">SQLAlchemy</a></li>
    <li><a href="https://www.encode.io/databases/">databases</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mysql.com/">MySQL</a></li>
  </ul>
</details>

#### Key Features <a name="key-features"></a>

- Track daily, weekly, monthly, and yearly revenues.
- Monitor low-stock inventory.

## Live Demo <a name="live-demo"></a>

- coming soon

## Screenshots <a name="screenshots"></a>

- ![/inventory/low-stock](<Screenshot from 2023-10-04 05-58-26.png>)

- ![/products](<Screenshot from 2023-10-04 05-58-59.png>)

- ![/sales](<Screenshot from 2023-10-04 05-59-12.png>)

## Getting Started <a name="getting-started"></a>

### Prerequisites <a name="prerequisites"></a>

To run this project, you need:

- Python 3.8+
- MySQL Database


In order to run this project you need:

1. Clone the repository:

   ```sh
   git clone https://github.com/haadiiii/revenue-analysis-api.git

   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project and add the following environment variables:

   ```sh
   DATABASE_URL=mysql://[username]:[password]@[host]:[port]/[database_name]
   ```

### Setup

To run this project, you need to:

1. Create a database in MySQL.

2. Create the tables in the database by running the following command:
   ```sh
   python models.py
   ```
3. Run the project by running the following command:
   ```sh
   uvicorn main:app --reload
   or
   python main.py
   ```
4. Open the following URL in your browser:

   ```sh
     http:// localhost:8000
   ```

<!-- brief
explanation of the endpoints provided by the API. -->

## API ENDPOINTS

### GET /revenue

Returns the total revenue for the current day.

#### Response

```json
{
  "DATE": 1000
}
```

### GET /revenue/weekly

Returns the total revenue for the current week.

#### Response

```json
{
  "DATE": 1000
}
```

### GET /revenue/monthly

Returns the total revenue for the current month.

#### Response

```json
{
  "DATE": 1000
}
```

### GET /revenue/yearly

Returns the total revenue for the current year.

#### Response

```json
{
  "DATE": 1000
}
```

### GET /products

Returns a list of all products.

#### Response

```json
[
  {
    "id": 1,
    "name": "Product 1",
    "price": 100,
    "inventory": 10
  },
  {
    "id": 2,
    "name": "Product 2",
    "price": 200,
    "inventory": 20
  }
]
```

### GET /products/{product_id}

Returns a product by id.

#### Response

```json
{
  "id": 1,
  "name": "Product 1",
  "price": 100,
  "inventory": 10
}
```

### POST /products

Creates a new product.

#### Request

```json
{
  "name": "Product 1",
  "price": 100,
  "inventory": 10
}
```

#### Response

```json
{
  "id": 1,
  "name": "Product 1",
  "price": 100,
  "inventory": 10
}
```

### PUT /products/{product_id}

Updates a product by id.

#### Request

```json
{
  "name": "Product 1",
  "price": 100,
  "inventory": 10
}
```

#### Response

```json
{
  "id": 1,
  "name": "Product 1",
  "price": 100,
  "inventory": 10
}
```

### GET /sales

Returns a list of all sales.

#### Response

```json
[
  {
    "id": 1,
    "product_id": 1,
    "quantity": 1,
    "date": "2021-09-01"
  },
  {
    "id": 2,
    "product_id": 2,
    "quantity": 2,
    "date": "2021-09-01"
  }
]
```

### GET /sales/{sale_id}

Returns a sale by id.

#### Response

```json
{
  "id": 1,
  "product_id": 1,
  "quantity": 1,
  "date": "2021-09-01"
}
```

### POST /sales

Creates a new sale.

#### Request

```json
{
  "product_id": 1,
  "quantity": 1,
  "date": "2021-09-01"
}
```

#### Response

```json
{
  "id": 1,
  "product_id": 1,
  "quantity": 1,
  "date": "2021-09-01"
}
```

### PUT /sales/{sale_id}

Updates a sale by id.

#### Request

```json
{
  "product_id": 1,
  "quantity": 1,
  "date": "2021-09-01"
}
```

#### Response

```json
{
  "id": 1,
  "product_id": 1,
  "quantity": 1,
  "date": "2021-09-01"
}
```

### GET /inventory/low-stock

Returns a list of all products with low stock (inventory < 10).

#### Response

```json
[
  {
    "id": 1,
    "name": "Product 1",
    "price": 100,
    "inventory": 5
  },
  {
    "id": 2,
    "name": "Product 2",
    "price": 200,
    "inventory": 6
  }
]
```

<!-- Database Documentation:
● Document the database schema, explaining the purpose of each table and its
relationships.-->

## Database Schema

- **products**

#### purpose

- Stores information about products.

```sql
  - id: int
  - name: string
  - price: int
  - inventory: int
```

- **sales**

#### purpose

- Stores information about sales.

```sql
  - id: int
  - product_id: int
  - quantity: int
  - date: date
```

### DEPENDENCIES

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [databases](https://www.encode.io/databases/)
- [MySQL](https://www.mysql.com/)
- [uvicorn](https://www.uvicorn.org/)
- [pydentic](https://pydantic-docs.helpmanual.io/)
- [Python MySQL Client](https://pypi.org/project/mysqlclient/)

### USAGE <a name="usage"></a>

```sh
python main.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Author <a name="authors"></a>

👤 **HaaDiiii**

- GitHub: [@Haadiiii](https://github.com/Haadiiii)
- Twitter: [@HaaDiii_99](https://twitter.com/HaaDiii_99)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/hamid-ali-01a872213/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

> Write a message to encourage readers to support your project

If you like this project and want to support it, please give a ⭐️!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FAQ (optional) -->

## ❓ FAQ (OPTIONAL) <a name="faq"></a>

> Add at least 2 questions new developers would ask when they decide to use your project.

- **[Question_1]**

  - [Answer_1]

- **[Question_2]**

  - [Answer_2]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
