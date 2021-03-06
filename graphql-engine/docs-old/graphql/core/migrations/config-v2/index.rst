.. meta::
   :description: Manage Hasura migrations and metadata
   :keywords: hasura, docs, migration, metadata

.. _migrations_v2:

Migrations & Metadata (config v2)
=================================

.. contents:: Table of contents
  :backlinks: none
  :depth: 2
  :local:

Introduction
------------

It is a typical requirement to export an existing Hasura "setup" so that you can
apply it on another instance to reproduce the same setup. For example, to achieve
a dev -> staging -> production environment promotion scenario.

.. note::

  This documentation is for Hasura migrations ``config v2``.

  For ``config v3``, see :ref:`migrations`.

How is Hasura state managed?
----------------------------

Hasura needs 2 pieces of information to recreate your GraphQL API, the underlying
PG database schema and the Hasura metadata which is used to describe the exposed
GraphQL API.

The :ref:`Hasura CLI <hasuracli_manual>` lets you manage these pieces of
information as you build your project via:

Database migration files
^^^^^^^^^^^^^^^^^^^^^^^^

The state of your PG database is managed via incremental SQL migration files.
These migration files can be applied one after the other to achieve the final
DB schema.

DB migration files can be generated incrementally and can by applied in parts to
reach particular checkpoints. They can be used to roll-back the DB schema as well.

.. note::

  You can choose to manage database migrations using external tools like knex, TypeORM,
  Django/Rails migrations, etc. as well.

Hasura metadata files
^^^^^^^^^^^^^^^^^^^^^

The state of Hasura metadata is managed via snapshots of the metadata. These
snapshots can be applied as a whole to configure Hasura to a state represented
in the snapshot.

Hasura metadata can be exported and imported as a whole.

Setting up migrations
---------------------

See :ref:`migrations_setup_v2`.


Advanced use cases
------------------

- :ref:`auto_apply_migrations_v2`
- :ref:`manual_migrations_v2`
- :ref:`roll_back_migrations_v2`
- :ref:`seed_data_migration_v2`

Reference documentation
-----------------------

- :ref:`migrations_how_it_works_v2`
- :ref:`Migration file format <migration_file_format_v2>`
- :ref:`Metadata format <metadata_format_v2>`

.. toctree::
  :maxdepth: 1
  :hidden:

  Setting up migrations <migrations-setup>
  Managing metadata <manage-metadata>
  Advanced use cases <advanced/index>
  Reference documentation <reference/index>
  Upgrading to config v2 <upgrade-v2>

