
# PHP proxy

Using a php server as a proxy

## How it works

- Running a local proxy
- Php server opens two sockets with your computer and any server
- As long as php session keeps open, routes traffic between two sockets

## How to use

  

1. Download all files, and upload `index.php` to your host
2. Configure `http_proxy.py` to connect to your php server. Fill your `php_host` and `php_port`
3. Configure `index.php` to connect to your local machine. Fill `$my_address` and `$my_port`. Requires an ipv4 or ipv6 address and configured firewall.
4. Configure your browser to use proxy
5. Run `http_proxy.py`

# To do

- Proxy protocols other than https
- Add authentication
- Add error and closing handling 