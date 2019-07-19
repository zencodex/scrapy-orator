## scrapy 如何整合 orator

orator 是 python 的 ORM 数据库操作框架。
数据库初始化代码在 `models/__init__.py` 中，建立关联的代码如下：

```py
import os
import yaml
from orator import DatabaseManager, Model
from pathlib import Path

__config = str(Path(os.path.realpath(__file__)).parents[1]) + '/orator.yml'
db = DatabaseManager(yaml.load(open(__config))['databases'])

Model.set_connection_resolver(db)
```

这么做的好处是，spider 里面引入 model 时，直接使用：

  from models.noi2018_award import Noi2018Award

`models/__init__.py` 会自动调用，这样数据库配置管理就自动完成了

## orator.yml 配置

```
databases:
  pgsql:
    driver: pgsql
    database: 100kwhy
    user: postgres
    password: ''
    prefix: ''
```

新建 model 命令：

  orator make:model table_name -m

## orator 常用命令

```sh
Usage:
  command [options] [arguments]

Options:
  -h, --help                      Display this help message
  -q, --quiet                     Do not output any message
  -V, --version                   Display this application version
      --ansi                      Force ANSI output
      --no-ansi                   Disable ANSI output
  -n, --no-interaction            Do not ask any interactive question
  -v|vv|vvv, --verbose[=VERBOSE]  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

Available commands:
  help              Displays help for a command
  list              Lists commands
  migrate           Run the database migrations.
 db
  db:seed           Seed the database with records.
 make
  make:migration    Create a new migration file.
  make:model        Creates a new Model class.
  make:seed         Create a new seeder file.
 migrate
  migrate:install   Create the migration repository.
  migrate:refresh   Reset and re-run all migrations.
  migrate:reset     Rollback all database migrations.
  migrate:rollback  Rollback the last database migration.
  migrate:status    Show a list of migrations up/down.
```