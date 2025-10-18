# Minetrack
A Django based mining operations expense and profit management system.
Project Progress

Week 1 — Project Setup & Requirements

Initialized a Django project and configured version control (Git).

Set up PostgreSQL/SQLite database connection.

Defined core models and relationships across dispatch, production, and logistics apps.

Week 2 — User Management System

Implemented user registration, authentication, and role-based access control (RBAC).

Added user login/logout functionality.

Created different access levels for Admin, Staff, and Viewer roles.

Week 3 — Core Functionality Development

Developed CRUD modules for:

Dispatch — tracking dispatch orders and driver assignments.

Production — recording production runs, materials, and quantities.

Logistics — managing deliveries, routes, and transport costs.

Linked models for relational data consistency.

Week 4 — Reporting and Analytics

Built a report generation system that aggregates data across all apps.

Implemented cost calculations and data summaries for specific date ranges.

Created a summary view to display breakdowns for each report.

Resolved several key issues:

AttributeError: 'Report' object has no attribute 'generate_report' — fixed by adjusting the method reference in the admin.

NoReverseMatch: URL patterns updated to properly handle report detail views.

NameError: resolved undefined variable references in admin.py.
