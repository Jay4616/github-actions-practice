# Day 44 – Secrets, Artifacts & Running Real Tests in CI

## Key Learnings & Task Answers

### 1. Why should you never print secrets in CI logs?
Although GitHub Actions automatically masks registered secrets with `***`, printing them directly poses severe security risks. Secrets can be accidentally exposed through base64 encoding, stack traces, unmasked debug variables, or third-party actions/scripts reading the console log.

### 2. When would you use artifacts in a real pipeline?
Artifacts store build outputs or reports that need to be shared across jobs or accessed after a workflow finishes. Common uses:
- Storing automated test reports and code coverage metrics.
- Passing built application binaries or web bundles from a `build` job to a `deploy` job.
- Preserving security scanning and audit logs.

### 3. What is being cached and where is it stored?
- **What is cached:** External package dependencies (e.g., `node_modules`, `pip` packages, Maven dependencies).
- **Where it is stored:** GitHub-hosted remote storage mapped to your repository, indexed by a unique cache key (like a hash of `requirements.txt`).
