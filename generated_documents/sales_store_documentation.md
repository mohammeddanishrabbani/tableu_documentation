# Department Store Sales Analysis Dashboard Documentation

## 1. Dashboard Overview

This suite of dashboards provides an interactive view of sales data for a department store. It comprises three main dashboards, each focusing on a different aspect of the business:

* **Executive Overview Dashboard:**  Provides a high-level summary of key performance indicators (KPIs) related to sales, gross profit, quantity sold, and number of orders. It also allows for year-over-year comparisons and includes trend charts for Sales, Gross Profit, Total Quantity Sold, and # of Orders.
* **Product Analysis Dashboard:** Focuses on product performance, showcasing top and bottom performers based on a selectable metric (Sales, Profit, or Quantity).  It also includes a trend chart for top sellers and a visualization of product orders by region.
* **Orders Dashboard:**  Offers a detailed view of order details, including filtering options by customer, country, and year.

All dashboards provide navigation buttons for easy access to other dashboards and export options for PDF, PowerPoint, and Image formats.

## 2. Purpose of the Dashboard

The purpose of these dashboards is to monitor and analyze sales performance, identify trends, understand customer preferences, and gain insights to inform business decisions related to inventory, pricing, and marketing strategies.

## 3. Business Questions it Answers

The dashboards answer the following business questions:

* **Overall Performance:**
    * How are overall sales, gross profit, quantity sold, and number of orders trending year over year?
    * What is the profit margin trend?
    * How does cost of goods sold (COGS) compare to revenue?
* **Product Performance:**
    * What are our top 5 best-selling products?
    * What are our 5 worst-performing products?
    * How are sales of our best-selling products trending over time?
    * What are customer product preferences by country?
* **Order Details:**
    * What are the details of individual orders (customer, country, city, product, quantity, sales)?
    * How many orders are placed by each customer?
    * What is the sales distribution across different regions?

## 4. Intended Audience

The dashboards are intended for a variety of stakeholders, including:

* **Executives:** To monitor overall business performance and identify areas for improvement.
* **Sales Analysts:** To analyze sales trends and identify contributing factors.
* **Product Managers:** To understand product performance and make informed decisions about inventory and pricing.
* **Marketing Teams:** To gain insights into customer preferences and tailor marketing campaigns.

## 5. Data Sources Used

The dashboards utilize data from an Excel file named "ex4-departmentstore". The following tables from this file are used in a federated data source:

* **OrderDetails:** Contains details of each order, including OrderID, ProductID, Quantity, Sales, Discount, Cost of Sales (COS), and Gross Profit (GP).
* **OrderHeader:** Contains information about the order header, including OrderDate, CustomerID, EmployeeID, ShippingCost, OrderID, ShippingCompany, and DeliveryDate.
* **Customers:** Contains customer information, such as Address, City, ContactName, Country, Region, Customer, CustomerID, Fax, Phone, PostalCode, CountryCode, Latitude, and Longitude.
* **Employees:** Contains employee data, including EmployeeID, Extension, EmployeeName, EmployeeGender, Hire Date, Office, Supervisor, JobTitle, AnnualSalary, and Sales Target.
* **Offices:** Contains office information, including Office and SalesOffice.
* **Products:** Contains product data, including ProductID, CategoryID, ProductName, and SupplierID.
* **Category:** Contains product category details including CategoryID, CategoryName, Department, and Description.
* **Suppliers:** Contains supplier details, including SupplierID, Supplier, SupplierContact, and SupplierCountry.


The data is extracted into a Hyper file for performance optimization.  Two parameters are also used:

* **Year_P:**  Allows users to select the year for analysis.
* **Metric Select:** Allows users to select the metric (Sales, Profit, Quantity) for product performance analysis.


This documentation provides a comprehensive understanding of the department store sales analysis dashboards. For any further questions, please contact the data analytics team.