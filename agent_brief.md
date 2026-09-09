# Project Brief: Issue Search and Filtering

## Mission

Improve the mini issue tracker by allowing API users to search and filter the
existing issue list.

## Current State

The application is a FastAPI backend that stores issues in memory. It supports
creating, listing, retrieving, updating, and deleting issues.

The current GET /issues endpoint always returns every stored issue. It does not
allow users to narrow the results.

## Required Outcome

Enhance GET /issues so API users can:

- Search issues using text from appropriate issue fields.
- Filter issues by status.
- Combine search and status filtering.
- Continue retrieving every issue when no filters are supplied.
- Receive an empty list when no issues match.

## Acceptance Criteria

- Search is case-insensitive.
- Search considers both issue titles and descriptions.
- Status filtering is case-insensitive.
- Search and status filters can be used together.
- Existing behaviour remains unchanged when no query parameters are supplied.
- Existing CRUD tests continue to pass.
- Automated tests cover the new behaviour and important edge cases.
- The README explains how to install, run, test, and use the filtering feature.
- No unnecessary dependencies are introduced.
- No unrelated functionality is changed.

## Constraints

- Work within the existing FastAPI architecture.
- Continue using the existing in-memory issue storage.
- Do not introduce a database.
- Preserve the existing API response structure.
- Avoid unrelated refactoring.

## Permissions

Claude may:

- Read and edit files on the assignment branch.
- Run local tests and development commands.
- Add or update automated tests and documentation.

Claude must ask before:

- Adding or upgrading a dependency.
- Changing an existing request or response model.
- Renaming or removing an existing endpoint.
- Deleting or substantially restructuring files.

Claude may not:

- Push or merge changes.
- Deploy the application.
- Access external systems or credentials.
- Perform destructive Git operations.

## Completion Evidence

Claude should report:

- What it discovered about the existing implementation.
- Its implementation decisions.
- Files changed.
- Tests and checks run, with their results.
- Remaining limitations or risks.