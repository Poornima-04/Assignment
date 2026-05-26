import graphene

from .xml_parser import parse_xml


# Passenger Type
class PassengerType(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    passenger_type = graphene.String()


# Flight Type
class FlightType(graphene.ObjectType):
    flight_number = graphene.String()
    departure = graphene.String()
    arrival = graphene.String()


# Price Type
class PriceType(graphene.ObjectType):
    total_amount = graphene.String()
    currency = graphene.String()


# Main Order Type
class OrderType(graphene.ObjectType):
    order_id = graphene.String()
    passenger = graphene.Field(PassengerType)
    flight = graphene.Field(FlightType)
    price = graphene.Field(PriceType)


# Query Class
class Query(graphene.ObjectType):

    order = graphene.Field(OrderType)

    def resolve_order(root, info):

        data = parse_xml()

        order_data = data["OrderViewRS"]["Order"]

        return {
            "order_id": order_data["OrderID"],

            "passenger": {
                "first_name": order_data["Passenger"]["FirstName"],
                "last_name": order_data["Passenger"]["LastName"],
                "passenger_type": order_data["Passenger"]["@type"]
            },

            "flight": {
                "flight_number": order_data["Flight"]["FlightNumber"],
                "departure": order_data["Flight"]["Departure"],
                "arrival": order_data["Flight"]["Arrival"]
            },

            "price": {
                "total_amount": order_data["Price"]["TotalAmount"],
                "currency": order_data["Price"]["@currency"]
            }
        }


schema = graphene.Schema(query=Query)