import pytest
import testinfra
def test_alpine(host):
    os_ver = host.file("/etc/os-release")
    assert os_ver.contains("Alpine")

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.")


