import pytest
import os
from ruamel.yaml import YAML

yaml=YAML(typ='safe', pure=True)

resp_pg_version_map = {
    '9_5': 'response_9',
    '9_6': 'response_9',
    '10': 'response_10_11',
    '11': 'response_10_11',
    '12': 'response_10_11',
    '13': 'response_10_11',
    'latest': 'response_10_11'
}

@pytest.mark.usefixtures('per_method_tests_db_state')
class TestPGDump:

    def test_pg_dump_for_public_schema(self, hge_ctx):
        query_file = self.dir() + '/pg_dump_public.yaml'
        PG_VERSION = os.getenv('PG_VERSION', 'latest')
        with open(query_file, 'r') as stream:
            q = yaml.load(stream)
            headers = q['headers'] or {}
            if hge_ctx.hge_key is not None:
                headers['x-hasura-admin-secret'] = hge_ctx.hge_key
            resp = hge_ctx.http.post(hge_ctx.hge_url + q['url'], json=q['query'], headers=headers)
            body = resp.text
            assert resp.status_code == q['status']
            print(body)
            print(q[resp_pg_version_map[PG_VERSION]])
            assert body == q[resp_pg_version_map[PG_VERSION]]

    def test_pg_dump_for_public_schema_for_user_role(self, hge_ctx):
        query_file = self.dir() + '/pg_dump_public.yaml'
        with open(query_file, 'r') as stream:
            q = yaml.load(stream)
            headers = q['headers'] or {}
            if hge_ctx.hge_key is not None:
                headers['x-hasura-admin-secret'] = hge_ctx.hge_key
            headers['X-Hasura-Role'] = 'user'
            resp = hge_ctx.http.post(hge_ctx.hge_url + q['url'], json=q['query'], headers=headers)
            body = resp.text
            assert resp.status_code == 400, body

    @classmethod
    def dir(cls):
        return "pgdump"
