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


# =========================================================
# EMPTY LISTS
# =========================================================

customers = []
subscriptions = []


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
    # APPEND ENTITIES TO LISTS
    # =====================================================

    customers.append(customer)

    subscriptions.append(subscription)


# =========================================================
# CREATE PANDAS DATAFRAMES
# =========================================================

customers_df = pd.DataFrame(customers)

subscriptions_df = pd.DataFrame(subscriptions)


# =========================================================
# PREVIEW DATA
# =========================================================

print(customers_df.head())

print(subscriptions_df.head())


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