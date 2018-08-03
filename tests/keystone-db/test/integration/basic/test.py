def test_mysql_is_installed(host):
    mysql = host.package("mysql-server")
    assert mysql.is_installed
    assert mysql.version.startswith("5.7.23")


def test_mysql_running_and_enabled(host):
    mysql = host.service("mysql")
    assert mysql.is_running
    assert mysql.is_enabled


def test_mysql_is_listening(host):
    socket = host.socket("tcp://0.0.0.0:3306")
    assert socket.is_listening


def test_keystone_database_tables_exist(host):
    query = host.run("mysql -uroot keystone -e 'show tables;'")
    assert 'access_token' in query.stdout
    assert 'endpoint' in query.stdout
    assert 'user' in query.stdout
    assert 'project' in query.stdout


def test_keystone_database_allowed_remote_users(host):
    query = host.run("mysql -uroot mysql -sN -e 'select User,Host from user where Host!=\"localhost\" and User!=\"keystone\";'")
    assert len(query.stdout) == 0
    assert query.rc == 0

