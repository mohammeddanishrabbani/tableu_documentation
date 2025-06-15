# Product Adoption Scorecard Dashboard Documentation

## 1. Dashboard Overview

This dashboard provides a comprehensive overview of product adoption across various customer segments. It aims to answer key business questions regarding user training, feature usage, integration success, and overall product engagement.  This information can be used to identify areas for improvement, tailor product offerings, and drive further adoption.

**Business Questions Answered:**

* What is the overall training adoption rate across different customer plan types?
* How are customers utilizing different product features (Monitors, Playbooks, Policies)?
* What is the success rate of vendor integrations, and are there any common integration challenges?
* How frequently are users logging in, and are there any trends in login activity?
* How does product usage correlate with customer size (number of users)?

**Target Audience:**

* Business Operations Teams
* Product Management
* Sales & Marketing
* Executive Leadership

## 2. Data Sources

The dashboard pulls data from an Excel file named "Customer List+ (Q4 2021 Biz Ops Case Study - Sent)" which contains the following interconnected tables:

* **Customer List:** Contains information about each customer, including their ID, number of users, creation date, and plan type.
* **Integrations:**  Tracks vendor integrations for each customer, including vendor name, category, and integration status.
* **Logins:**  Records customer login times.
* **Monitor Status Changes:**  Tracks changes in the status of monitors.
* **Monitors:** Contains data about monitors used by customers, including category, type, and status.
* **Playbooks:** Tracks playbook completion data for each customer.
* **Policies:**  Records policy creation data for customers.
* **Training:**  Contains information about employee training completion.


**Key Fields:**

* **CUSTOMER_ID:** Unique identifier for each customer. This field is crucial for linking data across all tables.
* **NUMBER_OF_USERS:**  Indicates the size of the customer organization. Used for segmentation and normalization.
* **PLAN_TYPE:** The customer's subscription plan. Used for comparing adoption rates across different plans.
* **CREATED_AT:** Timestamps for various actions, such as customer creation, policy creation, and monitor status changes.
* **STATUS:** Represents the status of various processes (integrations, monitors).
* **COMPLETED_ON:** Date of playbook completion.
* **COMPLETION_PERCENTAGE:**  Percentage of playbook tasks completed.
* **EMPLOYEES_TRAINED:** Number of employees who have completed training.

## 3. Key Metrics & Definitions

* **Training Adoption Rate:** The percentage of users within a customer organization who have completed training.
    * *Calculation:* `[EMPLOYEES_TRAINED]/[NUMBER_OF_USERS]`
* **Login Rate Per Customer:** The average number of logins per user within a customer organization.
    * *Calculation:* `COUNT([LOGIN_TIME])/SUM([NUMBER_OF_USERS])`
* **Playbook Completion Rate:**  The average daily change in playbook completion percentage.
    * *Calculation:* `(MAX([COMPLETION_PERCENTAGE])-MIN([COMPLETION_PERCENTAGE])) / DATEDIFF('day', (MIN([COMPLETED_ON])),(MAX([COMPLETED_ON])))`
* **Days Since Previous Date (Monitor Status Changes):** The number of days elapsed between consecutive monitor status changes.
    * *Calculation:* `DATEDIFF('day', LOOKUP(MIN([CREATED_AT (Monitor Status Changes)]),-1), MIN([CREATED_AT (Monitor Status Changes)]))`


## 4. Dashboard Structure

The dashboard is composed of several interconnected worksheets, organized into story points and dashboards.

**Key Worksheets and How to Read Them:**

* **Total Customers/Users/Trained Employees:** Single-value visualizations displaying the total counts.
* **Product Adoption Rate by Trained Employee Count:** Scatter plot showing the relationship between the number of users and the training adoption rate for each customer.  Color indicates the number of employees trained.  Darker red signifies a higher number of trained employees.
* **Count of Customers by Plan Type:** Bar chart showing the number of customers for each plan type. Color intensity represents the number of users within each plan.
* **Average Training Adoption Rate by Plan Type:** Bar chart displaying the average training adoption rate for each plan type. Color intensity indicates the adoption rate, with darker blue representing higher rates.
* **User Logins by Pricing Tier:**  Bubble chart showing user logins by the number of users and plan type. Bubble size corresponds to the number of logins. Color represents plan type.
* **Average Logins by Month:**  Bar chart visualizing average logins per month, broken down by plan type. Color represents the month.
* **Login Rate by Plan Type and Customer:**  Shape chart showing login rate per customer, broken down by plan type.  Color represents customer ID.
* **Vendor Integration Rate:** Bar chart showing the number of integrations for each vendor, broken down by status. Color represents integration status.
* **Vendor Integration Success Rate by Customers:** Heatmap showing the integration success rate for each customer, broken down by status. Color intensity represents the success rate.
* **Vendor Categories:** Pie chart displaying the distribution of vendor integrations across different categories.  Size of the pie slice and the percentage labels show the proportion of each category.
* **Playbook Completion:**  Heatmap visualizing playbook completion percentage for each customer over time. Color intensity represents the completion percentage.
* **Playbook Tasks Completion Rate Over Time:** Bar chart showing the playbook completion rate for each customer. Color intensity corresponds to the completion rate.
* **Playbook Tasks Completion Rate by Number of User Groups:** Bar chart displaying playbook completion rate by number of users group. Color intensity reflects the completion rate.
* **Policies Category Count:**  Bar chart showing the count of policies within each category. Color intensity corresponds to the policy count.
* **Published Policies Per Customer:** Bar chart displaying the number of published policies for each customer.  Color intensity represents the number of policies.
* **Median Published Policies by Number of Users Group:** Bar chart showing the median published policies by user group.
* **Monitor Status Rate:**  Heatmap showing the status of monitors for each customer. Color intensity represents the windowed total count of monitors.
* **Monitor Count per Customers:** Heatmap visualizing the number of monitors per customer, broken down by status. Color represents monitor status.
* **Median Monitor Status Changes per Number of User Group:** Heatmap showing the median number of monitor status changes per user group.
* **Median Days of Monitor Status Changes Per Number of Users Group:** Heatmap showing the median days between monitor status changes by number of users group.
* **Organization Monitor Usage Rate:**  Heatmap showing organization monitor usage rate by number of user group.


**Dashboards:**

* **Product Adoption Scorecard:** A storyboard navigating through key insights and metrics related to product adoption, including user training, vendor integration, user logins, playbook completion, monitor usage, and published policies.
* **User Training Score Card:**  Focuses on user training metrics, showing total customers, total users, total trained users, count of customers by plan type, average training adoption rate by plan type, and product adoption rate by trained employee count.
* **User Login Score Card:**  Presents user login data, visualizing user logins by pricing tier, average logins by month, and login rate by plan type and customer.
* **Vendor Integration Score Card:** Displays vendor integration metrics, including vendor integration rate, vendor integration success rate by customers, and vendor categories.
* **Playbook Tasks Completion Scorecard:** Tracks playbook completion, showing playbook tasks completion rate over time and playbook completion status.
* **Monitor Usage Completion Score Card:** Visualizes monitor usage and status changes, including monitor count per customer, monitor status rate, median monitor status changes per number of user group, and median days of monitor status changes per number of users group.
* **Published Policies Score Card:**  Focuses on published policies, presenting policies category count, published policies per customer, and median published policies by the number of users group.
* **Scorecard:** Displays an overview image of the scorecard.


## 5. Filters & Interactions

The dashboard utilizes filters to allow users to focus on specific segments of data.

* **Plan Type Filter:**  Allows filtering data by customer plan type.
* **Status Filters:**  Enable filtering by the status of integrations and monitors.
* **Number of Users (group):**  This calculated field groups customers by their number of users (0-50, 51-100, 101-200, 201-500). This can be used as a filter to analyze adoption across different customer sizes.

**Highlight Actions:**

* **Monitor Count per Customers:** Selecting a monitor status highlights the corresponding data across the dashboard.


## 6. Usage Tips

* It is recommended to apply filters first to narrow down the data and improve performance.
* Explore the tooltips on each visualization for detailed information about specific data points.
* Use the story points in the "Product Adoption Scorecard" dashboard to navigate through the key insights.


## 7. Limitations/Assumptions

* **Data Latency:** The data is refreshed daily. Therefore, the dashboard might not reflect real-time product usage.
* **Data Exclusions:** The data used in this dashboard covers Q4 2021 and might not represent current trends.
* **Unclear Columns:** Several columns labelled "What is this?" and "F#" are present in the dataset but their purpose is unknown and they are therefore excluded from the analysis.  Clarification on these columns would improve the analysis.


## 8. FAQs or Common Misunderstandings

* **Why are some customer IDs not present in all worksheets?**  This is because not all customers have data in all tables. For example, a customer might not have any integrations or might not have completed any playbooks.
* **How is the 'Number of Users (group)' calculated?**  This is a calculated field that bins customers based on their number of users into four groups: 0-50, 51-100, 101-200, and 201-500.
* **What does 'no_datasource' mean in the Monitor Status?**  This indicates that there is no data source available for that specific monitor.


This documentation provides a starting point for understanding and using the Product Adoption Scorecard dashboard. If you have further questions, please contact the Business Operations team. 