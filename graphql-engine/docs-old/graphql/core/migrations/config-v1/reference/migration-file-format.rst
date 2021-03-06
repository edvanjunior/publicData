.. meta::
   :description: Hasura Migration file format reference
   :keywords: hasura, docs, migration, file format

.. _migration_file_format_v1:

Migration file format reference (config v1)
===========================================

.. contents:: Table of contents
  :backlinks: none
  :depth: 1
  :local:

Migration filename format
-------------------------

Each migration file has the following format:

.. code-block:: bash

   <version>_<name>.{up|down}.{sql|yaml}

A ``version`` which is the Unix timestamp in nanoseconds when the file was
created is the first part. Followed by a ``name`` which is either manually added
or auto-generated by the console. The next part indicates what step this is. If
it is ``up``, it means that this is the forward step, for e.g. creating a
relationship or a table. The ``down`` indicates that it is the corresponding
rollback step. The last part denotes the file format - whether it is an SQL file
or a YAML file.

YAML files
----------

Each ``up`` or ``down`` YAML file contains Hasura metadata API actions to be
executed for that particular migration. The file should have a list of such API
actions, which is represented with a ``-`` in YAML. Here is an example file:

**1551151778747_create_table_public_author.up.yaml**

.. code-block:: yaml

   - type: run_sql
     args:
       sql: |
         CREATE TABLE "public"."author" (
           "id" SERIAL NOT NULL,
           "name" TEXT NOT NULL,
           PRIMARY KEY ("id")
         );
   - type: track_table
     args:
       schema: public
       name: author

**1551151778747_create_table_public_author.down.yaml**

.. code-block:: yaml

   - type: untrack_table
     args:
       schema: public
       name: author
   - type: run_sql
     args:
       sql: |
         DROP TABLE "public"."author"

Each one of the actions in these files are actually Hasura metadata API calls,
which are executed in **sequence** when the migration is applied. You can find
all the metadata actions that are available in the :ref:`metadata API reference <metadata_query>`.


SQL Files
---------

.. note::

   The files are there just for the user's convenience, since the SQL can
   already be included in the YAML files.

As the name indicates, an SQL file can contain SQL statements which are executed
on the apply step of the migration. There can be an ``up`` SQL and a ``down``
SQL file. The SQL file is executed first if it is present in an up migration and the
YAML file is executed first in a down migration.

