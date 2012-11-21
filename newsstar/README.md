## FAQ

When in trouble, run newsstar with `-vv` CLO.

* __newsstar doesn't post anything__.

  Make sure to uncomment & set in `/etc/newsstar/main.cf` the following
  variables:
  
  * `spool_dir`
  * `active_file`
  * `outgoing_dir`
  * `articles_dir`
  
  If you don't do this, articles will be collected in `outgoing_dir` but
  will never leave your machine.
