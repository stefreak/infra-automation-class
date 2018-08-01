template {
  source = "/etc/consul-templates/haproxy.cfg.ctmpl"
  destination = "/etc/haproxy/haproxy.cfg"
  command = "systemctl restart haproxy"
}
