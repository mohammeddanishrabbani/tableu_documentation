# Product Adoption Scorecard Dashboard Documentation

## 1. Dashboard Overview

This dashboard provides a comprehensive overview of product adoption across various customer segments, allowing us to understand how customers are using our product and identify areas for improvement. It answers key business questions such as:

* What is the overall product adoption rate?
* How does product adoption vary by plan type and customer size?
* What is the customer login rate and how does it trend over time?
* How are customers utilizing integrations and which vendors are most popular?
* What is the completion rate for playbooks and how is it changing?
* How effectively are customers using monitors and what is their status?
* How many policies are published by customers and how does this relate to their number of users?

**Target Audience:** This dashboard is designed for business users, analysts, and stakeholders interested in understanding product adoption trends, identifying opportunities for growth, and measuring the success of customer engagement initiatives.

## 2. Data Sources

The dashboard pulls data from the following Excel spreadsheet: "Q4 2021 Biz Ops Case Study - Sent".  This data is extracted into a Tableau Hyper file named "Product_adoption_scorecard.hyper".  The following tables/sheets are used:

* **Customer List:** Contains information about each customer.
    * **CUSTOMER_ID:** Unique identifier for each customer.
    * **NUMBER_OF_USERS:** Number of users within the customer's organization.
    * **CREATED_AT:** Date when the customer account was created.
    * **PLAN_TYPE:** The customer's subscription plan (e.g., "Growth Core", "Launch Plus").

* **Integrations:** Tracks customer integrations with third-party vendors.
    * **CUSTOMER_ID:** Unique identifier for each customer.
    * **VENDOR_NAME:** Name of the integrated vendor (e.g., "AWS", "Gusto").
    * **CATEGORY:** Category of the integration (e.g., "payroll", "business_suites").
    * **STATUS:** Status of the integration (e.g., "success", "pending", "error").

* **Logins:** Records customer login activity.
    * **CUSTOMER_ID:** Unique identifier for each customer.
    * **LOGIN_TIME:** Timestamp of the login event.

* **Monitor Status Changes:** Tracks changes in the status of monitors.
    * **CUSTOMER_ID:** Unique identifier for each customer.
    * **CREATED_AT:** Timestamp of the status change.
    * **STATUS:** Status of the monitor (e.g., "healthy", "triggered").
    * **MONITOR_ID:** Unique identifier for each monitor.
    * **ORGANIZATION_MONITOR_ID:**  Unique identifier for monitors within an organization.
    * **CHANGE:**  Type of status change.

* **Monitors:** Contains information about monitors.
    * **CUSTOMER_ID:** Unique identifier for each customer.
    * **MONITOR_ID:** Unique identifier for each monitor.
    * **MONITOR_CATEGORY:** Category of the monitor.
    * **ORGANIZATION_MONITOR_ID:** Unique identifier for monitors within an organization.
    * **STATUS:** Status of the monitor.
    * **MONITOR_TYPE:** Type of monitor.


* **Playbooks:** Tracks customer completion of playbooks.
    * **CUSTOMER_ID:** Unique identifier for each customer.
    * **COMPLETED_ON:** Date when the playbook was completed.
    * **TOTAL_COMPLETED:** Total number of completed tasks in the playbook.
    * **TOTAL_SUBTASKS:** Total number of subtasks in the playbook.
    * **COMPLETION_PERCENTAGE:** Percentage of completed tasks in the playbook.

* **Policies:** Records customer published policies.
    * **CUSTOMER_ID:** Unique identifier for each customer.
    * **CATEGORY:** Category of the policy.
    * **CREATED_AT:** Date when the policy was created.

* **Training:** Tracks customer employee training.
    * **CUSTOMER_ID:** Unique identifier for each customer.
    * **EMPLOYEES_TRAINED:** Number of employees trained.


## 3. Key Metrics & Definitions

* **Training Adoption Rate:** Percentage of users within a customer's organization who have completed training.
    * Calculation: `EMPLOYEES_TRAINED / NUMBER_OF_USERS`

* **Login Rate Per Customer:** Average number of logins per user for each customer.
    * Calculation: `COUNT(LOGIN_TIME) / SUM(NUMBER_OF_USERS)`

* **Playbook Completion Rate:**  The rate of change in playbook completion percentage over time.
    * Calculation: `(MAX(COMPLETION_PERCENTAGE) - MIN(COMPLETION_PERCENTAGE)) / DATEDIFF('day', MIN(COMPLETED_ON), MAX(COMPLETED_ON))`

* **Days Since Previous Date (Monitor Status Changes):** Calculates the number of days between consecutive monitor status changes.
    * Calculation: `DATEDIFF('day', LOOKUP(MIN([CREATED_AT (Monitor Status Changes)]),-1), MIN([CREATED_AT (Monitor Status Changes)]))`


## 4. Dashboard Structure

The dashboard consists of the following worksheets arranged across several dashboards and a storyboard:

**Story Board:** Product Adoption Scorecard

* Navigates to various dashboards based on specific areas of product adoption.

**Dashboards:**

* **User Training Score Card:** Focuses on training adoption rates.
    * **Total Customers, Total Users, Total Trained Users, Pricing Tier with Highest Users:**  Summary metrics displayed as text.
    * **Count of Customers by Plan Type:** Bar chart showing the distribution of customers across different plan types, colored by the number of users.
    * **Product Adoption Rate by Trained Employee Count:** Scatter plot showing the relationship between the number of users and the training adoption rate, colored by the number of employees trained.
    * **Average Training Adoption Rate by Plan Type:** Bar chart displaying the average training adoption rate for each plan type.

* **User Login Score Card:**  Analyzes user login behavior.
    * **User Logins by Pricing Tier:** Bubble chart showing the relationship between the number of users and the number of logins, colored by plan type.
    * **Average Logins by Month:** Bar chart displaying the average number of logins for each month, broken down by plan type.
    * **Login Rate by Plan Type and Customer:** Shape chart illustrating the login rate per customer for each plan type.

* **Vendor Integration Score Card:** Examines customer integration with vendors.
    * **Vendor Integration Rate:** Bar chart showing the success rate of integrations with different vendors, broken down by status.
    * **Vendor Integration Success Rate by Customers:** Heatmap displaying the integration success rate for each customer, broken down by status.
    * **Vendor Categories:** Pie chart showing the distribution of integrations across different vendor categories.
    * **Plan Type Filter:** Allows filtering the Vendor Integration Success Rate by Customers view by plan type.

* **Playbook Tasks Completion Score Card:** Tracks playbook completion rates.
    * **Playbook Tasks Completion Rate Over Time:** Bar chart showing the playbook completion rate for each customer.
    * **Playbook Completion:** Heatmap displaying the maximum completion percentage for each customer broken down by month and year.

* **Monitor Usage Completion Score Card:**  Monitors the usage and status of monitors.
    * **Monitor Count per Customers:** Heatmap showing the number of monitors per customer, broken down by monitor status.
    * **Median Monitor Status Changes per Number of User Group:**  Bubble chart showing the median number of monitor status changes for different user groups.
    * **Monitor Status Rate:** Heatmap displaying the percentage of monitors in each status for each customer.
    * **Status (Monitors) Filter:** Allows filtering the Monitor Count per Customers view by monitor status.

* **Published Policies Score Card:** Shows the number of published policies.
    * **Policies Category Count:** Bar chart showing the count of policies in each category.
    * **Published Policies Per Customer:** Bar chart displaying the number of published policies per customer.
    * **Median Published Policies by Number of Users Group:** Bar chart showing the median number of published policies for different user groups.

* **Score Card:** Displays an overview image representing the overall scorecard.


## 5. Filters & Interactions

* **Plan Type Filter (Vendor Integration Score Card):**  Filters the "Vendor Integration Success Rate by Customers" view to show data only for the selected plan type(s).
* **Status (Monitors) Filter (Monitor Usage Completion Score Card):** Filters the "Monitor Count per Customers" view to show data only for the selected monitor status(es).
* **Highlight Action (Monitor Count per Customers):** Selecting a monitor status in the "Monitor Count per Customers" view highlights corresponding data points in other views on the dashboard.


## 6. Usage Tips

* It's generally recommended to apply filters first to narrow down the data before exploring specific visualizations.
* Use the tooltips to get more detailed information about individual data points.
* Explore the different dashboards and story points to gain a holistic view of product adoption.


## 7. Limitations/Assumptions

* **Data Latency:** The data in this dashboard is updated daily.  Therefore, there may be a 24-hour delay between real-time activity and what is reflected in the dashboard.
* **Data Exclusions:**  The data may not include customers who have not logged in or interacted with the product.
* **"What is this?" Columns:** Several tables contain a column named "What is this?".  This column's purpose is unclear and its data is not used in the dashboard.  Further investigation is needed to understand the meaning and relevance of this column.
* **Unnamed Columns (F3, F4, F5, etc.):** Several tables contain unnamed columns.  These are not utilized in the dashboard and should be reviewed for potential inclusion or removal from the dataset.


## 8. FAQs or Common Misunderstandings

* **Q: Why is the training adoption rate for some customers greater than 100%?**  A: This can occur if a customer has trained more employees than they have active users. This may indicate they are training employees in anticipation of adding more users or are using the training for other purposes.
* **Q: How are the "Number of Users" groups determined?** A: The user groups are created using bins: 0-50, 51-100, 101-200, and 201-500. This allows for analysis based on customer size.


This documentation provides a comprehensive guide to understanding and utilizing the Product Adoption Scorecard dashboard.  If you have further questions, please contact the Business Operations team. 