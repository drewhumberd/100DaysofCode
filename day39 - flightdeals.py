from day39.flight_search import FlightSearch
from day39.data_manager import DataManager
from day39.notification_manager import NotificationManager
import time

flight_search = FlightSearch()
data_manager = DataManager()
notificationmanager = NotificationManager()
sheet_data = data_manager.get_dest_data()
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_city_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.dest_data = sheet_data
    data_manager.update_sheet()

for dest in sheet_data:
    time.sleep(30)
    flight = flight_search.get_prices(dest["iataCode"])
    if flight is None:
        continue
    if flight.price < dest["lowestPrice"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        message = f"Low price alert! Only £{flight.price} to fly from \
{flight.origin_city}-{flight.origin_airport} to \
{flight.destination_city}-{flight.destination_airport}, \
from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over via {flight.via_city}."
        notificationmanager.send_emails(emails, message)
        # notificationmanager.send_message(
        #     message=message
        # )
