该包是一个共用基础测试包,支持python3.4+．
主要功能：
1．支持web测试
2．支持接口测试
3. 支持mysql,oracle操作

=================安装步骤=====================
1. 安装python3.4+;
2. 安装pip
3.安装cx-Oracle（windonw,linux安装有些复杂，请在网上所搜下指导）
4. pip install -r requirements.txt(安装本包依赖的其他包)
5. 在dist里安装本包的最新或者自己生产包，再安装

========使用===============================
下载本包的示例项目，根据自己的项目进行裁剪:
github地址：https://github.com/benhuangyong/demoProject


============打包，安装包=============
查看包文件：
python setup.py check
打包命令：
python setup.py sdist
安装包：
sudo pip install pyQa-x.x.x.tar.gz
卸载包：
sudo pip uninstall pyQa

=========支持oracle数据库==================
cx_Oracle安装：(ubuntu)
该报需要支持oracel的操作
１．安装dpk
apt-get isntall  oracle-instantclient12.1-basic_12.1.0.2.0-1_amd64.deb
apt-get isntall  oracle-instantclient12.1-devel_12.1.0.2.0-1_amd64.deb
apt-get isntall oracle-instantclient12.1-sqlplus_12.1.0.2.0-1_amd64.deb

２．安装python3-dev
apt-get isntall  python3-dev

3. 拷贝libaio.so.1　libaio.so.1.0.1到
/lib/x86_64-linux-gnu/
/lib/x86_64-linux-gnu

４．/etc/profile　添加环境变量
export ORACLE_HOME=/usr/lib/oracle/12.1/client64

export ORACLE_BASE=/usr/lib/oracle/12.1

export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH

export NLS_LANG=AMERICAN_AMERICA.AL32UTF8

５．安装ox-Oracle
pip install cx-Oracle


==================文档生成=====================
１．　pip install Sphinx
2.  进入项目目录，运行　sphinx-quickstart

注意：autodoc: automatically insert docstrings from modules (y/n) [n]　这个选项要选择 y，文档目录填　doc
3. 进入doc目录，找到conf.py目录，添加
　import sys
sys.path.insert(0, '..')
rm *.rst
４．sphinx-apidoc -o . ..
５．make html

注意：auto insert dostring哪一个选项要选择 y，文档目录填　doc
3. 进入doc目录，找到conf.py目录，添加
　import sys
sys.path.insert(0, '..')
４．sphinx-apidoc -o . ..
５．make html


作者联系方式：
249773304@qq.com