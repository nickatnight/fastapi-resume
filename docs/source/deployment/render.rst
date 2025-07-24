Render
======

You can deploy your resume API to Render with the following steps:

1. Create a GitHub project with that includes your resume YAML file eg. ``resume.yaml``
2. Connect that repo to Render
3. Add this ``render.yaml`` file to the root of your repo:

    .. code-block:: yaml

        services:
          - type: web
            name: fast-resume
            runtime: python
            plan: starter
            # Trigger a deploy only if the linked branch's CI checks pass
            autoDeployTrigger: checksPass
            # Web services only. The path of the service's health check endpoint for zero-downtime deploys.
            healthCheckPath: /health
            buildCommand: uv pip install fastapi-resume
            # The command to run when starting the Docker-based service.
            startCommand: fast-resume serve resume.yaml --host 0.0.0.0 --port $PORT

            # Environment variables for the application
            envVars:
            - key: UV_VERSION
                value: '0.7.18'
            - key: PYTHON_VERSION
                value: '3.12.11'

4. Go to your Render dashboard a go to New -> Blueprint
5. Your site will then be available at ``https://<project-name>.onrender.com``
