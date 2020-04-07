

```shell
 $ ./manage.py runserver
Watching for file changes with StatReloader
[2020-02-14 08:15:32,115] INFO autoreload.run_with_reloader Watching for file changes with StatReloader
Performing system checks...

System check identified some issues:

WARNINGS:
?: (urls.W005) URL namespace 'the_django_plotly_dash' isn't unique. You may not be able to reverse all URLs in this namespace

System check identified 1 issue (0 silenced).
February 14, 2020 - 08:15:33
Django version 3.0.3, using settings 'tph.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[14/Feb/2020 08:15:38] "GET /static/CACHE/css/tph.8820d1c07f9e.css HTTP/1.1" 304 0
[2020-02-14 08:15:38,108] DEBUG view_bme280list.get_queryset all
[14/Feb/2020 08:15:39] "GET /monitor/v1/bme280s HTTP/1.1" 200 3620
[14/Feb/2020 08:15:39] "GET /static/CACHE/css/tph.8820d1c07f9e.css HTTP/1.1" 200 175976
^C[2020-02-14 08:27:09,536] DEBUG selector_events.__init__ Using selector: KqueueSelector
[2020-02-14 08:27:09,793] DEBUG selector_events.__init__ Using selector: KqueueSelector
~/Develop/deploy/rpi_tph $ ./manage.py runserver
Watching for file changes with StatReloader
[2020-02-14 08:28:18,254] INFO autoreload.run_with_reloader Watching for file changes with StatReloader
Performing system checks...

System check identified some issues:

WARNINGS:
?: (urls.W005) URL namespace 'the_django_plotly_dash' isn't unique. You may not be able to reverse all URLs in this namespace

System check identified 1 issue (0 silenced).
February 14, 2020 - 08:28:19
Django version 3.0.3, using settings 'tph.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[14/Feb/2020 08:28:35] "GET /static/CACHE/css/tph.8820d1c07f9e.css HTTP/1.1" 304 0
[2020-02-14 08:28:35,427] DEBUG view_tph_chart.tph_chart_view start
[2020-02-14 08:28:35,433] DEBUG view_tph_chart.tph_chart_view end
[14/Feb/2020 08:28:36] "GET /monitor/v1/chart HTTP/1.1" 200 1806
[14/Feb/2020 08:28:36] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_renderer/polyfill@7.v1_2_2m1580837354.7.0.min.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:36] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_renderer/react@16.v1_2_2m1580837354.8.6.min.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:36] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_renderer/react-dom@16.v1_2_2m1580837354.8.6.min.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:36] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_html_components/dash_html_components.v1_0_2m1573762545.min.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:36] "GET /monitor/django_plotly_dash/app/tph_chart/ HTTP/1.1" 200 2067
[14/Feb/2020 08:28:37] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dpd_components/bundle.v0_1_0m1531261909.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:36] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_core_components/dash_core_components.v1_8_0m1580836777.min.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:36] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_core_components/dash_core_components-shared.v1_8_0m1580836777.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:37] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_renderer/prop-types@15.v1_2_2m1580837354.7.2.min.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:37] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_renderer/dash_renderer.v1_2_2m1580837364.min.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:37] "GET /static/CACHE/css/tph.8820d1c07f9e.css HTTP/1.1" 200 175976
[14/Feb/2020 08:28:37] "GET /static/dash/component/dpd_components/bundle.js HTTP/1.1" 200 4653
[14/Feb/2020 08:28:37] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-dependencies HTTP/1.1" 200 187
[14/Feb/2020 08:28:37] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-layout HTTP/1.1" 200 550
[14/Feb/2020 08:28:37] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_core_components/async~datepicker.v1_8_0m1580836772.js HTTP/1.1" 302 0
[2020-02-14 08:28:37,792] DEBUG tph_chart.tph_chart_div start
[2020-02-14 08:28:37,793] DEBUG tph_chart.tph_chart_div timezone: 2020-02-13 23:28:37.793168+00:00, datetime: 2020-02-14 08:28:37.793405
[2020-02-14 08:28:37,793] DEBUG tph_chart.tph_chart_div args: ('2020-02-07T00:00:00', '2020-02-14T23:59:59.999999')
[2020-02-14 08:28:37,794] DEBUG tph_chart.tph_chart_div start date: 2020-02-07T00:00:00+09:00, end date: 2020-02-14T23:59:59.999999+09:00
[2020-02-14 08:28:37,794] DEBUG tph_chart.tph_chart_div kwargs: {}
[14/Feb/2020 08:28:37] "GET /static/dash/component/dash_core_components/async~datepicker.js HTTP/1.1" 200 556801
[2020-02-14 08:28:37,891] DEBUG tph_chart.tph_chart_div bme280s.count: 227
[2020-02-14 08:28:37,892] DEBUG tph_chart.tph_chart_div temperature: 21.398006799198328
[2020-02-14 08:28:40,103] DEBUG tph_chart.tph_chart_div end
[14/Feb/2020 08:28:40] "POST /monitor/django_plotly_dash/app/tph_chart/_dash-update-component HTTP/1.1" 200 46199
[14/Feb/2020 08:28:40] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_core_components/async~graph.v1_8_0m1580836772.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:40] "GET /monitor/django_plotly_dash/app/tph_chart/_dash-component-suites/dash_core_components/async~plotlyjs.v1_8_0m1580836772.js HTTP/1.1" 302 0
[14/Feb/2020 08:28:40] "GET /static/dash/component/dash_core_components/async~graph.js HTTP/1.1" 200 16598
[14/Feb/2020 08:28:40] "GET /static/dash/component/dash_core_components/async~plotlyjs.js HTTP/1.1" 200 3310800
^C[2020-02-14 08:28:59,575] DEBUG selector_events.__init__ Using selector: KqueueSelector
[2020-02-14 08:28:59,835] DEBUG selector_events.__init__ Using selector: KqueueSelector
```

```shell
$ gunicorn --env DJANGO_SETTING_MODEL=tph.settings tph.wsgi
[2020-02-14 08:29:06 +0900] [8064] [INFO] Starting gunicorn 20.0.4
[2020-02-14 08:29:06 +0900] [8064] [INFO] Listening at: http://127.0.0.1:8000 (8064)
[2020-02-14 08:29:06 +0900] [8064] [INFO] Using worker: sync
[2020-02-14 08:29:06 +0900] [8082] [INFO] Booting worker with pid: 8082
[2020-02-14 08:29:18,840] DEBUG view_tph_chart.tph_chart_view start
[2020-02-14 08:29:18,846] DEBUG selector_events.__init__ Using selector: KqueueSelector
[2020-02-14 08:29:18,851] DEBUG view_tph_chart.tph_chart_view end
Not Found: /static/CACHE/css/tph.8820d1c07f9e.css
[2020-02-14 08:29:19,868] WARNING log.log_response Not Found: /static/CACHE/css/tph.8820d1c07f9e.css
Not Found: /static/CACHE/css/tph.8820d1c07f9e.css
[2020-02-14 08:29:19,948] WARNING log.log_response Not Found: /static/CACHE/css/tph.8820d1c07f9e.css
Not Found: /static/admin/fonts/Roboto-Light-webfont.woff
[2020-02-14 08:29:20,532] WARNING log.log_response Not Found: /static/admin/fonts/Roboto-Light-webfont.woff
[2020-02-14 08:29:20,588] DEBUG tph_chart.tph_chart_div start
[2020-02-14 08:29:20,591] DEBUG tph_chart.tph_chart_div timezone: 2020-02-13 23:29:20.589949+00:00, datetime: 2020-02-14 08:29:20.589991
[2020-02-14 08:29:20,595] DEBUG tph_chart.tph_chart_div args: ('2020-02-07T00:00:00', '2020-02-14T23:59:59.999999')
[2020-02-14 08:29:20,598] DEBUG tph_chart.tph_chart_div start date: 2020-02-07T00:00:00+09:00, end date: 2020-02-14T23:59:59.999999+09:00
[2020-02-14 08:29:20,599] DEBUG tph_chart.tph_chart_div kwargs: {}
[2020-02-14 08:29:20,631] DEBUG tph_chart.tph_chart_div bme280s.count: 227
[2020-02-14 08:29:20,632] DEBUG tph_chart.tph_chart_div temperature: 21.398006799198328
[2020-02-14 08:29:21,974] DEBUG tph_chart.tph_chart_div end
^C[2020-02-14 08:29:46 +0900] [8064] [INFO] Handling signal: int
[2020-02-14 08:29:46 +0900] [8082] [INFO] Worker exiting (pid: 8082)
[2020-02-14 08:29:47 +0900] [8064] [INFO] Shutting down: Master
```

```shell
$ ls -l static/CACHE/css/
total 2872
-rw-r--r--  1 mitsu  staff  176353 Feb 13 08:23 bootstrap.d78e22d7bdb1.css
-rw-r--r--  1 mitsu  staff  282724 Feb 13 08:23 bootstrap.ee68a80e92b3.css
-rw-r--r--  1 mitsu  staff  176372 Feb 13 08:23 tph.12cc420fb413.css
-rw-r--r--  1 mitsu  staff  176316 Feb 13 08:23 tph.5169b846b712.css
-rw-r--r--  1 mitsu  staff  175976 Feb 14 08:29 tph.8820d1c07f9e.css
-rw-r--r--  1 mitsu  staff  176353 Feb 13 08:23 tph.d78e22d7bdb1.css
-rw-r--r--  1 mitsu  staff       0 Feb 13 08:23 tph.e3b0c44298fc.css
-rw-r--r--  1 mitsu  staff  282724 Feb 13 08:23 tph.ee68a80e92b3.css
