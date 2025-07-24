Quickstart
==========

This package is mean to be super simple to use, as it is a thin wrapper around FastAPI.

Start by installing the package:

.. code-block:: bash

    pip install fastapi-resume

Then create a YAML file with your resume data.

.. tip::

   The required top level keys are ``name``, ``about``, ``position``, ``experience``, ``education``, ``skills``, ``projects``, and ``contact``.

.. code-block:: yaml

    ---
    name:
      first: John
      middle: A.
      last: Doe
    about: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    position: Senior Software Engineer

    experience:
    - company: Tech Corp
      position: Senior Software Engineer
      timeperiod: January 2023 - Present
      description:
          - Lorem ipsum dolor sit amet, consectetur adipiscing elit
          - Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
          - Ut enim ad minim veniam, quis nostrud exercitation ullamco
          - Duis aute irure dolor in reprehenderit in voluptate velit esse
      website: https://techcorp.com

    - company: Startup Inc
      position: Software Engineer
      timeperiod: March 2021 - December 2022
      description:
          - Lorem ipsum dolor sit amet, consectetur adipiscing elit
          - Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
          - Ut enim ad minim veniam, quis nostrud exercitation ullamco
      website: https://startupinc.com

    education:
    - degree: Bachelor of Science, Computer Science
    timeperiod: 2017 - 2021
    school: University of Technology

    skills:
    - languages_frameworks:
      - Python
      - NodeJS
      - TypeScript
      - Java
    - infrastructure_tooling:
      - Kubernetes
      - Codecov
    - cloud_devops:
      - Docker
      - Terraform
    - databases:
      - PostgreSQL
      - MongoDB
      - Redis

    projects:
    - name: E-commerce Platform
      stack:
          - Django
          - React
          - PostgreSQL
          - Docker
      timeperiod: January 2023
      company: Tech Corp
      description: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.

    - name: API Gateway
      stack:
          - FastAPI
          - Redis
          - Docker
          - AWS
    timeperiod: June 2022
    company: Startup Inc
    description: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

    contact:
      email: john.doe@example.com
      phone: +1-555-123-4567
      street: 123 Main Street
      city: San Francisco
      website: johndoe.dev
      github: johndoe


Running the server
------------------

If your ``yaml`` file is at the root of your project, you can run the server with:

.. code-block:: bash

    $ fast-resume serve resume.yaml

This will serve your API at ``http://localhost:8000``.

The available endpoints are:

- ``/`` - Full resume info
- ``/basic`` - Basic info
- ``/experience`` - Experiences
- ``/education`` - Education
- ``/skills`` - Skills
- ``/skills/{category}`` - Skills by category
- ``/projects`` - Projects
