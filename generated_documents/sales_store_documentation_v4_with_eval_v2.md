# Department Store Performance Dashboard Documentation

## 1. Dashboard Overview

This interactive dashboard provides a comprehensive view of department store performance, empowering users to explore key metrics, trends, and gain valuable product insights. It's designed to help various stakeholders make data-driven decisions related to sales strategies, product assortment, and overall business operations.  The dashboard aims to answer crucial questions about overall performance, product performance, and order specifics, enabling informed decision-making.  It caters to a diverse audience, including executives, sales and marketing teams, product managers, and business analysts.

## 2. Data Sources

The dashboard uses data from the "ex4-departmentstore" Excel workbook. This workbook contains several interconnected sheets that provide a complete picture of the department store's operations:

* **OrderDetails:** Details about each product in an order, such as quantity, sales, discount, cost of sales, and gross profit.  This is linked to `OrderHeader` by `OrderID`.
* **OrderHeader:** Information about each order, including order date, customer ID, employee ID, shipping cost, order ID, shipping company, and delivery date. This sheet is the central hub, connecting to `Customers` through `CustomerID`, `Employees` via `EmployeeID`, and `OrderDetails` with `OrderID`.
* **Customers:** Customer information like address, city, contact name, country, region, customer name, customer ID, fax, phone, postal code, country code, latitude, and longitude.  Connected to `OrderHeader` via `CustomerID`.
* **Employees:**  Details about employees, such as employee ID, extension, employee name, gender, hire date, office, supervisor, job title, annual salary, and sales target. Linked to `OrderHeader` by `EmployeeID` and `Offices` through `Office`.
* **Offices:** Information about different office locations and their respective IDs.  Connected to `Employees` via `Office`.
* **Products:** Details about each product, including product ID, category ID, product name, and supplier ID. Related to `OrderDetails` through `ProductID`, `Category` by `CategoryID` and `Suppliers` via `SupplierID`.
* **Category:** Information about product categories, including category ID, category name, department, and description. Linked to `Products` via `CategoryID`.
* **Suppliers:** Details about suppliers, including supplier ID, supplier name, contact person, and country. Connected to `Products` through `SupplierID`.

The relationships between these sheets, based on their ID columns (OrderID, CustomerID, EmployeeID, ProductID, CategoryID, and SupplierID), allow for comprehensive analysis across different aspects of the business. The dashboard also utilizes Tableau Parameters for interactive filtering by Year and Metric (Sales, Profit, Quantity).


## 3. Key Metrics & Definitions

The dashboard presents several Key Performance Indicators (KPIs) to assess department store performance:

* **Sales:** The total revenue generated from product sales. Calculated as `Quantity * Unit Price * (1 - Discount)`.
* **Gross Profit (GP):** The profit earned after deducting the Cost of Goods Sold (COGS) from Sales.  Calculated as `Sales - COS`.
* **Profit Margin:** The percentage of revenue remaining after accounting for COGS.  Calculated as `Gross Profit / Sales`.
* **Quantity Sold:** The total number of units sold.
* **Number of Orders:** The total count of orders placed.
* **Cost of Goods Sold (COGS):** The direct costs associated with producing the goods sold by a company.
* **Year-over-Year (YoY) Growth:** The percentage change in a metric compared to the same period in the previous year. For example, YoY Sales growth shows how much sales increased or decreased compared to the previous year.  A positive value indicates growth, while a negative value indicates a decline.


## 4. Dashboard Structure

The dashboard is divided into three interconnected views:

* **Executive Overview Dashboard:** This high-level summary displays key performance indicators (KPIs) like total sales, gross profit, quantity sold, and number of orders. It allows year-over-year comparisons and shows monthly trends for these KPIs. Charts include bar graphs for monthly sales, gross profit, and quantity sold, allowing quick identification of peak and low periods.  A line graph visualizes profit margin trends over time, providing insight into profitability.  Another combination chart compares COGS and revenue over time, highlighting the relationship between costs and earnings. Navigation buttons provide access to other dashboards. Export options (PDF, PowerPoint, Image) are available.

* **Product Analysis Dashboard:** This dashboard focuses on detailed product performance.  It showcases the top 5 best-selling and worst-selling products based on a selectable metric (Sales, Profit, Quantity). Interactive bar charts visualize these top/bottom performers. A line chart displays sales trends for the best-selling products over time, helping to understand their performance trajectory.  A bubble chart visualizes product preferences by country, with bubble size representing the order volume for each product category in each country. This allows for easy identification of popular product categories in different regions.  Finally, a bar chart displays the distribution of sales and profit across different product categories, offering insights into category-level performance.  A parameter control allows users to switch the displayed metric. Navigation buttons are available.  Export options (PDF, PowerPoint, Image) are available.

* **Orders Dashboard:** This dashboard provides a detailed table view of order information.  The table includes columns for Customer, Country, Product, Quantity, and Sales.  Users can filter the table by Customer, Country, and Order Date. Navigation buttons are available. Export options (PDF, PowerPoint, Image) are available.

## 5. Filters & Interactions

* **Year Filter:**  The Executive Overview and Product Analysis dashboards include a filter to select the year for analysis.  This filter affects all visualizations on the respective dashboard, allowing users to focus on a specific year's performance.
* **Metric Filter (Product Analysis):** The Product Analysis dashboard includes a parameter control to select the metric (Sales, Profit, Quantity) used to rank best-selling and worst-selling products. Changing this filter updates the product rankings and related visualizations.
* **Order Details Filters (Orders Dashboard):** The Orders Dashboard allows filtering the order table by Customer, Country, and Order Date, providing granular control over the displayed information.
* **Navigation Buttons:** All dashboards include navigation buttons to easily switch between the different dashboard views.


## 6. Usage Tips

* **Executive Overview:** Start with this dashboard for a high-level overview before diving into detailed analysis.
* **Product Analysis:** Use the metric filter to analyze product performance from different perspectives (Sales, Profit, Quantity).
* **Orders Dashboard:** Filter the data by Customer, Country, or Order Date to find specific orders and understand customer behavior.


## 7. Limitations/Assumptions

* **Data Latency:** The dashboard data is refreshed on a schedule (not real-time).  Therefore, there might be a delay between actual performance and what's shown on the dashboard.
* **Data Accuracy:** The dashboard's accuracy depends on the quality of the underlying data in the Excel workbook.  It is assumed that the data is accurate and complete.
* **Historical Data:** The dashboard primarily focuses on historical data. While it can show trends, it doesn't provide predictive analytics.


## 8. FAQs or Common Misunderstandings

* **Why are some values shown as "£0"?**  This can occur if there were no sales, profit, or quantity recorded for a specific period or product.
* **How is the previous year's data calculated?**  The previous year's data is calculated based on the selected year in the year filter.  For example, if 2014 is selected, the previous year is 2013.