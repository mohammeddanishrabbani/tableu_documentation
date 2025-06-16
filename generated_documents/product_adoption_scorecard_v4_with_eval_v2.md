# Product Adoption Scorecard Documentation

## 1. Dashboard Overview

This interactive scorecard helps us understand how customers use our product. It shows key adoption metrics for different customer segments (based on number of users), plan types, and vendor integrations.  The dashboard is designed with a main storyboard for easy navigation between different sections, each focusing on a specific area of product adoption.

**Purpose:** The scorecard tracks product adoption trends to:

* Identify successful areas and areas for improvement.
* Understand customer behavior.
* Make data-driven decisions for product development, marketing, and customer support.

**Target Audience:** This dashboard is for:

* **Business Operations Teams:** Monitor performance and identify areas needing attention.
* **Product Managers:** Understand customer usage and plan product roadmaps.
* **Marketing Teams:** Tailor campaigns based on adoption and customer segments.
* **Customer Success Teams:** Proactively address issues and improve onboarding/training.
* **Executive Leadership:** Get a high-level view of adoption and its impact on business goals.

## 2. Data Sources

The scorecard uses data from the Excel file "Customer List+ (Q4 2021 Biz Ops Case Study - Sent)". The key interconnected sheets are linked by `CUSTOMER_ID`:

* **Customer List:** Customer details (ID, user count, creation date, plan type).
* **Integrations:** Customer integration details (vendor, category, status).
* **Logins:** Customer login times.
* **Monitor Status Changes:** Timestamps and types of monitor status changes.
* **Monitors:** Monitor details (category, status, type).
* **Playbooks:** Playbook completion data (completion dates, tasks, percentage).
* **Policies:** Published policy details (category, creation date).
* **Training:** Employee training data (trained employees per customer).

For performance, the data is extracted into a Tableau Hyper file named "Product_adoption_scorecard.hyper".

## 3. Key Metrics & Definitions

* **Training Adoption Rate:** Percentage of users trained per customer.
    * *Calculation:* `Employees Trained / Number of Users`
* **Login Rate Per Customer:** Average monthly logins per user for each customer.
    * *Calculation:* `Count of Login Times / Number of Users`
* **Vendor Integration Success Rate:** Percentage of successful vendor integrations.
    * *Calculation:* `Count of Successful Integrations / Count of All Integrations`
* **Monitor Status Rate:** Percentage of monitors in each status (healthy, triggered, no datasource).
    * *Calculation:* `Count of Monitors with Specific Status / Count of All Monitors`
* **Published Policies Per Customer:** Number of policies published by each customer.
    * *Calculation:* `Count of Policies for each Customer`
* **Playbook Completion Rate:** Rate of change in playbook completion percentage over time.
    * *Calculation:* `(Max Completion Percentage - Min Completion Percentage) / Date Difference between First and Last Completion Date`


## 4. Dashboard Structure

The scorecard is divided into several interactive sections, accessible via the main storyboard:

* **User Training Score Card:** Focuses on training adoption rates across plan types and customers. Includes visualizations for overall training adoption rate, distribution of trained employees, and customers with no trained users.
* **Vendor Integration Score Card:** Shows integration success rates for different vendors, categories, customers, and plan types. Includes visualizations for distribution of vendor integrations and success rates.
* **User Login Score Card:**  Analyzes login frequency by plan type, customer, and pricing tier. Includes visualizations showing average logins per month and login rate per customer.
* **Playbook Tasks Completion Score Card:** Tracks playbook completion rates over time and by number of user groups.  Includes visualizations showing playbook completion progress and rates.
* **Monitor Status Score Card:**  Provides an overview of monitor usage and status changes. Includes visualizations for monitor count per customer, monitor status rate, and median days between status changes.
* **Published Policies Score Card:** Shows the number of published policies per customer and their distribution across categories. Includes visualizations for policy category count and median published policies by user group.
* **Score Card:** Provides a summarized overview of key metrics.


## 5. Filters & Interactions

Most visualizations allow filtering by plan type, customer segment (number of users), and vendor. Applying filters will update the corresponding charts and tables.  Some charts include drill-down capabilities, allowing a deeper dive into specific customer segments or plan types.  Highlight actions are also available, enabling users to select a data point in one visualization and see related information highlighted in other visualizations.


## 6. Usage Tips

* **Start with Filters:** Begin your analysis by applying filters to narrow your focus to specific customer segments, plan types, or time periods.
* **Explore Tooltips:** Hover over data points in visualizations to see detailed information and tooltips.
* **Utilize the Storyboard:** Use the storyboard to navigate between different sections of the scorecard and gain a comprehensive view of product adoption.



## 7. Limitations/Assumptions

* **Data Freshness:** The data is from Q4 2021 and may not reflect the current state of product adoption. Updates are performed periodically.
* **Data Completeness:**  The dataset may not capture all customer interactions with the product.  For example, certain features or usage patterns may not be tracked.
* **Calculated Metrics:** Some metrics, such as Playbook Completion Rate, are calculated based on available data and may not perfectly represent the underlying activity.


## 8. FAQs or Common Misunderstandings

* **Why is my customer not showing up on the dashboard?** The current data is from Q4 2021.  If your customer joined after this period, they won’t be included.
* **What does "initial status" mean in the Monitor Status Changes visualization?** This represents the initial status of a monitor when it was first added.
* **How often is the data updated?** The data is currently updated quarterly. We are working towards more frequent updates.