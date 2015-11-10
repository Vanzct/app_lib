###本文档内容是服务器配置服务相关

# 服务配置请参考：
  http://www.tuicool.com/articles/zUvqMr

# 用到的框架或软件有：
  flask:python web开发的框架
  virtualenv:单独建立python环境的python插件
  uwsgi:flask和nginx对接的标准插件
  supervisor:自动启动uwsgi服务的服务管理插件
  nginx:请求转发的服务器

pip install --upgrade pip

# 依赖包写入 requirements.txt
  pip freeze >requirements.txt

# 安装依赖包
  pip install -r requirements.txt

服务器地址：
ssh root@123.57.14.49

vim /etc/supervisord.conf

sudo service supervisord start

netstat -tln  查看端口使用情况
netstat -tln | grep 8083  则是只查看端口8083的使用情况
lsof -i :8083 端口被哪个进程占用