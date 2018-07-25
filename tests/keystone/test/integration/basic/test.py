def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.14")


def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


def test_nginx_public_keystone_is_listening(host):
    socket = host.socket("tcp://0.0.0.0:5000")
    assert socket.is_listening


def test_nginx_admin_keystone_is_listening(host):
    socket = host.socket("tcp://0.0.0.0:35357")
    assert socket.is_listening


def test_nginx_configuration(host):
    assert host.run("/usr/sbin/nginx -t").rc == 0


def test_nginx_keystone_public_endpoint(host):
    request = host.run("curl -v http://127.0.0.1:5000/v3")
    assert 'HTTP/1.1 200 OK' in request.stderr
    assert 'x-openstack-request-id' in request.stderr


def test_nginx_keystone_admin_endpoint(host):
    request = host.run("curl -v http://127.0.0.1:35357/v3")
    assert 'HTTP/1.1 200 OK' in request.stderr
    assert 'x-openstack-request-id' in request.stderr
