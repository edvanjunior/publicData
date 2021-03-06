.. meta::
   :description: Manage migrations on the database using the Hasura CLI
   :keywords: hasura, docs, CLI, hasura migrate

.. _hasura_migrate:

Hasura CLI: hasura migrate
--------------------------

Manage migrations on the database.

Synopsis
~~~~~~~~


Manage migrations on the database.

Options
~~~~~~~

::

      --admin-secret string            admin secret for Hasura GraphQL engine (env "HASURA_GRAPHQL_ADMIN_SECRET")
      --certificate-authority string   path to a cert file for the certificate authority (env "HASURA_GRAPHQL_CERTIFICATE_AUTHORITY")
      --database-name string           database on which operation should be applied
      --disable-interactive            disables interactive prompts (default: false) (env "HASURA_GRAPHQL_DISABLE_INTERACTIVE")
      --endpoint string                http(s) endpoint for Hasura GraphQL engine (env "HASURA_GRAPHQL_ENDPOINT")
  -h, --help                           help for migrate
      --insecure-skip-tls-verify       skip TLS verification and disable cert checking (default: false) (env "HASURA_GRAPHQL_INSECURE_SKIP_TLS_VERIFY")

Options inherited from parent commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

      --envfile string      .env filename to load ENV vars from (default ".env")
      --log-level string    log level (DEBUG, INFO, WARN, ERROR, FATAL) (default "INFO")
      --no-color            do not colorize output (default: false)
      --project string      directory where commands are executed (default: current dir)
      --skip-update-check   skip automatic update check on command execution

SEE ALSO
~~~~~~~~

* :ref:`hasura <hasura>` 	 - Hasura GraphQL engine command line tool
* :ref:`hasura migrate apply <hasura_migrate_apply>` 	 - Apply migrations on the database
* :ref:`hasura migrate create <hasura_migrate_create>` 	 - Create files required for a migration
* :ref:`hasura migrate delete <hasura_migrate_delete>` 	 - (PREVIEW) clear migrations from local project and server
* :ref:`hasura migrate squash <hasura_migrate_squash>` 	 - (PREVIEW) Squash multiple migrations into a single one
* :ref:`hasura migrate status <hasura_migrate_status>` 	 - Display current status of migrations on a database

*Auto generated by spf13/cobra*
