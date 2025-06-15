# Department Store Sales Analysis Dashboard Documentation

## 1. Dashboard Overview

This interactive dashboard suite analyzes department store sales performance, providing insights into key metrics, product trends, and regional data.  It aims to empower data-driven decisions for inventory, marketing, and business strategy. The dashboards are designed for executives, sales analysts, marketing managers, and inventory managers.

**Purpose and Business Questions:**

The dashboards address these key questions:

* **Overall Performance:**
    * What are the total sales, gross profit, quantity sold, and number of orders for a given year?
    * How do these KPIs compare to the previous year?
    * What are the monthly trends for sales, gross profit, and order quantity?
    * What is the overall profit margin and its trend over time?
    * How does cost of goods sold compare to revenue over time?
* **Product Performance:**
    * What are the top 5 best-selling and worst-selling products based on sales, profit, or quantity?
    * How has the performance of top sellers trended over time?
    * What are the customer preferences for product categories by country?
* **Regional Analysis:**
    * How do sales and profits vary by product category?
    * What are the sales figures by region/country?
    * What are the order details for each customer, including location, product, quantity, and sales?


## 2. Data Sources

Data is sourced from the "ex4-departmentstore" Excel workbook, which includes the following tables: OrderDetails, OrderHeader, Customers, Employees, Offices, Products, Category, and Suppliers.  These tables are linked to provide a comprehensive view of sales. Key fields include:

* **OrderDetails:** Order ID, Product ID, Quantity, Sales, Discount, Cost of Sales (COS), Gross Profit (GP).
* **OrderHeader:** Order Date, Customer ID, Employee ID, Shipping Cost, Order ID, Shipping Company, Delivery Date.
* **Customers:** Customer ID, Customer Name, Country, Region, City.
* **Products:** Product ID, Product Name, Category ID.
* **Category:** Category ID, Category Name, Department.

The data is extracted into a Hyper file for use in Tableau.


## 3. Key Metrics & Definitions

* **Sales:** Total revenue generated from product sales.
* **Gross Profit:**  Sales minus Cost of Goods Sold (COGS).
* **Quantity Sold:** The total number of units sold.
* **Number of Orders:** The total number of orders placed.
* **Profit Margin:**  (Gross Profit / Sales) * 100.  Expressed as a percentage.
* **Cost of Goods Sold (COGS):** The direct costs associated with producing the goods sold.

## 4. Dashboard Structure

The dashboard suite consists of three interconnected dashboards:

* **Executive Overview Dashboard:** Provides a high-level summary of KPIs (Sales, Gross Profit, Quantity Sold, Number of Orders) with year-over-year comparisons and trend analysis. Visualizations include KPI cards, bar charts for monthly trends, and a map showing sales by region.
* **Product Analysis Dashboard:** Focuses on product performance.  Includes visualizations for top/worst sellers, sales trends of best sellers, and a packed bubble chart showing product category preferences by country.  Uses a "Metric Select" filter to choose the performance metric (Sales, Profit, or Quantity).
* **Orders Dashboard:**  Displays detailed order information in a table, allowing exploration of sales and quantity by customer, country, and order date.  Includes filters for Customer, Country, and Order Date.

## 5. Filters & Interactions

* **Year_P Parameter:**  Filters data across all dashboards by the selected year.
* **Metric Select Parameter (Product Analysis Dashboard):**  Allows users to analyze product performance based on Sales, Profit, or Quantity.
* **Order Details Dashboard Filters:** Interactive filters for Customer, Country, and Order Date.
* **Navigation Buttons:** Buttons on each dashboard allow navigation to other dashboards in the suite.

## 6. Usage Tips

* Start by selecting the desired year using the Year_P parameter.
* On the Product Analysis Dashboard, experiment with the Metric Select parameter to gain different perspectives on product performance.
* Use the filters on the Orders Dashboard to drill down into specific customer segments, countries, or time periods.

## 7. Limitations/Assumptions

* The dashboards reflect the data present in the Excel workbook.  Accuracy depends on the underlying data quality.
* Calculations assume the relationships between tables in the Excel file are correctly defined.
* There may be a delay in data updates depending on the data refresh schedule.