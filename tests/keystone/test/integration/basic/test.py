def test_keystone_is_installed(host):
    keystone = host.package("keystone")
    assert keystone.is_installed


def test_apache2_is_installed(host):
    apache2 = host.package("apache2")
    assert apache2.is_installed


def test_apache2_running_and_enabled(host):
    apache2 = host.service("apache2")
    assert apache2.is_running
    assert apache2.is_enabled


def test_apache2_public_keystone_is_listening(host):
    socket = host.socket("tcp://0.0.0.0:5000")
    assert socket.is_listening


def test_apache2_admin_keystone_is_listening(host):
    socket = host.socket("tcp://0.0.0.0:35357")
    assert socket.is_listening


def test_nginx_keystone_public_endpoint(host):
    request = host.run("curl -v http://127.0.0.1:5000/v3")
    assert 'HTTP/1.1 200 OK' in request.stderr
    assert 'x-openstack-request-id' in request.stderr


def test_nginx_keystone_admin_endpoint(host):
    request = host.run("curl -v http://127.0.0.1:35357/v3")
    assert 'HTTP/1.1 200 OK' in request.stderr
    assert 'x-openstack-request-id' in request.stderr
