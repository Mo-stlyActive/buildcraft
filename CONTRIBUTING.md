# Contributing to BuildCraft AI

## Version Control & Branching Strategy

- **main**: Always production-ready. Only thoroughly reviewed, tested code is merged here.
- **Feature branches**: Create a new branch for each feature, bugfix, or task.
  - Naming: `feat/<feature-name>`, `fix/<bug-description>`, `chore/<task>`, etc.
  - Example: `feat/oblivion-data-scraper`, `fix/login-bug`, `chore/update-readme`
- **Pull Requests (PRs)**: All changes to `main` must go through a PR. PRs should reference the relevant task or PRD and require at least one review before merging.
- **Commit Messages**: Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):
  - `feat: add new build planner UI`
  - `fix: correct skill calculation bug`
  - `chore: update dependencies`
- **Release Tags**: Tag releases on `main` as `v1.0.0`, `v1.1.0`, etc.
- **Protected Branches**: Protect `main` to require PRs and reviews.

## Workflow

1. Create a new branch for your work.
2. Make your changes and commit with a conventional commit message.
3. Push your branch and open a pull request against `main`.
4. Reference the relevant task or PRD in your PR description.
5. Request a review and make any necessary changes.
6. Once approved, merge your PR.

For more details, see the project README. 