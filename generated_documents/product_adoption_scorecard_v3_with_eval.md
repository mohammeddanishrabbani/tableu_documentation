# Product Adoption Scorecard and Analysis

## 1. Dashboard Overview

This interactive dashboard analyzes customer product adoption, providing insights into training completion, vendor integration success, login frequency, published policies, and monitor usage.  It helps stakeholders understand customer behavior, identify trends, and inform decisions related to product development, marketing, and customer success. The target audience includes Business Operations, Product Managers, Marketing, Customer Success, and Executive Leadership.

## 2. Data Sources

The dashboard uses data from the Excel file "Customer List+ (Q4 2021 Biz Ops Case Study - Sent)", specifically the following sheets:

* **Customer List:** Customer information (ID, number of users, creation date, plan type).  `CUSTOMER_ID` is the key field linking to other sheets.
* **Integrations:** Vendor integration details (vendor name, category, status).  Linked to Customer List via `CUSTOMER_ID`.
* **Logins:** Customer login times. Linked to Customer List via `CUSTOMER_ID`.
* **Monitor Status Changes:** Changes in monitor statuses. Linked to Customer List and Monitors via `CUSTOMER_ID` and `MONITOR_ID`.
* **Monitors:** Monitor information (category, type, status). Linked to Customer List via `CUSTOMER_ID`.
* **Playbooks:** Playbook completion data (completion date, completed tasks, total subtasks). Linked to Customer List via `CUSTOMER_ID`.
* **Policies:** Published policy information (category, creation date). Linked to Customer List via `CUSTOMER_ID`.
* **Training:** Employee training data (employees trained per customer). Linked to Customer List via `CUSTOMER_ID`.

These data sources are combined and extracted into a Tableau Hyper file ("Product_adoption_scorecard.hyper") for performance.

## 3. Key Metrics & Definitions

* **Training Adoption Rate:** Percentage of users trained per customer (`EMPLOYEES_TRAINED` / `NUMBER_OF_USERS`).
* **Login Rate Per Customer:** Average logins per user per customer (`COUNT(LOGIN_TIME)` / `NUMBER_OF_USERS`).
* **Playbook Completion Rate:**  Change in `COMPLETION_PERCENTAGE` over time, calculated as (`MAX(COMPLETION_PERCENTAGE)` - `MIN(COMPLETION_PERCENTAGE)`) / (`DATEDIFF('day', MIN(COMPLETED_ON), MAX(COMPLETED_ON))`).
* **Monitor Status Rate:** Percentage of monitors in each status (healthy, triggered, no datasource). Calculated as the count of monitors in each status divided by the total number of monitors.
* **Median Days Between Monitor Status Changes:** The median number of days between changes in monitor status, calculated using `DATEDIFF` on the `CREATED_AT` field in the Monitor Status Changes sheet.

## 4. Dashboard Structure

The dashboard is comprised of several visualizations, including:

* **Total Customers/Users/Trained Employees:**  Summary KPIs showing overall counts.
* **Count of Customers by Plan Type:** Bar chart displaying customer distribution across plan types.
* **Average Training Adoption Rate by Plan Type:**  Heatmap visualizing the average training adoption rate for each plan.
* **Product Adoption Rate by Trained Employee Count:** Scatter plot showing the relationship between trained employee count and product adoption rate.
* **User Logins by Pricing Tier:**  Bar chart displaying user login counts by plan type.
* **Average Logins by Month:** Bar chart showing average logins over time, broken down by plan type.
* **Login Rate by Plan Type and Customer:** Scatter plot visualizing login rate for each customer, segmented by plan type.
* **Vendor Integration Rate:** Bar chart displaying the success, pending, and error rates of vendor integrations.
* **Vendor Integration Success Rate by Customers:** Heatmap visualizing vendor integration success rates for each customer.
* **Vendor Categories:** Pie chart showing the distribution of vendor integration categories.
* **Playbook Completion:** Heatmap showing playbook completion percentage for each customer over time.
* **Playbook Tasks Completion Rate Over Time:** Bar chart displaying the playbook completion rate over time.
* **Playbook Tasks Completion Rate by Number of User Groups:** Bar chart displaying playbook completion rate by number of user groups.
* **Published Policies Per Customer:** Bar chart showing the number of published policies per customer.
* **Policies Category Count:** Packed bubble chart visualizing the count of policies in each category.
* **Median Published Policies by Number of Users Group:** Bar chart visualizing the median published policies for each number of users group.
* **Monitor Count per Customers:** Bar chart showing monitor counts per customer, broken down by monitor status.
* **Monitor Status Rate:** Bar chart visualizing the distribution of monitor statuses.
* **Median Days of Monitor Status Changes Per Number of Users Group:**  Heatmap visualizing median days between monitor status changes per user group.
* **Organization Monitor Usage Rate:** Heatmap showing the number of days between monitor status changes by number of users group.
* **Scorecard:** An overview image summarizing key product adoption metrics.

## 5. Filters & Interactions

Dashboards utilizing multiple sheets often employ filters to refine the data displayed.  While specific filter details are not available in the metadata, users should explore the available filters within each dashboard. Common filters might include date ranges, plan types, or vendor categories.  Some dashboards may also have highlight actions, allowing users to select a data point in one visualization and see related information highlighted in other visualizations.

## 6. Usage Tips

Start by applying any relevant filters, such as date ranges or plan types, to focus your analysis. Explore the different visualizations to understand the various aspects of product adoption. Use highlight actions, if available, to investigate specific customer segments or trends.

## 7. Limitations/Assumptions

The dashboard relies on data from the provided Excel file, which is a snapshot of Q4 2021 data.  Therefore, the insights may not reflect current customer behavior.  Additionally, the "What is this?" columns present in several sheets seem to contain extraneous data and were not used in the analysis.  There may be some unknown data quality issues within the source Excel file that could affect the accuracy of the metrics. The dashboard assumes that `CUSTOMER_ID` is a reliable identifier for linking data across different sheets.