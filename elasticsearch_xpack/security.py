from elasticsearch.client.utils import NamespacedClient, query_params, _make_path, SKIP_IN_PATH

class SecurityClient(NamespacedClient):
    @query_params('refresh')
    def delete_user(self, username, params=None):
        """
        `<https://www.elastic.co/guide/en/x-pack/current/security-api-users.html#security-api-delete-user>`_

        :arg username: username
        :arg refresh: Refresh the index after performing the operation
        """
        if username in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'username'.")
        return self.transport.perform_request('DELETE', _make_path('_xpack',
            'security', 'user', username), params=params)

    @query_params()
    def get_user(self, username=None, params=None):
        """
        `<https://www.elastic.co/guide/en/x-pack/current/security-api-users.html#security-api-get-user>`_

        :arg username: A comma-separated list of usernames
        """
        return self.transport.perform_request('GET', _make_path('_xpack',
            'security', 'user', username), params=params)

    @query_params('refresh')
    def put_role(self, name, body, params=None):
        """
        `<https://www.elastic.co/guide/en/x-pack/current/security-api-roles.html#security-api-put-role>`_

        :arg name: Role name
        :arg body: The role to add
        :arg refresh: Refresh the index after performing the operation
        """
        for param in (name, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")
        return self.transport.perform_request('PUT', _make_path('_xpack',
            'security', 'role', name), params=params, body=body)

    @query_params()
    def authenticate(self, params=None):
        """
        `<https://www.elastic.co/guide/en/x-pack/current/security-api-authenticate.html>`_
        """
        return self.transport.perform_request('GET',
            '/_xpack/security/_authenticate', params=params)

    @query_params('refresh')
    def put_user(self, username, body, params=None):
        """
        `<https://www.elastic.co/guide/en/x-pack/current/security-api-users.html#security-api-put-user>`_

        :arg username: The username of the User
        :arg body: The user to add
        :arg refresh: Refresh the index after performing the operation
        """
        for param in (username, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")
        return self.transport.perform_request('PUT', _make_path('_xpack',
            'security', 'user', username), params=params, body=body)

    @query_params('usernames')
    def clear_cached_realms(self, realms, params=None):
        """
        `<https://www.elastic.co/guide/en/x-pack/current/security-api-clear-cache.html>`_

        :arg realms: Comma-separated list of realms to clear
        :arg usernames: Comma-separated list of usernames to clear from the
            cache
        """
        if realms in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'realms'.")
        return self.transport.perform_request('POST', _make_path('_xpack',
            'security', 'realm', realms, '_clear_cache'), params=params)

    @query_params('refresh')
    def change_password(self, body, username=None, params=None):
        """
        `<https://www.elastic.co/guide/en/x-pack/current/security-api-change-password.html>`_

        :arg body: the new password for the user
        :arg username: The username of the user to change the password for
        :arg refresh: Refresh the index after performing the operation
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")
        return self.transport.perform_request('PUT', _make_path('_xpack',
            'security', 'user', username, '_password'), params=params,
            body=body)

    @query_params()
    def get_role(self, name=None, params=None):
        """
        `<https://www.elastic.co/guide/en/x-pack/current/security-api-roles.html#security-api-get-role>`_

        :arg name: Role name
        """
        return self.transport.perform_request('GET', _make_path('_xpack',
            'security', 'role', name), params=params)

    @query_params()
    def clear_cached_roles(self, name, params=None):
        """
        `<https://www.elastic.co/guide/en/x-pack/current/security-api-roles.html#security-api-clear-role-cache>`_

        :arg name: Role name
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")
        return self.transport.perform_request('POST', _make_path('_xpack',
            'security', 'role', name, '_clear_cache'), params=params)

    @query_params('refresh')
    def delete_role(self, name, params=None):
        """
        `<https://www.elastic.co/guide/en/x-pack/current/security-api-roles.html#security-api-delete-role>`_

        :arg name: Role name
        :arg refresh: Refresh the index after performing the operation
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")
        return self.transport.perform_request('DELETE', _make_path('_xpack',
            'security', 'role', name), params=params)

