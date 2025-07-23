from typing import NotRequired, TypedDict


class Name(TypedDict):
    first: str
    middle: NotRequired[str]
    last: NotRequired[str]


class Experience(TypedDict):
    company: str
    position: str
    timeperiod: str
    description: list[str]
    website: NotRequired[str]


class Education(TypedDict):
    degree: str
    timeperiod: str
    school: str


class Skill(TypedDict):
    languages_frameworks: list[str]
    infrastructure_tooling: list[str]
    cloud_devops: list[str]
    databases: list[str]


class Project(TypedDict):
    name: str
    stack: list[str]
    timeperiod: str
    company: str
    description: str


class Contact(TypedDict):
    email: str
    phone: NotRequired[str]
    street: NotRequired[str]
    city: NotRequired[str]
    website: NotRequired[str]


class ResumePartial(TypedDict):
    name: Name
    about: str
    position: str


class Resume(TypedDict):
    name: Name
    about: str
    position: str
    experience: list[Experience]
    education: list[Education]
    skills: list[Skill]
    projects: list[Project]
    contact: Contact
