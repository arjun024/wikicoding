#! /bin/bash

mysqldump -u <<redacted>> -p <<redacted>> wikicoding_db | gzip > `date +%Y%m%d%H%M`.sql.gz
