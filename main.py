from datetime import datetime, timedelta

def calculate_delivery_dates(start_date_str):
    if not start_date_str:
        start_date_str = input("Please enter the R&D delivery date (dd-mm-yyyy): ")
    
    # Convert the start date string to a datetime object
    start_date = datetime.strptime(start_date_str, '%d-%m-%Y')

    # Calculate LAB delivery date (8 days after R&D, which is on the next Monday)
    lab_date = start_date + timedelta(days=6)

    # Calculate NPE delivery dates (3 and 4 days after LAB, which is Thursday and Friday)
    npe_date1 = lab_date + timedelta(days=3)
    npe_date2 = lab_date + timedelta(days=4)

    # Calculate PE delivery dates (9 and 10 days after NPE, which is Saturday and Sunday)
    pe_date1 = npe_date1 + timedelta(days=9)
    pe_date2 = npe_date1 + timedelta(days=10)

    # Print the delivery dates
    print(f"R&D delivery date: {start_date.strftime('%d %B %Y')}")
    print(f"LAB delivery date: {lab_date.strftime('%d %B %Y')}")
    print(f"NPE delivery date: {npe_date1.strftime('%d %B %Y')} / {npe_date2.strftime('%d %B %Y')}")
    print(f"PE delivery date: {pe_date1.strftime('%d %B %Y')} / {pe_date2.strftime('%d %B %Y')}")

# Example usage
start_date_str = ''  # Or any initial date in 'dd-mm-yyyy' format, e.g., '09-04-2024'
calculate_delivery_dates(start_date_str)
