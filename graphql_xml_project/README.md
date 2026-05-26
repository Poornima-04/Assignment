# GraphQL XML Query API

## Overview

This project demonstrates how XML data can be exposed through a GraphQL API using Django and Graphene-Django.

A sample XML file was created based on the provided `OrderViewRS.xsd` schema. The XML contains order, passenger, flight, and pricing details.

The XML data is parsed using Python and exposed through GraphQL queries.

---

## Tech Stack

- Python
- Django
- Graphene-Django
- GraphQL
- XML
- xmltodict

---

## Project Structure

```text
graphql_xml_project/
│
├── airline_api/
│   ├── settings.py
│   ├── urls.py
│
├── orders/
│   ├── sample_order.xml
│   ├── xml_parser.py
│   ├── schema.py
│
├── queries.graphql
├── README.md
├── manage.py
```

---

## XML Sample

```xml
<OrderViewRS>

    <Order>

        <OrderID>ORD001</OrderID>

        <Passenger type="Adult">
            <FirstName>Poornima</FirstName>
            <LastName>P</LastName>
        </Passenger>

        <Flight>
            <FlightNumber>AI202</FlightNumber>
            <Departure>TRV</Departure>
            <Arrival>DEL</Arrival>
        </Flight>

        <Price currency="INR">
            <TotalAmount>8500</TotalAmount>
        </Price>

    </Order>

</OrderViewRS>
```

---

## How It Works

1. XML data is stored in `sample_order.xml`
2. `xml_parser.py` parses XML into Python dictionary
3. `schema.py` exposes XML data through GraphQL
4. GraphiQL interface is used to test queries

---

## Install Dependencies

```bash
pip install django graphene-django xmltodict django-graphiql-debug-toolbar
```

---

## Run Server

```bash
python manage.py runserver 8001
```

---

## Open GraphQL Playground

```text
http://127.0.0.1:8001/graphql/
```

---

## Example GraphQL Query

```graphql
query {
  order {

    orderId

    passenger {
      firstName
      lastName
      passengerType
    }

    flight {
      flightNumber
      departure
      arrival
    }

    price {
      totalAmount
      currency
    }

  }
}
```

---

## Example Response

```json
{
  "data": {
    "order": {
      "orderId": "ORD001",
      "passenger": {
        "firstName": "Poornima",
        "lastName": "P",
        "passengerType": "Adult"
      },
      "flight": {
        "flightNumber": "AI202",
        "departure": "TRV",
        "arrival": "DEL"
      },
      "price": {
        "totalAmount": "8500",
        "currency": "INR"
      }
    }
  }
}
```

---

## Dynamic Query Example

```graphql
query {
  order {
    orderId
  }
}
```

---

## Author

Poornima P
