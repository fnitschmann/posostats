# This script could and should be used in server envs to update the stats
# regulary
from posostats import FacebookUpdater, TwitterUpdater

print("===Started to fetch current posts for all accounts")
FacebookUpdater().update_accounts_and_posts()
TwitterUpdater().update_accounts_and_posts()
print("===Finished")
