# Contributing to valorantbp

When contributing to the development of valorantbp, please first discuss the change you wish to make via issue, email, or any other method with the maintainers before making a change.
Please note we have a [Code of Conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.
## Standard Commit Messages

This project is using the [Conventional Commits](https://www.conventionalcommits.org/) specifications. Please follow these steps to ensure your commit messages are standardized:

- Commit messages should have this format: `<type>[optional scope]: <description>`
- Type must be one of the following:
  * **docs**: Changes made in documentation
  * **feat**: If you have added a new feature
  * **style**: Changes that do not affect the meaning of the code (whitespace, formatting, missing semi-colons, etc)
- Scope should be `ui` or `global`
- Example: `feat(ui): added image gallery`

## Before making PR
- Run `git fetch upstream` & `git rebase upstream/master` to fetch updated codebase into your local repository before creating any new branch.
- Run `git checkout -b <your-branch-name>`
  
## How to setup the project locally

1. Fork and clone the repository.
2. Add remote upstream `git remote add upstream https://github.com/alanyee/valorantbp`
