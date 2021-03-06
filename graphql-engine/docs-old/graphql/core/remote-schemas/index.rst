.. meta::
   :description: Manage remote schemas with Hasura
   :keywords: hasura, docs, remote schema

.. _remote_schemas:

Remote Schemas
==============

.. contents:: Table of contents
  :backlinks: none
  :depth: 1
  :local:

Introduction
------------

Hasura gives you CRUD + realtime GraphQL APIs with authorization & access control. However, in many cases, you will
need to write APIs (queries, mutations) that contain custom logic. For example, implementing a payment API, or
querying data that is not in your database.

Hasura has the ability to merge remote GraphQL schemas and provide a unified GraphQL API. Think of it
like automated schema stitching. All you need to do is build your own GraphQL service and then provide the HTTP
endpoint to Hasura. Your GraphQL service can be written in any language or framework.

This is what Hasura running with "Remote schemas" looks like:


.. thumbnail:: /img/graphql/core/remote-schemas/remote-schema-arch.png
   :class: no-shadow
   :width: 900px
   :alt: Architecture of Hasura with remote schemas

Use cases
---------

- Custom business logic, like a payment API
- Querying data that is not available in your database

You can handle these use cases by writing resolvers in a custom GraphQL server
and making Hasura merge this "remote schema" with the existing auto-generated
schema. You can also add multiple remote schemas. Think of the merged schema as
a union of top-level nodes from each of the sub-schemas.

.. note::

  If you are looking for adding authorization & access control for your
  app users to the GraphQL APIs that are auto-generated via Hasura, head to
  :ref:`auth`

.. admonition:: Health monitoring of remote schemas in Hasura Cloud
  :class: dhc
  
  Hasura Cloud offers built-in API metrics with integrated health checks and distributed tracing for your remote schemas. Read more at :ref:`Distributed Tracing in Hasura Cloud <tracing>`.

Learn more
----------

.. toctree::
   :maxdepth: 1

   adding-schema
   remote-schema-relationships
   auth/index

.. admonition:: Additional Resources

  Data Federation with Hasura - `Watch Webinar <https://hasura.io/events/webinar/data-federation-hasura-graphql/?pg=docs&plcmt=body&cta=watch-webinar&tech=>`__.