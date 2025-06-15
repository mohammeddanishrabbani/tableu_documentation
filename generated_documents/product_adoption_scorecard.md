# Product Adoption Scorecard and Analysis - Documentation

## 1. Dashboard Overview

The Product Adoption Scorecard and Analysis dashboard provides a comprehensive overview of how customers are adopting and utilizing our product. It offers insights into various aspects of product usage, including training completion, integration success, login frequency, monitor status, and published policies. The dashboard comprises several interactive visualizations that allow users to explore the data and identify trends across different customer segments, plan types, and time periods.

## 2. Purpose of the Dashboard

The primary purpose of this dashboard is to monitor and analyze product adoption trends to inform business decisions. It aims to identify areas of success, pinpoint potential roadblocks to adoption, and provide data-driven recommendations for improving product engagement and customer satisfaction.  This information can be used to refine marketing strategies, enhance product features, and tailor customer support efforts.

## 3. Business Questions it Answers

The dashboard is designed to answer the following key business questions:

* **Training:**
    * What is the overall training adoption rate?
    * How does the training adoption rate vary by plan type?
    * How many customers have not trained any users?
* **Integrations:**
    * What is the vendor integration success rate across different vendors and categories?
    * How does the vendor integration rate vary by customer?
    * What are the most popular vendor categories?
* **Logins:**
    * What is the average login rate per customer?
    * How does the login rate differ by plan type and customer?
    * How do average logins trend over time, broken down by month and plan type?
* **Monitors:**
    * How many monitors are being used per customer?
    * What is the monitor status rate (healthy, triggered, no datasource)?
    * How does the median time between monitor status changes vary by the number of users?
* **Policies:**
    * How many policies are being published per customer?
    * What are the most common policy categories?
    * How does the median number of published policies differ by the number of users?

## 4. Intended Audience

This dashboard is intended for a variety of stakeholders, including:

* **Business Operations Teams:** To monitor product adoption metrics and identify areas for improvement.
* **Product Managers:** To understand customer usage patterns and inform product development decisions.
* **Marketing Teams:** To tailor marketing campaigns and target specific customer segments.
* **Sales Teams:** To gain insights into customer engagement and identify upsell/cross-sell opportunities.
* **Executive Leadership:** To track overall product performance and assess the effectiveness of adoption strategies.

## 5. Data Sources Used

The dashboard utilizes data from a single Excel file named "Customer List+ (Q4 2021 Biz Ops Case Study - Sent)".  Within this Excel file, data is pulled from the following sheets (effectively acting as tables):

* **Customer List:** Contains information about each customer, including their ID, number of users, creation date, plan type, and other attributes.
* **Integrations:** Details customer integrations with different vendors, including vendor name, category, and status.
* **Logins:** Tracks customer login activity, including customer ID and login time.
* **Monitor Status Changes:** Records changes in monitor status for each customer, including timestamp, status, and change type.
* **Monitors:** Contains information about the monitors used by customers, such as category, status, and type.
* **Playbooks:** Tracks the completion of playbooks by customers, including completion date, number of completed tasks, and total subtasks.
* **Policies:**  Details the policies published by customers, including category and creation date.
* **Training:** Records the number of employees trained for each customer.


These sheets are linked together within Tableau using the Customer ID field to create a relational data model.  A Hyper extract of this combined data is also used for performance optimization.