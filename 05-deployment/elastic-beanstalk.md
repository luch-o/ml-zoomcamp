# Deploying to AWS Elastic Beanstalk

Elastic Beanstalk is an AWS service in which we can deploy our applications without worrying for the underlying infrastructure. Is a Platform as a Sevice (Paas) which provisions the infrastructure for us so our application can run in the AWS cloud. This is a free service, but we have to pay for the infrastructure provisioned by EB such as EC2 instances, load balancers, etc.

## Prerequisites

- Having an AWS account
- Configure programatic access (i.e. credentials file)

## Installing the EB CLI

We can install the Elastic Beanstalk CLI as development dependency using pipenv

```bash
$ pipenv instal awsebcli --dev
```

## Deploying the Application with EB

1. Create the app with this command
    ```bash
    $ eb init -p docker -r us-east-1 prediction-service
    ```
    - `-p` argument to set the platform
    - `-r` argument to set the region in which we want to deploy our app
    - The name of the application as a positional argument

2. Test locally by running the application with the following command:
    ```
    $ eb local run --port 9696
    ```

3. Deploy to the cloud with this command
    ```
    $ eb create prediction-service-env
    ```
    Passing the environment name as a positional argument

> **Warning**
>
> These steps with the default configuration will expose the service publicly  
>

## Terminate the EB Environment

To terminate the environment and avoid incurring charges run the following command

```
$ eb terminate prediction-service-env
```

Passing the environment name as a positional parameter, we will be asked for confirmation to delete al underlying resources.
