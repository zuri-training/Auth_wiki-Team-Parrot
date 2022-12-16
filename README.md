This is a solution to the [Project Phase , Milestone 1](https://w2pp.zuriboard.com/dashboard/team/148/task/45).

## Task Title: Documentation, Design Sketch


- [Overview](#overview)
  - [Resources](#Resources)
- [Autheticated Users](#Autheticated-Users)
  - [Un-Authenticated-users](#Un-Authenticated-users) 
  - [Database-Schema](#Database-Schema) 
  
- [TOOLS](#TOOLS)
- [Team Members](#Meet-Our-Team)
- [Author](#Author)
- [Acknowledgments](#Acknowledgments)
- [Hosted-Link](https://authwiki-team-parrot-production.up.railway.app/).
## Overview

A website by the name of AuthWiki offers a library of
authentication codes, explains each code in great depth,
and provides examples of how the codes operate.
Through AuthWiki, users have access to a community. In Auth-Wiki,
there are two types of users:
* Unauthenticated users and
* Authenticated users.

The unauthenticated user is only able to view and interact
with the documentation, browse the library in part,
access the most basic website information, and cannot download
code samples. The authenticated user, on the other hand, has
total access to the website and has the ability to contribute
via remarks and responses, view example usages, and download
code samples.
A non-registered user needs to sign up in order to have full access.

### Resources


 -[User-Research](https://www.figma.com/file/LJ5wmuoeKKIy59ENkW4nwM/USER-RESEARCH-(TEAM-PARROT)?node-id=0%3A1&t=iBcPUzWceGbFRBPE-1)
 - [Figma-Design](https://www.figma.com/file/sND8VLhfgWLIyNkJ5jTLeG/Team-Parrot?t=iBcPUzWceGbFRBPE-1)
  - [Style Guide]()
 - [Design-Sketch](https://www.figma.com/file/sND8VLhfgWLIyNkJ5jTLeG/Team-Parrot?node-id=186%3A75&t=tlVN5wBtH8bEtc73-1)




### Authenticated-users
- Full access to the plaftorm
- contribute, however, contribution should be limited to comments and reactions
- Able to view example usage
- Download code samples
### Un-Authenticated-users
- Visit the plaftorm to view basic information about it
- View and interact with the documentation
- Register to contribute
- Browse through library with limited information, download should not be available
### Database-Schema

The Backend Team Made tables/entities first:

User
Library
Comment
Code_snippets

Decided what attribute each was to have and assigned a private key or id to each table

Next worked on relationships between the tables.

User has a one to one  relationships with profile (user_id)

User has a one to many  relationships with comments and library (snippet_id, the library's id)

Library has a one to many  relationships with code_snippet and comments

Comments has a one to many  relationships with code_snippets

![](./auth_wiki/account/static/img/img.jpeg)
## TOOLS

- **Figma**
- **Django**
- **VSCode**
- **Python**
- **Pen**
- **Paper**


## Meet Our Team

- Rukayat Lamidi -- Product Designer
- Bright Uwaoma -- Product Designer
- Margaret Ekerendu -- Product Designer
- Ebubechukwu Ijezie-- Product Designer
- Ali Abdul-Quadir --  Product Designer
- Ige Jide  -- Product designer
- Loveth Iniovoghare  -- Product Designer
- Damilola Bilewu -- Product Designer
- Dorcas Abraham -- Product Designer
- Akinde Oluwadamilola -- Product Designer
- Oluwatimilehin Erinle -- Full stack Developer (Python)
- Oluwaseun Akanji -- FullStack Developer (Python)
- Khadija Danhassan - FullStack Developer (Python)
- Onokwakpor Oghenekparobo -- Frontend Developer
- Francis Chukwuoma -- Backend Developer (Python)
- Oyepitan Fortune --Backend Developer (Python)
- Henry Ugwu -- FullStack Developer (Python)
- Morah Chukwuemeka - FullStack Developer (Python)

## Author

 [Team-Parrot](https://github.com/zuri-training/Auth_wiki-Team-Parrot)

## Acknowledgments

Big Big respect to the Zuri Team
