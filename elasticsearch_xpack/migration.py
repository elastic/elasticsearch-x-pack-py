from elasticsearch.client.utils import NamespacedClient, query_params, _make_path, SKIP_IN_PATH

class MigrationClient(NamespacedClient):
    @query_params('allow_no_indices', 'expand_wildcards', 'ignore_unavailable')
    def get_assistance(self, index=None, params=None):
        """
        `<>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default 'open', valid
            choices are: 'open', 'closed', 'none', 'all'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        """
        return self.transport.perform_request('GET', _make_path('_xpack',
            'migration', 'assistance', index), params=params)

    @query_params()
    def upgrade(self, index, params=None):
        """
        `<>`_

        :arg index: The name of the index
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")
        return self.transport.perform_request('POST', _make_path('_xpack',
            'migration', 'upgrade', index), params=params)
