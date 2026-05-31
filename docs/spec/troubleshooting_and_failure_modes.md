# Troubleshooting And Failure Modes

## Weak Generated System

If the generated system is too generic, the agent probably did not inspect enough repository context.

Fix:
- rerun initialization with explicit permission for a broader first pass
- require more project-specific routes
- require generated files to include exact paths

## Negative Token Savings

Negative savings does not always mean the workflow failed.

Common causes:
- baseline came from post-edit changed context instead of original preflight
- task required many source files
- broad context baseline was too narrow
- source files were counted multiple times
- broad context was not actually the realistic alternative

Fix:
- ensure baseline snapshot exists
- ensure reporter prefers session baseline
- pass inspected files explicitly

## Agent Skips Workflow

Add to generated instructions:
- even compiler-error fixes should use a narrow workflow unless no edit is needed
- user does not need to request the system explicitly

## Agent Reports Filenames Only

Fix generated instructions:
- require full relative paths everywhere

## Agent Reads Runtime Folders

Update:
- avoid paths in routes
- editing rules
- context generator hard excludes
