# README

# demo_django

## Create sales automactily

We create a script where you pass a valid store_id and the script make a sale.

```bash
cd ./scripts
python3 create_sale.py <STORE_ID>
```

- Create a job in crontab

```bash
vim /etc/crontab
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
*/2 * * * * root python3 /root/demo_django/scripts/create_sales.py 1
*/2 * * * * root python3 /root/demo_django/scripts/create_sales.py 2
*/2 * * * * root python3 /root/demo_django/scripts/create_sales.py 3
*/2 * * * * root python3 /root/demo_django/scripts/create_sales.py 4
*/2 * * * * root python3 /root/demo_django/scripts/create_sales.py 5
*/2 * * * * root python3 /root/demo_django/scripts/create_sales.py 6
```