from elasticsearch.client.utils import NamespacedClient, query_params, _make_path, SKIP_IN_PATH

class WatcherClient(NamespacedClient):
    @query_params()
    def stop(self, params=None):
        """
        `<http://www.elastic.co/guide/en/watcher/current/appendix-api-service.html>`_
        """
        return self.transport.perform_request('POST', '/_xpack/watcher/_stop',
            params=params)

    @query_params('master_timeout')
    def ack_watch(self, watch_id, action_id=None, params=None):
        """
        `<http://www.elastic.co/guide/en/watcher/current/appendix-api-ack-watch.html>`_

        :arg watch_id: Watch ID
        :arg action_id: A comma-separated list of the action ids to be acked
        :arg master_timeout: Specify timeout for watch write operation
        """
        if watch_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'watch_id'.")
        return self.transport.perform_request('PUT', _make_path('_xpack',
            'watcher', 'watch', watch_id, '_ack', action_id), params=params)

    @query_params('debug')
    def execute_watch(self, id=None, body=None, params=None):
        """
        `<http://www.elastic.co/guide/en/watcher/current/appendix-api-execute-watch.html>`_

        :arg id: Watch ID
        :arg body: Execution control
        :arg debug: indicates whether the watch should execute in debug mode
        """
        return self.transport.perform_request('PUT', _make_path('_xpack',
            'watcher', 'watch', id, '_execute'), params=params, body=body)

    @query_params()
    def start(self, params=None):
        """
        `<http://www.elastic.co/guide/en/watcher/current/appendix-api-service.html>`_
        """
        return self.transport.perform_request('POST', '/_xpack/watcher/_start',
            params=params)

    @query_params('master_timeout')
    def activate_watch(self, watch_id, params=None):
        """
        `<https://www.elastic.co/guide/en/watcher/current/api-rest.html#api-rest-activate-watch>`_

        :arg watch_id: Watch ID
        :arg master_timeout: Specify timeout for watch write operation
        """
        if watch_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'watch_id'.")
        return self.transport.perform_request('PUT', _make_path('_xpack',
            'watcher', 'watch', watch_id, '_activate'), params=params)

    @query_params('master_timeout')
    def deactivate_watch(self, watch_id, params=None):
        """
        `<https://www.elastic.co/guide/en/watcher/current/api-rest.html#api-rest-deactivate-watch>`_

        :arg watch_id: Watch ID
        :arg master_timeout: Specify timeout for watch write operation
        """
        if watch_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'watch_id'.")
        return self.transport.perform_request('PUT', _make_path('_xpack',
            'watcher', 'watch', watch_id, '_deactivate'), params=params)

    @query_params('active', 'master_timeout')
    def put_watch(self, id, body, params=None):
        """
        `<http://www.elastic.co/guide/en/watcher/current/appendix-api-put-watch.html>`_

        :arg id: Watch ID
        :arg body: The watch
        :arg active: Specify whether the watch is in/active by default
        :arg master_timeout: Specify timeout for watch write operation
        """
        for param in (id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")
        return self.transport.perform_request('PUT', _make_path('_xpack',
            'watcher', 'watch', id), params=params, body=body)

    @query_params('force', 'master_timeout')
    def delete_watch(self, id, params=None):
        """
        `<http://www.elastic.co/guide/en/watcher/current/appendix-api-delete-watch.html>`_

        :arg id: Watch ID
        :arg force: Specify if this request should be forced and ignore locks
        :arg master_timeout: Specify timeout for watch write operation
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")
        return self.transport.perform_request('DELETE', _make_path('_xpack',
            'watcher', 'watch', id), params=params)

    @query_params()
    def get_watch(self, id, params=None):
        """
        `<http://www.elastic.co/guide/en/watcher/current/appendix-api-get-watch.html>`_

        :arg id: Watch ID
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")
        return self.transport.perform_request('GET', _make_path('_xpack',
            'watcher', 'watch', id), params=params)

    @query_params()
    def stats(self, metric=None, params=None):
        """
        `<http://www.elastic.co/guide/en/watcher/current/appendix-api-stats.html>`_

        :arg metric: Controls what additional stat metrics should be include in
            the response
        """
        return self.transport.perform_request('GET', _make_path('_xpack',
            'watcher', 'stats', metric), params=params)

    @query_params()
    def restart(self, params=None):
        """
        `<http://www.elastic.co/guide/en/watcher/current/appendix-api-service.html>`_
        """
        return self.transport.perform_request('POST', '/_xpack/watcher/_restart',
            params=params)

