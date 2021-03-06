.. meta::
   :description: Performance of Hasura GraphQL queries on MS SQL Server
   :keywords: hasura, docs, ms sql server, schema, queries, performance

.. _ms_sql_server_query_performance:

MS SQL Server: Query performance
================================

.. contents:: Table of contents
  :backlinks: none
  :depth: 2
  :local:

Introduction
------------

Sometimes queries can become slow due to large data volumes or levels of nesting.
This page explains how to identify the query performance, and how queries can be optimized.

.. _ms_sql_server_analysing_query_performance:

Analysing query performance
---------------------------

Let's say we want to analyse the following query:


.. code-block:: graphql

   query {
      authors(where: {name: {_eq: "Mario"}}) {
         rating
      }
   }

In order to analyse the performance of a query, you can click on the ``Analyze`` button on the Hasura console:

.. thumbnail:: /img/graphql/core/queries/analyze-query.png
   :width: 800px
   :alt: Query analyze button on Hasura console

The following query execution plan is generated:

.. thumbnail:: /img/graphql/core/queries/query-analysis-before-index.png
   :width: 800px
   :alt: Execution plan for Hasura GraphQL query

We can see that a sequential scan is conducted on the ``authors`` table. This means that MS SQL Server goes through every row of the ``authors`` table in order to check if the author's name equals "Mario".
The ``cost`` of a query is an arbitrary number generated by MS SQL Server and is to be interpreted as a measure of comparison rather than an absolute measure of something.

Read more about query performance analysis in the `MS SQL Server explain statement docs <https://docs.microsoft.com/en-us/sql/t-sql/queries/explain-transact-sql?view=azure-sqldw-latest>`__.

Query optimization
------------------

.. _ms_sql_server_data_validation_mssql_indexes:

Using MS SQL indexes
^^^^^^^^^^^^^^^^^^^^

`MS SQL Server indexes <https://docs.microsoft.com/en-us/sql/relational-databases/indexes/indexes?view=sql-server-ver15>`__ are special lookup tables that MS SQL Server can use to speed up data lookup.
An index acts as a pointer to data in a table, and it works very similar to an index in the back of a book.
If you look in the index first, you'll find the data much quicker than searching the whole book (or - in this case - database).

Let's say we know that ``authors`` table is frequently queried by ``name``:

.. code-block:: graphql

   query {
      authors(where: {name: {_eq: "Mario"}}) {
         rating
      }
   }

We've seen in the :ref:`above example <ms_sql_server_analysing_query_performance>` that by default MS SQL Server conducts a sequential scan i.e. going through all the rows.
Whenever there is a sequential scan, it can be optimized by adding an index.

The following statement sets an index on ``name`` in the ``authors`` table.

.. code-block:: plpgsql

  CREATE INDEX ON authors (name);

.. rst-class:: api_tabs
.. tabs::

  .. tab:: Console

   An index can be added in the ``Data -> SQL`` tab in the Hasura console.

  .. tab:: CLI

   :ref:`Create a migration manually <manual_migrations>` and add your create index statement to the ``up.sql`` file.
   Also, add an SQL statement to revert that statement to the ``down.sql`` file in case you need to :ref:`roll back <roll_back_migrations>` the migration.

   Apply the migration by running:

   .. code-block:: bash

      hasura migrate apply

  .. tab:: API

   You can add an index by making an API call to the :ref:`schema_run_sql metadata API <schema_run_sql>`:

   .. code-block:: http

      POST /v2/query HTTP/1.1
      Content-Type: application/json
      X-Hasura-Role: admin

      {
         "type": "run_sql",
         "args": {
            "source": "<db-name>",
            "sql": "<create index statement>"
         }
      }

Let's compare the performance analysis to :ref:`the one before adding the index <ms_sql_server_analysing_query_performance>`.
What was a ``sequential scan`` in the example earlier is now an ``index scan``. ``Index scans`` are usually more performant than ``sequential scans``.
We can also see that the ``cost`` of the query is now lower than the one before we added the index.

.. thumbnail:: /img/graphql/core/queries/query-analysis-after-index.png
   :width: 800px
   :alt: Execution plan for Hasura GraphQL query

.. note::

   In some cases sequential scans can still be faster than index scans, e.g. if the result returns a high percentage of the rows in the table.
   MS SQL Server comes up with multiple query plans and takes the call on what kind of scan would be faster.
