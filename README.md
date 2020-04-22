# API-Development-Guide

This is a step by step guide to develop APIs. Our final goal is to build working APIs for a Calorie Counting App with the following functionalities -

1. CRUD on Meal and User Resources.

2. RBAC on Meal and User Resources with the following roles -
    (a) A regular user would only be able to CRUD on his own Meal records.
    (b) A user manager would be able to CRUD only users
    (c) An admin would be able to CRUD all records and users.
    
3. Intergrate with third party APIs to get calorie count for food_items entered by the user.

4. Allow usesr to set a daily limit on their calorie count and keep a track of when user exceeds that limit.

5. Add filtering options during list operations.

6. Add Unit Tests for the above.
