# python-do-app-boilerplate

## Description
Boilerplate for running Python applications using [DigitalOcean App platform](https://www.digitalocean.com/docs/app-platform/)

The boilerplate app contains:
- 1 service
- 1 static site
- 1 worker
- 1 dev database

## Commands
1. Install [doctl](https://www.digitalocean.com/docs/apis-clis/doctl/how-to/install/)
2. Run `doctl apps create --spec app.yaml` to create the app
3. Run `doctl apps update <app id> --spec app.yaml` to update the app
4. Run `doctl apps logs <app id>` to get app logs

## App Specification Reference
https://www.digitalocean.com/docs/app-platform/references/app-specification-reference/

## Example
