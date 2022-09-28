# Xadmin for Django 4 [![Build Status](https://travis-ci.org/sshwsfc/xadmin.png?branch=master)](https://travis-ci.org/sshwsfc/xadmin)

Drop-in replacement of Django admin comes with lots of goodies, fully
extensible with plugin support, pretty UI based on Twitter Bootstrap.

## Live Demo

<http://demo.xadmin.io>

- User: admin
- Password: admin

## Features

- Drop-in replacement of Django admin
- Twitter Bootstrap based UI with theme support
- Extensible with plugin support
- Better filter, date range, number range, etc.
- Built-in data export with xls, csv, xml and json format
- Dashboard page with widget support
- In-site bookmarking
- Full CRUD methods

## Screenshots

![](https://raw.github.com/sshwsfc/django-xadmin/docs-chinese/docs/images/plugins/action.png)

![](https://raw.github.com/sshwsfc/django-xadmin/docs-chinese/docs/images/plugins/filter.png)

![](https://raw.github.com/sshwsfc/django-xadmin/docs-chinese/docs/images/plugins/chart.png)

![](https://raw.github.com/sshwsfc/django-xadmin/docs-chinese/docs/images/plugins/export.png)

![](https://raw.github.com/sshwsfc/django-xadmin/docs-chinese/docs/images/plugins/editable.png)

## Get Started

### Install

Xadmin is best installed via PyPI. To install the latest version, run:

```{.sourceCode .bash}
pip install xadmin2
```

or Install from github source:

```{.sourceCode .bash}
pip install git+git://github.com/wgbbiao/xadmin.git
```

## Install Requires

- [django](http://djangoproject.com) \>=3
- [django-crispy-forms](http://django-crispy-forms.rtfd.org) \>=1.8.1
  (For xadmin crispy forms)
- [django-reversion](https://github.com/etianen/django-reversion)>=3.0.4
  ([OPTION] For object history and reversion feature, please select
  right version by your django, see
  [changelog](https://github.com/etianen/django-reversion/blob/master/CHANGELOG.rst)
  )
- [django-formtools](https://github.com/django/django-formtools)>=2.1
  ([OPTION] For wizward form)
- [xlwt](http://www.python-excel.org/)>=1.3.0 ([OPTION] For export xls files)
- [xlsxwriter](https://github.com/jmcnamara/XlsxWriter) >=1.2.6([OPTION] For
  export xlsx files)

## Documentation

- English (coming soon)
- [Chinese](https://xadmin.readthedocs.org/en/latest/index.html)

## Changelogs

### 2.0.4

- Compact with Django4.0, Django3.0.

### 2.0.1

- Compact with Django2.0.

### 0.6.0

- Compact with Django1.9.
- Add Clock Picker widget for timepicker.
- Fixed some userface errors.

### 0.5.0

- Update fontawesome to 4.0.3
- Update javascript files to compact fa icons new version
- Update tests for the new instance method of the AdminSite class
- Added demo graphs
- Added quickfilter plugin.
- Adding apps_icons with same logic of apps_label_title.
- Add xlsxwriter for big data export.
- Upgrade reversion models admin list page.
- Fixed reverse many 2 many lookup giving FieldDoesNotExist error.
- Fixed user permission check in inline model.

Detail\_

- [detail](./changelog.md)

## Online Group

- QQ 群 : 282936295

## Run Demo Locally

```{.sourceCode .bash}
cd demo_app
./manage.py migrate
./manage.py runserver
```

Open <http://127.0.0.1:8000> in your browser, the admin user password is
`admin`

## Help

Help Translate : <http://trans.xadmin.io>
