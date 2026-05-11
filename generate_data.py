# =========================================================
# IMPORTS
# =========================================================

import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta


# =========================================================
# FAKER INSTANCE
# =========================================================

fake = Faker()


# =========================================================
# BUSINESS CONFIGURATION LISTS
# =========================================================

segments = [
    "SMB",
    "Mid-Market",
    "Enterprise",
    "Strategic"
]

regions = [
    "North America",
    "EMEA",
    "APJ",
    "LATAM"
]

industries = [
    "Financial Services",
    "Retail",
    "Healthcare",
    "Technology",
    "Manufacturing",
    "AI",
    "Media"
]

growth_profiles = [
    "High Growth",
    "Stable",
    "Declining"
]

subscription_plans = [
    "Starter",
    "Professional",
    "Enterprise",
    "Strategic"
]
event_types = [
    "login",
    "dashboard_query",
    "pipeline_execution",
    "ai_model_run",
    "data_ingestion"
]

product_areas = [
    "Analytics",
    "Data Engineering",
    "Machine Learning",
    "AI Workloads",
    "Data Warehousing"
]

# =========================================================
# EMPTY LISTS
# =========================================================

customers = []
subscriptions = []
usage_events = []
compute_consumption = []

# =========================================================
# MAIN DATA GENERATION LOOP
# =========================================================

for i in range(1, 101):

    # =====================================================
    # CUSTOMER ENTITY
    # =====================================================

    customer = {

        "customer_id": f"CUST-{i:04d}",

        "customer_name": fake.company(),

        "segment": random.choice(segments),

        "region": random.choice(regions),

        "industry": random.choice(industries),

        "signup_date": fake.date_between(
            start_date="-3y",
            end_date="today"
        )
    }

    # =====================================================
    # SEGMENT-BASED BUSINESS LOGIC
    # =====================================================

    if customer["segment"] == "SMB":

        customer["employee_count"] = random.randint(20, 200)

        customer["annual_revenue_m"] = round(
            random.uniform(1, 20),
            1
        )

    elif customer["segment"] == "Mid-Market":

        customer["employee_count"] = random.randint(200, 2000)

        customer["annual_revenue_m"] = round(
            random.uniform(20, 200),
            1
        )

    elif customer["segment"] == "Enterprise":

        customer["employee_count"] = random.randint(2000, 20000)

        customer["annual_revenue_m"] = round(
            random.uniform(200, 2000),
            1
        )

    else:

        customer["employee_count"] = random.randint(20000, 100000)

        customer["annual_revenue_m"] = round(
            random.uniform(2000, 10000),
            1
        )

    # =====================================================
    # PLATFORM MATURITY
    # =====================================================

    customer["platform_maturity"] = random.choice([
        "Low",
        "Medium",
        "High"
    ])

    # =====================================================
    # GROWTH PROFILE
    # =====================================================

    customer["growth_profile"] = random.choice(
        growth_profiles
    )

    # =====================================================
    # SUBSCRIPTION BUSINESS LOGIC
    # =====================================================

    if customer["segment"] == "SMB":

        subscription_plan = "Starter"

        base_arr = random.randint(5000, 20000)

        included_compute_units = random.randint(100, 500)

    elif customer["segment"] == "Mid-Market":

        subscription_plan = "Professional"

        base_arr = random.randint(20000, 100000)

        included_compute_units = random.randint(500, 5000)

    elif customer["segment"] == "Enterprise":

        subscription_plan = "Enterprise"

        base_arr = random.randint(100000, 500000)

        included_compute_units = random.randint(5000, 20000)

    else:

        subscription_plan = "Strategic"

        base_arr = random.randint(500000, 5000000)

        included_compute_units = random.randint(20000, 100000)

    # =====================================================
    # SUBSCRIPTION ENTITY
    # =====================================================

    subscription = {

        "subscription_id": f"SUB-{i:04d}",

        "customer_id": customer["customer_id"],

        "subscription_plan": subscription_plan,

        "base_arr": base_arr,

        "included_compute_units": included_compute_units,

        "renewal_date": fake.date_between(
            start_date="today",
            end_date="+1y"
        )
    }

    # =====================================================
    # USAGE EVENTS GENERATION
    # =====================================================

    number_of_events = random.randint(20, 100)

    for event_index in range(number_of_events):

        usage_event = {

            "event_id": f"EVT-{i:04d}-{event_index:04d}",

            "customer_id": customer["customer_id"],

            "event_timestamp": fake.date_time_between(
                start_date="-90d",
                end_date="now"
            ),

            "event_type": random.choice(event_types),

            "product_area": random.choice(product_areas),

            "active_users": random.randint(1, 500)
        }

        usage_events.append(usage_event)

            # =====================================================
    # COMPUTE CONSUMPTION GENERATION
    # =====================================================

    number_of_consumption_records = random.randint(30, 90)

    for consumption_index in range(
        number_of_consumption_records
    ):

        # ================================================
        # SEGMENT-BASED CONSUMPTION LOGIC
        # ================================================

        if customer["segment"] == "SMB":

            compute_units_used = random.randint(50, 500)

            storage_gb_used = random.randint(100, 1000)

            query_count = random.randint(100, 1000)

        elif customer["segment"] == "Mid-Market":

            compute_units_used = random.randint(500, 5000)

            storage_gb_used = random.randint(1000, 10000)

            query_count = random.randint(1000, 10000)

        elif customer["segment"] == "Enterprise":

            compute_units_used = random.randint(5000, 20000)

            storage_gb_used = random.randint(10000, 50000)

            query_count = random.randint(10000, 100000)

        else:

            compute_units_used = random.randint(
                20000,
                100000
            )

            storage_gb_used = random.randint(
                50000,
                500000
            )

            query_count = random.randint(
                100000,
                1000000
            )

        # ================================================
        # GROWTH PROFILE IMPACT
        # ================================================

        if customer["growth_profile"] == "High Growth":

            compute_units_used = int(
                compute_units_used * 1.5
            )

        elif customer["growth_profile"] == "Declining":

            compute_units_used = int(
                compute_units_used * 0.7
            )

        # ================================================
        # COMPUTE CONSUMPTION ENTITY
        # ================================================

        consumption_record = {

            "consumption_id":
                f"CONS-{i:04d}-{consumption_index:04d}",

            "customer_id":
                customer["customer_id"],

            "consumption_date":
                fake.date_between(
                    start_date="-90d",
                    end_date="today"
                ),

            "compute_units_used":
                compute_units_used,

            "storage_gb_used":
                storage_gb_used,

            "query_count":
                query_count
        }

        compute_consumption.append(
            consumption_record
        )

    # =====================================================
    # APPEND ENTITIES TO LISTS
    # =====================================================

    customers.append(customer)

    subscriptions.append(subscription)


# =========================================================
# CREATE PANDAS DATAFRAMES
# =========================================================

customers_df = pd.DataFrame(customers)

subscriptions_df = pd.DataFrame(subscriptions)

usage_events_df = pd.DataFrame(usage_events)

compute_consumption_df = pd.DataFrame(
    compute_consumption
)

# =========================================================
# PREVIEW DATA
# =========================================================

print(customers_df.head())

print(subscriptions_df.head())

print(usage_events_df.head())

print(compute_consumption_df.head())

# =========================================================
# EXPORT CSV FILES
# =========================================================

customers_df.to_csv(
    "data/raw/customers.csv",
    index=False
)

subscriptions_df.to_csv(
    "data/raw/subscriptions.csv",
    index=False
)

usage_events_df.to_csv(
    "data/raw/usage_events.csv",
    index=False
)

compute_consumption_df.to_csv(
    "data/raw/compute_consumption.csv",
    index=False
)